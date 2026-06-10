"""
TalentConnect AI Agent
Connecting Talent, Opportunities and Outcomes through AI.

One Streamlit app covering the full talent-specialist journey:
transcript → coaching notes → candidate profile → JD analysis & outreach
→ fitment analysis & interview prep → saved records.
"""

import streamlit as st

import prompts
import utils

st.set_page_config(
    page_title="TalentConnect AI Agent",
    page_icon="🤝",
    layout="wide",
)

utils.init_records()

# ---------------------------------------------------------------------------
# Sidebar
# ---------------------------------------------------------------------------

with st.sidebar:
    st.title("🤝 TalentConnect AI Agent")
    st.caption("Connecting Talent, Opportunities and Outcomes through AI.")

    page = st.radio(
        "Workflow",
        [
            "1 · Coaching Notes & Follow-up",
            "2 · Candidate Profile",
            "3 · JD Analysis & Outreach",
            "4 · Fitment & Interview Prep",
            "5 · Records",
        ],
    )

    st.markdown("---")
    if utils.get_api_key():
        st.success(f"API key loaded · model: {utils.get_model()}")
    else:
        st.error(
            "No API key configured. Add OPENAI_API_KEY in "
            "Manage app → Settings → Secrets, then reboot the app."
        )
    st.caption(f"Saved records this session: {len(st.session_state.records)}")
    st.caption(
        "Records live in the current session. Use the Records page to "
        "export a backup file before closing the app."
    )


def generate(button_label: str, system_prompt: str, user_content: str,
             result_key: str, missing_msg: str) -> None:
    """Shared generate-button behaviour for every page."""
    if st.button(button_label, type="primary", key=f"{result_key}_btn"):
        if not user_content.strip():
            st.warning(missing_msg)
            return
        try:
            with st.spinner("TalentConnect AI is working…"):
                st.session_state[result_key] = utils.run_ai(system_prompt, user_content)
        except RuntimeError as exc:
            st.error(str(exc))


# ---------------------------------------------------------------------------
# 1 · Coaching Notes & Follow-up
# ---------------------------------------------------------------------------

if page.startswith("1"):
    st.header("Coaching transcript → notes & WhatsApp follow-up")
    st.write(
        "Upload or paste a coaching session transcript. Generate structured "
        "coaching notes, then a WhatsApp follow-up in your style."
    )

    transcript = utils.read_input("the coaching transcript", "transcript", height=260)
    candidate_name = st.text_input("Candidate name (optional, used in record titles)")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Coaching notes")
        generate(
            "Generate coaching notes",
            prompts.COACHING_NOTES,
            transcript,
            "result_notes",
            "Please upload or paste a transcript first.",
        )
        utils.result_block(
            "result_notes", "Coaching note",
            f"Coaching notes — {candidate_name or 'candidate'}",
        )

    with col2:
        st.subheader("WhatsApp follow-up")
        generate(
            "Generate WhatsApp follow-up",
            prompts.WHATSAPP_FOLLOWUP,
            transcript,
            "result_whatsapp",
            "Please upload or paste a transcript first.",
        )
        utils.result_block(
            "result_whatsapp", "Outreach",
            f"WhatsApp follow-up — {candidate_name or 'candidate'}",
        )

# ---------------------------------------------------------------------------
# 2 · Candidate Profile
# ---------------------------------------------------------------------------

elif page.startswith("2"):
    st.header("Résumé + coaching notes → candidate profile")
    st.write(
        "Combine the candidate's résumé with approved coaching notes to produce "
        "an employer-ready profile and honest internal positioning notes."
    )

    resume = utils.read_input("the résumé / CV", "resume")
    notes = utils.read_input("approved coaching notes (optional)", "profile_notes", height=160)
    candidate_name = st.text_input("Candidate name (optional)")

    combined = ""
    if resume.strip():
        combined = f"=== RÉSUMÉ ===\n{resume}"
        if notes.strip():
            combined += f"\n\n=== APPROVED COACHING NOTES ===\n{notes}"

    generate(
        "Generate candidate profile",
        prompts.CANDIDATE_PROFILE,
        combined,
        "result_profile",
        "Please provide the résumé first (coaching notes are optional).",
    )
    utils.result_block(
        "result_profile", "Candidate profile",
        f"Profile — {candidate_name or 'candidate'}",
    )

# ---------------------------------------------------------------------------
# 3 · JD Analysis & Outreach
# ---------------------------------------------------------------------------

