"""
TalentConnect AI Agent
Connecting Talent, Opportunities and Outcomes through AI.

Connected pipeline: data entered once flows to every module.
1 Candidate Profile · 2 Coaching Notes & Follow-up · 3 Jobs, Matching & Outreach
4 Fitment & Submission · 5 Interview Prep · 6 Dashboard
"""

import streamlit as st

import prompts
import utils

st.set_page_config(page_title="TalentConnect AI Agent", page_icon="🤝", layout="wide")
utils.init_store()

NEW = "➕ Add new…"


# ---------------------------------------------------------------------------
# Shared helpers
# ---------------------------------------------------------------------------

def ai_generate(system_prompt: str, user_content: str) -> str | None:
    try:
        with st.spinner("TalentConnect AI is working…"):
            return utils.run_ai(system_prompt, user_content)
    except RuntimeError as exc:
        st.error(str(exc))
        return None


def candidate_selector(key: str, allow_new: bool = True):
    """Dropdown of saved candidates. Returns a candidate dict or None."""
    candidates = st.session_state.candidates
    options = ([NEW] if allow_new else []) + [c["id"] for c in candidates]
    if not options:
        st.info("No candidates yet — add one on page 1 · Candidate Profile.")
        return None
    labels = {c["id"]: f"{c['name']}  ·  added {c['created']}" for c in candidates}
    choice = st.selectbox(
        "Candidate", options, key=f"{key}_cand",
        format_func=lambda x: labels.get(x, x),
    )
    return None if choice == NEW else utils.get_candidate(choice)


def job_selector(key: str, allow_new: bool = True):
    """Dropdown of saved jobs. Returns a job dict or None."""
    jobs = st.session_state.jobs
    options = ([NEW] if allow_new else []) + [j["id"] for j in jobs]
    if not options:
        st.info("No jobs yet — add one on page 3 · Jobs, Matching & Outreach.")
        return None
    labels = {j["id"]: f"{j['title']} — {j['employer'] or 'employer N/A'}" for j in jobs}
    choice = st.selectbox(
        "Job / role", options, key=f"{key}_job",
        format_func=lambda x: labels.get(x, x),
    )
    return None if choice == NEW else utils.get_job(choice)


def show_output(content: str, filename: str, key: str) -> None:
    st.markdown("---")
    st.markdown(content)
    base = filename.rsplit(".", 1)[0]
    dcol1, dcol2 = st.columns(2)
    with dcol1:
        st.download_button(
            "⬇️ Download Word (.docx)",
            data=utils.markdown_to_docx_bytes(content),
            file_name=f"{base}.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            key=f"{key}_docx",
        )
    with dcol2:
        st.download_button("Download .txt", data=content,
                           file_name=filename, key=f"{key}_dl")


def candidate_context(candidate: dict) -> str:
    """Best available description of a candidate for prompting."""
    parts = [f"Candidate name: {candidate['name']}"]
    if candidate.get("salary"):
        parts.append(f"Expected salary: {candidate['salary']}")
    if candidate.get("notice"):
        parts.append(f"Notice period: {candidate['notice']}")
    if candidate.get("profile"):
        parts.append(f"\n=== CANDIDATE PROFILE ===\n{candidate['profile']}")
    if candidate.get("resume"):
        parts.append(f"\n=== RÉSUMÉ ===\n{candidate['resume']}")
    if candidate.get("coaching_notes"):
        parts.append(f"\n=== COACHING NOTES ===\n{candidate['coaching_notes']}")
    return "\n".join(parts)


# ---------------------------------------------------------------------------
# Sidebar
# ---------------------------------------------------------------------------

