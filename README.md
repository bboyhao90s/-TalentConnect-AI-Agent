# TalentConnect AI Agent

*Connecting Talent, Opportunities and Outcomes through AI.*

One Streamlit app covering the full talent-specialist journey:

1. Coaching transcript → coaching notes + WhatsApp follow-up
2. Résumé + coaching notes → candidate profile & employer positioning
3. Employer JD → hiring analysis + outreach (with or without profiles)
4. Candidate + JD → fitment score, gaps, recommendation, interview prep, submission email
5. Saved records with export/import backup

Supports PDF, DOCX and TXT uploads, in English and Chinese.

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
