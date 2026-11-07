# ⚡ Vibe Coder

High-end phone-style Streamlit app that cleanses and triages your prompts using free Gemini 1.5 Flash.

## Features

- **Multi-skin engine**: Cyberpunk Neon · Minimalist Dark · Cyber-Y2K Retro
- **Live free Gemini integration** (Google AI Studio key)
- **Smart complexity pipeline**:
  - Simple prompts → answered directly inside the app
  - Deep / architectural prompts → beautifully optimized prompt ready to copy into your paid models
- **Best-mate personality**: encouraging, collaborative, never robotic

## Quick Start

```bash
# 1. Clone / enter the folder
cd vibe-coder-app

# 2. Create virtualenv (recommended)
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 3. Install
pip install -r requirements.txt

# 4. Get a free Gemini API key
#    → https://aistudio.google.com/apikey

# 5. Run
streamlit run app.py
```

Optional: set the key as an environment variable so you don’t have to paste it every time:

```bash
export GEMINI_API_KEY="AIza..."
streamlit run app.py
```

## Deploy

Works great on:
- Streamlit Community Cloud
- Hugging Face Spaces
- Railway / Render / Fly.io

Just set the `GEMINI_API_KEY` secret in the platform.

---

Built for vibe coders.