with st.sidebar:
    st.title("🤝 TalentConnect AI Agent")
    st.caption("Connecting Talent, Opportunities and Outcomes through AI.")

    page = st.radio(
        "Workflow",
        [
            "1 · Candidate Profile",
            "2 · Coaching Notes & Follow-up",
            "3 · Jobs, Matching & Outreach",
            "4 · Fitment & Submission",
            "5 · Interview Prep",
            "6 · Dashboard",
        ],
    )

    st.markdown("---")
    if utils.get_api_key():
        st.success(f"API key loaded · model: {utils.get_model()}")
    else:
        st.error("No API key configured. Add OPENAI_API_KEY in "
                 "Manage app → Settings → Secrets, then reboot the app.")
    st.caption(
        f"📇 {len(st.session_state.candidates)} candidates · "
        f"💼 {len(st.session_state.jobs)} jobs · "
        f"🗂️ {len(st.session_state.outputs)} records"
    )
    st.caption("Data lives in this session — export a backup on the Dashboard.")


# ===========================================================================
# 1 · CANDIDATE PROFILE
# ===========================================================================

if page.startswith("1"):
    st.header("1 · Candidate Profile")
    st.write("Add a candidate once — every other module can then select them "
             "from a dropdown. Generate their employer-ready profile here.")

    selected = candidate_selector("p1")

    if selected is None:
        st.subheader("Add a new candidate")
        name = st.text_input("Candidate name *")
        col1, col2 = st.columns(2)
        with col1:
            salary = st.text_input("Expected salary", placeholder="e.g. $3,000 - $3,500")
        with col2:
            notice = st.text_input("Notice period", placeholder="e.g. Immediate / 1 month")
        resume = utils.read_input("the résumé / CV", "p1_resume")
        if st.button("Save candidate", type="primary"):
            if not name.strip():
                st.warning("Please enter the candidate's name.")
            else:
                utils.add_candidate(name, resume, salary, notice)
                st.success(f"Saved {name}. Select them in the dropdown above to continue.")
                st.rerun()
    else:
        st.subheader(selected["name"])
        col1, col2 = st.columns(2)
        col1.metric("Expected salary", selected.get("salary") or "N/A")
        col2.metric("Notice period", selected.get("notice") or "N/A")

        with st.expander("View / update résumé", expanded=not selected.get("resume")):
            new_resume = utils.read_input("an updated résumé / CV", "p1_update")
            if new_resume.strip() and st.button("Replace stored résumé"):
                selected["resume"] = new_resume
                st.success("Résumé updated.")
            if selected.get("resume"):
                st.text_area("Stored résumé", selected["resume"], height=180, disabled=True)

        if selected.get("coaching_notes"):
            st.caption("✅ Coaching notes on file — they will enrich the profile.")

        if st.button("Generate candidate profile", type="primary"):
            source = candidate_context(selected)
            if not selected.get("resume") and not selected.get("coaching_notes"):
                st.warning("Add a résumé (above) or coaching notes (page 2) first.")
            else:
                result = ai_generate(prompts.CANDIDATE_PROFILE, source)
                if result:
                    selected["profile"] = result
                    utils.add_output("Candidate profile", result, candidate_id=selected["id"],
                                     title=f"Profile — {selected['name']}")
        if selected.get("profile"):
            show_output(selected["profile"], f"profile_{selected['name']}.txt", "p1_out")


# ===========================================================================
# 2 · COACHING NOTES & FOLLOW-UP
# ===========================================================================