elif page.startswith("3"):
    st.header("Employer JD → hiring analysis & outreach")
    st.write(
        "Analyse a job description, then draft employer outreach — with or "
        "without candidate profiles attached."
    )

    jd = utils.read_input("the job description", "jd", height=240)
    employer = st.text_input("Employer / hiring manager name (optional)")

    tab_analysis, tab_outreach = st.tabs(["JD analysis", "Employer outreach"])

    with tab_analysis:
        generate(
            "Analyse this JD",
            prompts.JD_ANALYSIS,
            jd,
            "result_jd",
            "Please upload or paste the job description first.",
        )
        utils.result_block(
            "result_jd", "JD analysis",
            f"JD analysis — {employer or 'employer'}",
        )

    with tab_outreach:
        profiles = st.text_area(
            "Candidate profile summaries to attach (optional — leave blank for "
            "exploratory outreach without profiles)",
            height=160,
            placeholder="Paste one or more profile summaries from page 2, or leave blank.",
        )
        outreach_input = ""
        if jd.strip():
            outreach_input = f"=== JOB DESCRIPTION ===\n{jd}"
            if profiles.strip():
                outreach_input += f"\n\n=== CANDIDATE PROFILES ===\n{profiles}"
            if employer.strip():
                outreach_input += f"\n\n=== EMPLOYER CONTACT ===\n{employer}"

        generate(
            "Draft employer outreach",
            prompts.EMPLOYER_OUTREACH,
            outreach_input,
            "result_outreach",
            "Please provide the job description first.",
        )
        utils.result_block(
            "result_outreach", "Outreach",
            f"Outreach — {employer or 'employer'}",
        )

# ---------------------------------------------------------------------------
# 4 · Fitment & Interview Prep
# ---------------------------------------------------------------------------

elif page.startswith("4"):
    st.header("Candidate + JD → fitment, emails & interview prep")
    st.write(
        "Run a candid fitment analysis between one candidate and one role. "
        "Produces score, gaps, recommendation, interview prep, submission "
        "email and candidate WhatsApp update."
    )

    col1, col2 = st.columns(2)
    with col1:
        candidate_doc = utils.read_input("the candidate résumé / profile", "fit_candidate")
    with col2:
        jd_doc = utils.read_input("the job description", "fit_jd")

    extras = st.text_input(
        "Known constraints (optional): expected salary, notice period, location…",
        placeholder="e.g. expects S$4,500, 1 month notice, prefers hybrid",
    )
    candidate_name = st.text_input("Candidate name (optional)", key="fit_name")

    fit_input = ""
    if candidate_doc.strip() and jd_doc.strip():
        fit_input = (
            f"=== CANDIDATE ===\n{candidate_doc}\n\n"
            f"=== JOB DESCRIPTION ===\n{jd_doc}"
        )
        if extras.strip():
            fit_input += f"\n\n=== KNOWN CONSTRAINTS ===\n{extras}"

    generate(
        "Run fitment analysis",
        prompts.FITMENT_ANALYSIS,
        fit_input,
        "result_fitment",
        "Please provide both the candidate document and the job description.",
    )
    utils.result_block(
        "result_fitment", "Fitment analysis",
        f"Fitment — {candidate_name or 'candidate'}",
    )

# ---------------------------------------------------------------------------
# 5 · Records
# ---------------------------------------------------------------------------

else:
    st.header("Saved records")
    st.write(
        "Records from this session. Streamlit Cloud storage is temporary, so "
        "export a backup file to keep records permanently, and import it in a "
        "future session to continue."
    )

    col1, col2 = st.columns(2)
    with col1:
        st.download_button(
            "⬇️ Export all records (JSON backup)",
            data=utils.export_records(),
            file_name="talentconnect_records.json",
            mime="application/json",
            disabled=not st.session_state.records,
        )
    with col2:
        backup = st.file_uploader("Import a backup file", type=["json"], key="import_file")
        if backup is not None and st.button("Import records"):
            try:
                added = utils.import_records(backup.read().decode("utf-8"))
                st.success(f"Imported {added} record(s).")
            except Exception as exc:
                st.error(f"Could not import: {exc}")

    st.markdown("---")

    if not st.session_state.records:
        st.info("No records yet. Generate something on pages 1-4 and choose 'Save to records'.")
    else:
        type_filter = st.multiselect(
            "Filter by type", utils.RECORD_TYPES, default=utils.RECORD_TYPES
        )
        shown = [r for r in st.session_state.records if r["type"] in type_filter]
        st.caption(f"Showing {len(shown)} of {len(st.session_state.records)} record(s)")

        for record in reversed(shown):
            with st.expander(f"{record['type']} · {record['title']} · {record['created']}"):
                st.markdown(record["content"])
                if st.button("🗑️ Delete this record", key=f"del_{record['id']}"):
                    utils.delete_record(record["id"])
                    st.rerun()
