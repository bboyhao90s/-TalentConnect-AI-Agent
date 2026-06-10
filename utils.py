"""
TalentConnect AI Agent — utilities.
File text extraction, OpenAI wrapper, and a simple in-session record store
with JSON export/import (Streamlit Community Cloud storage is ephemeral,
so export is the durable save).
"""

import io
import json
import os
from datetime import datetime

import streamlit as st


# ---------------------------------------------------------------------------
# OpenAI
# ---------------------------------------------------------------------------

def get_api_key() -> str | None:
    """Read the API key from Streamlit secrets or environment."""
    try:
        key = st.secrets.get("OPENAI_API_KEY", None)
    except Exception:
        key = None
    return key or os.environ.get("OPENAI_API_KEY")


def get_model() -> str:
    try:
        model = st.secrets.get("OPENAI_MODEL", None)
    except Exception:
        model = None
    return model or os.environ.get("OPENAI_MODEL") or "gpt-4o-mini"


def run_ai(system_prompt: str, user_content: str, temperature: float = 0.4) -> str:
    """Call the OpenAI chat completions API and return the text response.

    Raises RuntimeError with a human-readable message on failure so the UI
    can show it directly.
    """
    api_key = get_api_key()
    if not api_key:
        raise RuntimeError(
            "No OpenAI API key found. Add OPENAI_API_KEY in the app's Secrets "
            "(Streamlit Cloud: Manage app → Settings → Secrets)."
        )

    try:
        from openai import OpenAI

        client = OpenAI(api_key=api_key)
        response = client.chat.completions.create(
            model=get_model(),
            temperature=temperature,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_content},
            ],
        )
        return response.choices[0].message.content or ""
    except Exception as exc:  # surface a readable error in the UI
        raise RuntimeError(f"OpenAI request failed: {exc}") from exc


# ---------------------------------------------------------------------------
# File reading (PDF / DOCX / TXT)
# ---------------------------------------------------------------------------

def extract_text(uploaded_file) -> str:
    """Extract plain text from a Streamlit UploadedFile (pdf, docx, txt)."""
    if uploaded_file is None:
        return ""

    name = uploaded_file.name.lower()
    data = uploaded_file.read()
    uploaded_file.seek(0)

    if name.endswith(".pdf"):
        return _extract_pdf(data)
    if name.endswith(".docx"):
        return _extract_docx(data)
    # default: treat as text
    for encoding in ("utf-8", "utf-16", "gb18030", "latin-1"):
        try:
            return data.decode(encoding)
        except (UnicodeDecodeError, LookupError):
            continue
    return data.decode("utf-8", errors="replace")


def _extract_pdf(data: bytes) -> str:
    from pypdf import PdfReader

    reader = PdfReader(io.BytesIO(data))
    pages = [(page.extract_text() or "") for page in reader.pages]
    text = "\n\n".join(pages).strip()
    if not text:
        return "[This PDF appears to be scanned images with no extractable text. Please paste the text manually.]"
    return text


def _extract_docx(data: bytes) -> str:
    import docx

    document = docx.Document(io.BytesIO(data))
    parts = [p.text for p in document.paragraphs]
    for table in document.tables:
        for row in table.rows:
            parts.append(" | ".join(cell.text for cell in row.cells))
    return "\n".join(part for part in parts if part.strip())


def read_input(label: str, key: str, height: int = 220) -> str:
    """Render an upload-or-paste input block and return the resulting text."""
    uploaded = st.file_uploader(
        f"Upload {label} (PDF, DOCX or TXT)",
        type=["pdf", "docx", "txt"],
        key=f"{key}_file",
    )
    pasted = st.text_area(
        f"…or paste {label} text here",
        key=f"{key}_text",
        height=height,
        placeholder="Paste text here if you are not uploading a file.",
    )
    if uploaded is not None:
        try:
            text = extract_text(uploaded)
            st.caption(f"Read {len(text):,} characters from {uploaded.name}")
            return text
        except Exception as exc:
            st.error(f"Could not read {uploaded.name}: {exc}")
            return ""
    return pasted or ""


# ---------------------------------------------------------------------------
# Record store (session state + JSON export/import)
# ---------------------------------------------------------------------------

RECORD_TYPES = ["Coaching note", "Candidate profile", "JD analysis", "Outreach", "Fitment analysis"]


def init_records() -> None:
    if "records" not in st.session_state:
        st.session_state.records = []


def save_record(record_type: str, title: str, content: str) -> None:
    init_records()
    st.session_state.records.append(
        {
            "id": datetime.now().strftime("%Y%m%d-%H%M%S-") + str(len(st.session_state.records)),
            "type": record_type,
            "title": title.strip() or f"Untitled {record_type.lower()}",
            "content": content,
            "created": datetime.now().strftime("%Y-%m-%d %H:%M"),
        }
    )


def delete_record(record_id: str) -> None:
    init_records()
    st.session_state.records = [r for r in st.session_state.records if r["id"] != record_id]


def export_records() -> str:
    init_records()
    return json.dumps(st.session_state.records, ensure_ascii=False, indent=2)


def import_records(json_text: str) -> int:
    init_records()
    data = json.loads(json_text)
    if not isinstance(data, list):
        raise ValueError("Expected a JSON list of records.")
    existing = {r["id"] for r in st.session_state.records}
    added = 0
    for record in data:
        if isinstance(record, dict) and record.get("id") and record["id"] not in existing:
            st.session_state.records.append(record)
            added += 1
    return added


# ---------------------------------------------------------------------------
# Shared UI helpers
# ---------------------------------------------------------------------------

def result_block(result_key: str, record_type: str, default_title: str) -> None:
    """Show a generated result with download + save-to-records controls."""
    content = st.session_state.get(result_key)
    if not content:
        return
    st.markdown("---")
    st.markdown(content)
    st.download_button(
        "Download as text file",
        data=content,
        file_name=f"{record_type.lower().replace(' ', '_')}.txt",
        key=f"{result_key}_dl",
    )
    with st.expander("Save to records"):
        title = st.text_input("Record title", value=default_title, key=f"{result_key}_title")
        if st.button("Save", key=f"{result_key}_save"):
            save_record(record_type, title, content)
            st.success("Saved. View it in the Records page.")
