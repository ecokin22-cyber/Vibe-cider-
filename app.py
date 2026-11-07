"""
Vibe Coder • Prompt Cleanser & Triage Engine
High-end Streamlit phone-app wrapper
"""

import streamlit as st
import os
import json
from typing import Optional
from google import genai
from google.genai import types

st.set_page_config(
    page_title="Vibe Coder",
    page_icon="⚡",
    layout="centered",
    initial_sidebar_state="collapsed",
)

THEMES = {
    "Cyberpunk Neon": {
        "bg": "#0a0a12",
        "surface": "rgba(20, 12, 40, 0.75)",
        "primary": "#00f0ff",
        "secondary": "#ff00aa",
        "accent": "#b000ff",
        "text": "#e0f7ff",
        "muted": "#8899aa",
        "border": "rgba(0, 240, 255, 0.35)",
        "glow": "0 0 20px rgba(0, 240, 255, 0.4)",
        "font": "'Orbitron', 'Segoe UI', sans-serif",
        "radius": "16px",
    },
    "Minimalist Dark": {
        "bg": "#0d0d0d",
        "surface": "rgba(28, 28, 28, 0.85)",
        "primary": "#a0a0a0",
        "secondary": "#ffffff",
        "accent": "#666666",
        "text": "#f0f0f0",
        "muted": "#888888",
        "border": "rgba(255, 255, 255, 0.12)",
        "glow": "none",
        "font": "'Inter', 'SF Pro Display', system-ui, sans-serif",
        "radius": "12px",
    },
    "Cyber-Y2K Retro": {
        "bg": "#1a0a2e",
        "surface": "rgba(40, 10, 60, 0.8)",
        "primary": "#ff6ec7",
        "secondary": "#00ffcc",
        "accent": "#ffcc00",
        "text": "#fff0f5",
        "muted": "#c9a0dc",
        "border": "rgba(255, 110, 199, 0.45)",
        "glow": "0 0 25px rgba(255, 110, 199, 0.5)",
        "font": "'Press Start 2P', 'Courier New', monospace",
        "radius": "8px",
    },
}

def inject_theme_css(theme_name: str):
    t = THEMES[theme_name]
    css = f"""
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;600;700&family=Inter:wght@400;500;600&family=Press+Start+2P&display=swap');

    .stApp {{
        background: {t['bg']} !important;
        color: {t['text']} !important;
        font-family: {t['font']} !important;
    }}

    #MainMenu, footer, header {{visibility: hidden;}}
    .stDeployButton {{display: none;}}

    .main .block-container {{
        max-width: 430px !important;
        padding: 1.2rem 1rem 3rem 1rem !important;
        background: {t['surface']} !important;
        border: 1px solid {t['border']} !important;
        border-radius: 28px !important;
        box-shadow: {t['glow']}, 0 25px 50px -12px rgba(0,0,0,0.6) !important;
        backdrop-filter: blur(16px);
        margin-top: 1.5rem !important;
    }}

    h1, h2, h3, h4 {{
        color: {t['primary']} !important;
        font-family: {t['font']} !important;
        letter-spacing: 0.5px;
    }}

    p, span, label, .stMarkdown {{
        color: {t['text']} !important;
    }}

    .stButton > button {{
        background: linear-gradient(135deg, {t['primary']}33, {t['secondary']}22) !important;
        color: {t['text']} !important;
        border: 1px solid {t['border']} !important;
        border-radius: {t['radius']} !important;
        font-weight: 600 !important;
        transition: all 0.25s ease !important;
        box-shadow: {t['glow']} !important;
    }}
    .stButton > button:hover {{
        background: linear-gradient(135deg, {t['primary']}55, {t['secondary']}44) !important;
        transform: translateY(-2px);
        box-shadow: 0 0 30px {t['primary']}88 !important;
    }}

    .stButton > button[kind="primary"] {{
        background: linear-gradient(135deg, {t['primary']}, {t['secondary']}) !important;
        color: #000 !important;
        border: none !important;
    }}

    .stTextArea textarea, .stTextInput input {{
        background: rgba(0,0,0,0.35) !important;
        color: {t['text']} !important;
        border: 1px solid {t['border']} !important;
        border-radius: {t['radius']} !important;
        font-family: {t['font']} !important;
    }}

    .stSelectbox > div > div {{
        background: rgba(0,0,0,0.35) !important;
        border: 1px solid {t['border']} !important;
        border-radius: {t['radius']} !important;
        color: {t['text']} !important;
    }}

    .stCodeBlock, pre {{
        background: rgba(0,0,0,0.5) !important;
        border: 1px solid {t['border']} !important;
        border-radius: {t['radius']} !important;
    }}

    .stSuccess, .stInfo, .stWarning {{
        background: {t['surface']} !important;
        border-left: 4px solid {t['primary']} !important;
        border-radius: {t['radius']} !important;
    }}

    .vibe-header {{
        text-align: center;
        margin-bottom: 0.5rem;
    }}
    .vibe-sub {{
        text-align: center;
        color: {t['muted']} !important;
        font-size: 0.85rem;
        margin-bottom: 1.5rem;
    }}
    .theme-pill {{
        display: inline-block;
        padding: 0.25rem 0.75rem;
        border-radius: 999px;
        background: {t['primary']}22;
        border: 1px solid {t['border']};
        color: {t['primary']};
        font-size: 0.7rem;
        margin-bottom: 1rem;
    }}
    .copy-box {{
        background: rgba(0,0,0,0.4);
        border: 1px solid {t['border']};
        border-radius: {t['radius']};
        padding: 1rem;
        margin: 1rem 0;
    }}
    """
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)


if "theme" not in st.session_state:
    st.session_state.theme = "Cyberpunk Neon"
if "api_key" not in st.session_state:
    st.session_state.api_key = os.getenv("GEMINI_API_KEY", "")


def get_client(api_key: str) 