elif page.startswith("2"):
    st.header("2 · Coaching Notes & WhatsApp Follow-up")
    st.write("Paste a session transcript. Notes are saved to the candidate's "
             "record and reused by the profile and fitment modules.")

    selected = candidate_selector("p2")
    if selected is None and st.session_state.candidates:
        st.caption("Or add the candidate quickly by name:")
    if selected is None:
        quick_name = st.text_input("New candidate name *", key="p2_name")

    transcript = utils.read_input("the coaching transcript", "p2_tr", height=240)

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Coaching notes")
        if st.button("Generate coaching notes", type="primary"):
            if not transcript.strip():
                st.warning("Please provide the transcript first.")
            elif selected is None and not (st.session_state.get("p2_name") or "").strip():
                st.warning("Select a candidate or enter a name first.")
            else:
                result = ai_generate(prompts.COACHING_NOTES, transcript)
                if result:
                    if selected is None:
                        selected = utils.add_candidate(st.session_state["p2_name"])
                    selected["coaching_notes"] = result
                    utils.add_output("Coaching notes", result, candidate_id=selected["id"],
                                     title=f"Coaching notes — {selected['name']}")
                    st.session_state["p2_notes_out"] = result
        if st.session_state.get("p2_notes_out"):
            show_output(st.session_state["p2_notes_out"], "coaching_notes.txt", "p2_n")

    with col2:
        st.subheader("WhatsApp follow-up")
        if st.button("Generate WhatsApp follow-up", type="primary"):
            if not transcript.strip():
                st.warning("Please provide the transcript first.")
            else:
                result = ai_generate(prompts.WHATSAPP_FOLLOWUP, transcript)
                if result:
                    utils.add_output(
                        "WhatsApp follow-up", result,
                        candidate_id=selected["id"] if selected else None,
                        title=f"WhatsApp — {selected['name'] if selected else 'candidate'}",
                    )
                    st.session_state["p2_wa_out"] = result
        if st.session_state.get("p2_wa_out"):
            show_output(st.session_state["p2_wa_out"], "whatsapp_followup.txt", "p2_w")


# ===========================================================================
# 3 · JOBS, MATCHING & OUTREACH
# ===========================================================================

elif page.startswith("3"):
    st.header("3 · Jobs, Candidate Matching & Outreach")
    st.write("Save a job once, check which of your candidates fit it, then "
             "draft outreach attaching the best profiles.")

    job = job_selector("p3")

    if job is None:
        st.subheader("Add a new job")
        col1, col2 = st.columns(2)
        with col1:
            title = st.text_input("Job title *", placeholder="e.g. IT Support Engineer")
        with col2:
            employer = st.text_input("Employer / hiring manager")
        jd = utils.read_input("the job description", "p3_jd", height=220)
        if st.button("Save job", type="primary"):
            if not title.strip() or not jd.strip():
                st.warning("Please provide at least the job title and JD.")
            else:
                utils.add_job(title, employer, jd)
                st.success(f"Saved {title}. Select it in the dropdown above to continue.")
                st.rerun()
    else:
        st.subheader(f"{job['title']} — {job['employer'] or 'employer N/A'}")
        tab_match, tab_outreach, tab_jd = st.tabs(
            ["🎯 Match my candidates", "✉️ Outreach", "📋 JD analysis"])

        with tab_match:
            pool = [c for c in st.session_state.candidates
                    if c.get("profile") or c.get("resume") or c.get("coaching_notes")]
            st.caption(f"{len(pool)} candidate(s) with enough data to match.")
            if st.button("Run candidate matching", type="primary",
                         disabled=not pool):
                pool_text = "\n\n---\n\n".join(
                    candidate_context(c)[:3000] for c in pool)
                content = (f"=== JOB DESCRIPTION: {job['title']} ===\n{job['jd']}"
                           f"\n\n=== CANDIDATE POOL ===\n\n{pool_text}")
                result = ai_generate(prompts.CANDIDATE_MATCHING, content)
                if result:
                    utils.add_output("Match report", result, job_id=job["id"],
                                     title=f"Match report — {job['title']}")
                    st.session_state["p3_match_out"] = result
            if st.session_state.get("p3_match_out"):
                show_output(st.session_state["p3_match_out"], "match_report.txt", "p3_m")

        with tab_outreach:
            pool_labels = {c["id"]: c["name"] for c in st.session_state.candidates}
            chosen = st.multiselect(
                "Attach candidate profiles (leave empty for exploratory outreach)",
                list(pool_labels),
                format_func=lambda x: pool_labels.get(x, x),
            )
            if st.button("Draft employer outreach", type="primary"):
                content = f"=== JOB DESCRIPTION: {job['title']} ===\n{job['jd']}"
                if job["employer"]:
                    content += f"\n\n=== EMPLOYER CONTACT ===\n{job['employer']}"
                if chosen:
                    profiles = "\n\n---\n\n".join(
                        candidate_context(utils.get_candidate(cid))[:2500] for cid in chosen)
                    content += f"\n\n=== CANDIDATE PROFILES ===\n{profiles}"
                result = ai_generate(prompts.EMPLOYER_OUTREACH, content)
                if result:
                    utils.add_output("Outreach", result, job_id=job["id"],
                                     title=f"Outreach — {job['title']}")
                    st.session_state["p3_out_out"] = result
            if st.session_state.get("p3_out_out"):
                show_output(st.session_state["p3_out_out"], "outreach.txt", "p3_o")

        with tab_jd:
            if st.button("Analyse this JD", type="primary"):
                result = ai_generate(prompts.JD_ANALYSIS, job["jd"])
                if result:
                    job["analysis"] = result
                    utils.add_output("JD analysis", result, job_id=job["id"],
                                     title=f"JD analysis — {job['title']}")
            if job.get("analysis"):
                show_output(job["analysis"], "jd_analysis.txt", "p3_j")


