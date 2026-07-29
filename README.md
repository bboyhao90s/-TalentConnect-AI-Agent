# TalentConnect AI Agent

*Connecting Talent, Opportunities and Outcomes through AI.*

A connected talent-specialist pipeline — enter data once, use it everywhere:

1. **Candidate Profile** — add candidates (name, salary, notice, résumé), generate employer-ready profiles
2. **Coaching Notes & Follow-up** — transcript → notes in the official template + WhatsApp follow-up
3. **Jobs, Matching & Outreach** — save JDs, rank your candidate pool with a weighted scoring index, draft WSG/SSG outreach
4. **Fitment & Submission** — official fitment format (Experience / Transferable Skills / Technical Skills / Qualifications table + fit summary + upskilling note) and submission email
5. **Interview Prep** — role-specific prep guide grounded in the candidate's real background
6. **Dashboard** — candidate pipeline matrix, all records, backup export/import

Everything generated is auto-recorded and linked to its candidate and job.
Supports PDF, DOCX and TXT uploads, English and Chinese.
All templates live in `prompts.py` — edit that one file to change any output format.

## Deploy to Streamlit Community Cloud (public URL)

**Step 1 — Put these files on GitHub**

1. Sign in at github.com → click **+** (top right) → **New repository**
2. Name: `TalentConnect-AI-Agent` → set **Public** → **Create repository**
3. On the new repo page: **Add file → Upload files**
4. Drag in: `app.py`, `prompts.py`, `utils.py`, `requirements.txt`, `README.md`, `sample_transcript.txt`
   (Do **not** upload any file containing your API key.)
5. Click **Commit changes**

**Step 2 — Deploy on Streamlit**

1. Go to share.streamlit.io → sign in **with GitHub**
2. **Create app** → **Deploy a public app from GitHub**
3. Repository: `YOUR-USERNAME/TalentConnect-AI-Agent` · Branch: `main` · Main file path: `app.py`
4. Click **Deploy**

**Step 3 — Add your API key (the secure way)**

1. Once the app loads, click **Manage app** (bottom right) → **⋮ → Settings → Secrets**
2. Paste exactly:

```toml
OPENAI_API_KEY = "sk-your-real-key"
OPENAI_MODEL = "gpt-4o-mini"
```

3. **Save** → the app reboots → the sidebar should show "API key loaded".

Your public URL is `https://YOUR-APP-NAME.streamlit.app` — that's what you submit.

## Run locally (optional)

```bash
pip install -r requirements.txt
mkdir -p .streamlit
cp .streamlit/secrets.toml.example .streamlit/secrets.toml   # then edit in your key
streamlit run app.py
```

## Notes

- The API key never appears in the browser or on GitHub; it lives only in Streamlit's Secrets.
- Streamlit Cloud storage is temporary: use **Records → Export** to back up, **Import** to restore.
- `OPENAI_MODEL` can be changed in Secrets (e.g. `gpt-4.1-mini`) without touching the code.

## Candidate Database (pre-loaded pool)

The app ships with a bundled database of classified 0626-cohort candidates
(`candidate_db.py`). Each record is classified using the Skill Marriage method:
prior experience x new course skills -> unique value, recommended roles and
seniority. Only full name and email are stored as identifiers (PDPA-safe).

- **Browse:** Page 1 -> "Candidate Database" tab. Filter by Talent Specialist,
  Course and Cohort, or search by name / skill / role.
- **Use a candidate:** click "Add to my candidates" to copy them into your
  working set — they then flow through coaching, matching, fitment, interview
  prep and outreach like any added candidate.
- **Match a JD against the pool:** Page 3 -> "Match my candidates" tab ->
  choose "Full candidate database" or "Database (filtered)" as the match scope,
  paste/select a JD, and run matching to get a ranked shortlist.

To grow the database monthly, append new classified records to `CANDIDATE_DB`
in `candidate_db.py` (a future upload workflow can automate this).

**Privacy note:** the database holds real candidate names. Do not deploy it on a
public URL without access control (a login/password gate). Keep to sample data
on any public demo.

## Team login (password gate)

The app can be protected by a shared team password so only people with the
password can open it — required before putting real candidate names online.

**To turn it on:** in Streamlit Cloud → Manage app → Settings → Secrets, add:

    APP_PASSWORD = "your-strong-team-password"

Then reboot. Everyone opening the app must enter this password once per session.
A "Log out" button appears in the sidebar.

**If APP_PASSWORD is not set, the app stays open** (no login) and shows a warning
reminding you to set one before going live with real data. This shared-password
gate is proportionate protection for a team tool; it is not per-user accounts.

