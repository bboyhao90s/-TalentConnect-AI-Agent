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
# Data store: candidates, jobs, generated outputs (session + JSON backup)
# ---------------------------------------------------------------------------

OUTPUT_TYPES = [
    "Candidate profile", "Coaching notes", "WhatsApp follow-up", "JD analysis",
    "Match report", "Outreach", "Fitment analysis", "Profile submission", "Interview prep",
]


def _now() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M")


def _new_id(prefix: str) -> str:
    return f"{prefix}-{datetime.now().strftime('%Y%m%d%H%M%S%f')}"


def init_store() -> None:
    st.session_state.setdefault("candidates", [])
    st.session_state.setdefault("jobs", [])
    st.session_state.setdefault("outputs", [])


def add_candidate(name: str, resume: str = "", salary: str = "", notice: str = "") -> dict:
    init_store()
    candidate = {
        "id": _new_id("cand"), "name": name.strip(), "resume": resume,
        "salary": salary, "notice": notice, "profile": "", "coaching_notes": "",
        "created": _now(),
    }
    st.session_state.candidates.append(candidate)
    return candidate


def get_candidate(cid: str) -> dict | None:
    init_store()
    return next((c for c in st.session_state.candidates if c["id"] == cid), None)


def add_job(title: str, employer: str = "", jd: str = "") -> dict:
    init_store()
    job = {
        "id": _new_id("job"), "title": title.strip(), "employer": employer.strip(),
        "jd": jd, "analysis": "", "created": _now(),
    }
    st.session_state.jobs.append(job)
    return job


def get_job(jid: str) -> dict | None:
    init_store()
    return next((j for j in st.session_state.jobs if j["id"] == jid), None)


def add_output(output_type: str, content: str, candidate_id: str | None = None,
               job_id: str | None = None, title: str = "") -> dict:
    """Auto-record every generated artefact, linked to candidate and/or job."""
    init_store()
    record = {
        "id": _new_id("out"), "type": output_type, "title": title or output_type,
        "content": content, "candidate_id": candidate_id, "job_id": job_id,
        "created": _now(),
    }
    st.session_state.outputs.append(record)
    return record


def outputs_for(candidate_id: str | None = None, job_id: str | None = None,
                output_type: str | None = None) -> list[dict]:
    init_store()
    results = st.session_state.outputs
    if candidate_id:
        results = [o for o in results if o.get("candidate_id") == candidate_id]
    if job_id:
        results = [o for o in results if o.get("job_id") == job_id]
    if output_type:
        results = [o for o in results if o.get("type") == output_type]
    return results


def delete_output(output_id: str) -> None:
    init_store()
    st.session_state.outputs = [o for o in st.session_state.outputs if o["id"] != output_id]


def delete_candidate(cid: str) -> None:
    init_store()
    st.session_state.candidates = [c for c in st.session_state.candidates if c["id"] != cid]
    st.session_state.outputs = [o for o in st.session_state.outputs if o.get("candidate_id") != cid]


def delete_job(jid: str) -> None:
    init_store()
    st.session_state.jobs = [j for j in st.session_state.jobs if j["id"] != jid]
    st.session_state.outputs = [o for o in st.session_state.outputs if o.get("job_id") != jid]


def export_store() -> str:
    init_store()
    return json.dumps(
        {
            "candidates": st.session_state.candidates,
            "jobs": st.session_state.jobs,
            "outputs": st.session_state.outputs,
        },
        ensure_ascii=False, indent=2,
    )


def import_store(json_text: str) -> dict:
    init_store()
    data = json.loads(json_text)
    counts = {}
    for key in ("candidates", "jobs", "outputs"):
        items = data.get(key, [])
        existing = {x["id"] for x in st.session_state[key]}
        added = [x for x in items if isinstance(x, dict) and x.get("id") and x["id"] not in existing]
        st.session_state[key].extend(added)
        counts[key] = len(added)
    return counts