# ===========================================================================
# 4 · FITMENT & SUBMISSION
# ===========================================================================

elif page.startswith("4"):
    st.header("4 · Fitment Analysis & Profile Submission")
    st.write("Profile submission: the formal shortlist email to the client. "
             "Fitment analysis: the 3-column JD-to-skills mapping with "
             "first-person pitch lines, prepared before the interview.")

    col1, col2 = st.columns(2)
    with col1:
        candidate = candidate_selector("p4", allow_new=False)
    with col2:
        job = job_selector("p4", allow_new=False)

    course = st.text_input(
        "Upskilling course / domain",
        placeholder="e.g. SCTP Professional Diploma in Data Science",
    )

    if candidate and job:
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Fitment analysis")
            if st.button("Generate fitment analysis", type="primary"):
                content = (
                    f"Job Title: {job['title']}\n"
                    f"Upskilling course/domain: {course or 'N/A'}\n\n"
                    f"=== JOB DESCRIPTION ===\n{job['jd']}\n\n"
                    f"=== CANDIDATE EXPERIENCE ===\n{candidate_context(candidate)}"
                )
                result = ai_generate(prompts.FITMENT_ANALYSIS, content)
                if result:
                    utils.add_output("Fitment analysis", result,
                                     candidate_id=candidate["id"], job_id=job["id"],
                                     title=f"Fitment — {candidate['name']} × {job['title']}")
                    st.session_state["p4_fit_out"] = result
            if st.session_state.get("p4_fit_out"):
                show_output(st.session_state["p4_fit_out"], "fitment_analysis.txt", "p4_f")

        with col2:
            st.subheader("Profile submission")
            fitments = utils.outputs_for(candidate["id"], job["id"], "Fitment analysis")
            if not fitments:
                st.caption("Tip: if a fitment analysis exists for this pair, the email will use it as evidence.")
            if st.button("Generate profile submission", type="primary"):
                content = (
                    f"Job Title: {job['title']} at {job['employer'] or 'the employer'}\n\n"
                    f"=== CANDIDATE ===\n{candidate_context(candidate)[:3000]}"
                )
                if fitments:
                    content += f"\n\n=== FITMENT ANALYSIS ===\n{fitments[-1]['content']}"
                result = ai_generate(prompts.SUBMISSION_EMAIL, content)
                if result:
                    utils.add_output("Profile submission", result,
                                     candidate_id=candidate["id"], job_id=job["id"],
                                     title=f"Profile submission — {candidate['name']} × {job['title']}")
                    st.session_state["p4_sub_out"] = result
            if st.session_state.get("p4_sub_out"):
                show_output(st.session_state["p4_sub_out"], "profile_submission.txt", "p4_s")


# ===========================================================================
# 5 · INTERVIEW PREP
# ===========================================================================

elif page.startswith("5"):
    st.header("5 · Interview Preparation")
    st.write("The pre-interview pack: the Interview Preparation Guide and the "
             "Fitment Analysis (3-column JD-to-skills mapping with pitch "
             "lines). Generate both, download as Word, send to the candidate.")

    col1, col2 = st.columns(2)
    with col1:
        candidate = candidate_selector("p5", allow_new=False)
    with col2:
        job = job_selector("p5", allow_new=False)

    if candidate and job:
        base_content = (
            f"Job Title: {job['title']}\n"
            f"Company: {job['employer'] or 'N/A'}\n\n"
            f"=== JOB DESCRIPTION ===\n{job['jd']}\n\n"
            f"=== CANDIDATE BACKGROUND ===\n{candidate_context(candidate)}"
        )
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("📘 Interview Preparation Guide")
            if st.button("Generate prep guide", type="primary"):
                result = ai_generate(prompts.INTERVIEW_PREP, base_content)
                if result:
                    utils.add_output("Interview prep", result,
                                     candidate_id=candidate["id"], job_id=job["id"],
                                     title=f"Interview prep — {candidate['name']} × {job['title']}")
                    st.session_state["p5_out"] = result
            if st.session_state.get("p5_out"):
                show_output(st.session_state["p5_out"],
                            f"Interview_Preparation_Guide_{candidate['name']}.txt", "p5_o")
        with col2:
            st.subheader("📊 Fitment Analysis")
            if st.button("Generate fitment analysis", type="primary", key="p5_fit_btn"):
                result = ai_generate(prompts.FITMENT_ANALYSIS, base_content)
                if result:
                    utils.add_output("Fitment analysis", result,
                                     candidate_id=candidate["id"], job_id=job["id"],
                                     title=f"Fitment — {candidate['name']} × {job['title']}")
                    st.session_state["p5_fit_out"] = result
            if st.session_state.get("p5_fit_out"):
                show_output(st.session_state["p5_fit_out"],
                            f"Fitment_Analysis_{candidate['name']}.txt", "p5_f")


# ===========================================================================
# 6 · DASHBOARD
# ===========================================================================

else:
    st.header("6 · Dashboard")

    col1, col2, col3 = st.columns(3)
    col1.metric("Candidates", len(st.session_state.candidates))
    col2.metric("Jobs", len(st.session_state.jobs))
    col3.metric("Generated records", len(st.session_state.outputs))

    # Pipeline matrix: which artefacts exist per candidate
    st.subheader("Candidate pipeline")
    if not st.session_state.candidates:
        st.info("No candidates yet. Start on page 1 · Candidate Profile.")
    else:
        stages = ["Coaching notes", "Candidate profile", "Fitment analysis",
                  "Profile submission", "Interview prep"]
        rows = []
        for c in st.session_state.candidates:
            row = {"Candidate": c["name"],
                   "Salary": c.get("salary") or "—",
                   "Notice": c.get("notice") or "—"}
            for s in stages:
                done = bool(utils.outputs_for(candidate_id=c["id"], output_type=s))
                if s == "Coaching notes":
                    done = done or bool(c.get("coaching_notes"))
                if s == "Candidate profile":
                    done = done or bool(c.get("profile"))
                row[s] = "✅" if done else "—"
            rows.append(row)
        st.dataframe(rows, use_container_width=True)

    st.subheader("Jobs")
    if st.session_state.jobs:
        st.dataframe(
            [{"Job title": j["title"], "Employer": j["employer"] or "—",
              "Added": j["created"],
              "Match report": "✅" if utils.outputs_for(job_id=j["id"], output_type="Match report") else "—",
              "Outreach": "✅" if utils.outputs_for(job_id=j["id"], output_type="Outreach") else "—"}
             for j in st.session_state.jobs],
            use_container_width=True,
        )
    else:
        st.info("No jobs yet. Add one on page 3.")

    st.subheader("All generated records")
    if st.session_state.outputs:
        fcol1, fcol2 = st.columns(2)
        with fcol1:
            module_filter = st.selectbox(
                "1️⃣ Filter by module",
                ["All modules"] + utils.OUTPUT_TYPES,
            )
        with fcol2:
            cand_ids = [c["id"] for c in st.session_state.candidates]
            cand_labels = {c["id"]: c["name"] for c in st.session_state.candidates}
            candidate_filter = st.selectbox(
                "2️⃣ Filter by candidate",
                ["All candidates"] + cand_ids + ["(Not linked to a candidate)"],
                format_func=lambda x: cand_labels.get(x, x),
            )

        shown = st.session_state.outputs
        if module_filter != "All modules":
            shown = [o for o in shown if o["type"] == module_filter]
        if candidate_filter == "(Not linked to a candidate)":
            shown = [o for o in shown if not o.get("candidate_id")]
        elif candidate_filter != "All candidates":
            shown = [o for o in shown if o.get("candidate_id") == candidate_filter]

        st.caption(f"Showing {len(shown)} of {len(st.session_state.outputs)} record(s)")
        if not shown:
            st.info("No records match these filters.")
        job_labels = {j["id"]: j["title"] for j in st.session_state.jobs}
        for record in reversed(shown):
            who = cand_labels.get(record.get("candidate_id"), "")
            role = job_labels.get(record.get("job_id"), "")
            tag = " · ".join(x for x in (who, role) if x)
            header = f"{record['type']} · {record['title']} · {record['created']}"
            if tag:
                header += f"  ({tag})"
            with st.expander(header):
                st.markdown(record["content"])
                bcol1, bcol2 = st.columns(2)
                with bcol1:
                    st.download_button(
                        "⬇️ Word (.docx)",
                        data=utils.markdown_to_docx_bytes(record["content"]),
                        file_name=f"{record['type'].replace(' ', '_')}.docx",
                        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                        key=f"dl_{record['id']}",
                    )
                with bcol2:
                    if st.button("🗑️ Delete this record", key=f"del_{record['id']}"):
                        utils.delete_output(record["id"])
                        st.rerun()
    else:
        st.info("Nothing generated yet.")

    st.subheader("Backup & restore")
    st.caption("Streamlit Cloud storage is temporary — export before closing, "
               "import to continue in a future session.")
    col1, col2 = st.columns(2)
    with col1:
        st.download_button("⬇️ Export everything (JSON backup)",
                           data=utils.export_store(),
                           file_name="talentconnect_backup.json",
                           mime="application/json")
    with col2:
        backup = st.file_uploader("Import a backup file", type=["json"], key="imp")
        if backup is not None and st.button("Import"):
            try:
                counts = utils.import_store(backup.read().decode("utf-8"))
                st.success(f"Imported: {counts['candidates']} candidates, "
                           f"{counts['jobs']} jobs, {counts['outputs']} records.")
                st.rerun()
            except Exception as exc:
                st.error(f"Could not import: {exc}")

    with st.expander("⚠️ Delete a candidate or job (removes their linked records)"):
        col1, col2 = st.columns(2)
        with col1:
            if st.session_state.candidates:
                dc_labels = {c["id"]: c["name"] for c in st.session_state.candidates}
                cid = st.selectbox("Candidate to delete", list(dc_labels),
                                   format_func=lambda x: dc_labels.get(x, x))
                if st.button("Delete candidate"):
                    utils.delete_candidate(cid)
                    st.rerun()
        with col2:
            if st.session_state.jobs:
                dj_labels = {j["id"]: j["title"] for j in st.session_state.jobs}
                jid = st.selectbox("Job to delete", list(dj_labels),
                                   format_func=lambda x: dj_labels.get(x, x))
                if st.button("Delete job"):
                    utils.delete_job(jid)
                    st.rerun()
