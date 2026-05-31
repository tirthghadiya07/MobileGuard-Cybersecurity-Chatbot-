# ============================================================
#  MobileGuard — AI-Powered Mobile Security Chatbot
#  Student   : Tirth
#  Topic     : Mobile Security (Smartphone & iOS Security)
#  Subject   : AICS — Assignment 3 | 2025-26
#  Framework : Python + Streamlit
# ============================================================

# ────────────────────────────────────────
#  SECTION 1: IMPORTS
#  We only use built-in Python modules +
#  Streamlit. No extra installs needed
#  except: pip install streamlit
# ────────────────────────────────────────
import html as html_lib
import streamlit as st      # Web UI framework
import re                   # Regular expressions for PIN checking
import random               # For quiz shuffling and fallback messages

# Import our custom modules
from chatbot import get_response, QUICK_TIPS   # Chatbot logic
from quiz import QUIZ_QUESTIONS                # Quiz questions

# ────────────────────────────────────────
#  SECTION 2: STREAMLIT PAGE CONFIGURATION
#  Must be the FIRST Streamlit command
# ────────────────────────────────────────
st.set_page_config(
    page_title="MobileGuard – Security Chatbot",  # Browser tab title
    page_icon="📱",                                # Browser tab icon
    layout="wide",                                 # Use full screen width
    initial_sidebar_state="expanded",              # Sidebar open by default
)

# ────────────────────────────────────────
#  SECTION 3: CUSTOM CSS STYLING
#  We inject custom CSS to override
#  Streamlit's default white theme and
#  create a dark cybersecurity look.
#
#  st.markdown() with unsafe_allow_html=True
#  lets us write raw HTML/CSS into the page.
# ────────────────────────────────────────
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&family=Orbitron:wght@500;700;900&family=JetBrains+Mono:wght@400;500&display=swap');

/* ── MOBILEGUARD DESIGN TOKENS (unified palette) ─── */
:root {
    --mg-bg: #060913;
    --mg-bg-card: rgba(10, 15, 30, 0.85);
    --mg-primary: #6366f1;
    --mg-primary-light: #818cf8;
    --mg-primary-deep: #4f46e5;
    --mg-accent: #22d3ee;
    --mg-gradient: linear-gradient(135deg, #6366f1 0%, #22d3ee 100%);
    --mg-gradient-h: linear-gradient(90deg, #818cf8 0%, #22d3ee 100%);
    --mg-text: #e2e8f0;
    --mg-text-muted: #94a3b8;
    --mg-border: rgba(99, 102, 241, 0.28);
    --mg-border-accent: rgba(34, 211, 238, 0.22);
    --mg-glow: rgba(99, 102, 241, 0.4);
    --mg-glow-accent: rgba(34, 211, 238, 0.3);
    --mg-success: #10b981;
    --mg-success-bg: rgba(16, 185, 129, 0.12);
    --mg-danger: #f43f5e;
    --mg-warning: #f59e0b;
    --mg-radius: 14px;
}

/* ── GLOBAL BACKGROUND & TYPOGRAPHY ───────────────── */
html, body, [data-testid="stAppViewContainer"] {
    font-family: 'Outfit', sans-serif;
}

.stApp {
    background-color: var(--mg-bg);
    background-image:
        linear-gradient(rgba(99, 102, 241, 0.04) 1px, transparent 1px),
        linear-gradient(90deg, rgba(34, 211, 238, 0.03) 1px, transparent 1px);
    background-size: 30px 30px;
    color: var(--mg-text);
}

/* Main content area — reduce top gap */
.st-emotion-cache-zy6yx3,
[data-testid="stMainBlockContainer"] {
    width: 100% !important;
    padding: 1.1rem 6rem 10rem !important;
    max-width: initial !important;
    min-width: auto !important;
}

/* ── FORCE SIDEBAR ALWAYS VISIBLE & TRANSITIONS ───── */
section[data-testid="stSidebar"] {
    transform: translate(0px, 0px) !important;
    margin-left: 0px !important;
    width: 21rem !important;
    min-width: 21rem !important;
    transition: transform 0.3s ease, width 0.3s ease !important;
}

/* Adjust app content layout to prevent overlap with the forced-open sidebar */
# div[data-testid="stAppViewContainer"] {
#     margin-left: 21rem !important;
# }

/* On mobile/narrow screens, let it behave responsively */
@media (max-width: 991px) {
    div[data-testid="stAppViewContainer"] {
        margin-left: 0px !important;
    }
}

/* Style the collapse/expand trigger button to look like a neon scanner scanner icon */
div[data-testid="collapsedControl"] {
    background: #090e1a !important;
    border: 1px solid var(--mg-border) !important;
    border-radius: 0 8px 8px 0 !important;
    padding: 6px !important;
    box-shadow: 0 0 15px var(--mg-glow) !important;
    transition: all 0.3s ease;
}

div[data-testid="collapsedControl"] button {
    color: var(--mg-accent) !important;
}

/* ── ANIMATIONS ──────────────────────────────── */
@keyframes fadeIn {
    from { opacity: 0; transform: translateY(15px); }
    to { opacity: 1; transform: translateY(0); }
}

/* Smooth fade-in for page contents */
.cyber-card, .chat-container, .stAlert, .bot-bubble, .user-bubble, div[data-testid="stForm"] {
    animation: fadeIn 0.5s cubic-bezier(0.16, 1, 0.3, 1) both;
}

/* Neon glow pulsate animation for buttons */
@keyframes neonPulsate {
    0% { box-shadow: 0 0 5px var(--mg-glow-accent); }
    50% { box-shadow: 0 0 18px var(--mg-glow); }
    100% { box-shadow: 0 0 5px var(--mg-glow-accent); }
}

.stButton > button, div[data-testid="stFormSubmitButton"] button {
    animation: neonPulsate 3s infinite alternate;
}

/* ── SIDEBAR — COMMAND PANEL REDESIGN ─────────── */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #060913 0%, #0a0f1c 45%, #0f172a 100%) !important;
    border-right: none !important;
    box-shadow: 8px 0 40px rgba(0, 0, 0, 0.65), inset -1px 0 0 var(--mg-border) !important;
    z-index: 10 !important;
    animation: slideInSidebar 0.45s cubic-bezier(0.22, 1, 0.36, 1) forwards;
}

section[data-testid="stSidebar"]::before {
    content: "";
    position: fixed;
    top: 0;
    left: 0;
    width: 4px;
    height: 100vh;
    background: linear-gradient(180deg, var(--mg-primary-deep) 0%, var(--mg-primary) 50%, var(--mg-accent) 100%);
    z-index: 11;
    pointer-events: none;
}

section[data-testid="stSidebar"] > div:first-child {
    background: transparent !important;
    padding: 0.25rem 0.85rem 1.25rem 1rem !important;
}

@keyframes slideInSidebar {
    from { transform: translateX(-12px); opacity: 0.6; }
    to { transform: translateX(0); opacity: 1; }
}

@keyframes sbPulse {
    0%, 100% { opacity: 1; box-shadow: 0 0 0 0 var(--mg-glow-accent); }
    50% { opacity: 0.85; box-shadow: 0 0 0 6px rgba(34, 211, 238, 0); }
}

@keyframes sbShimmer {
    0% { background-position: 200% center; }
    100% { background-position: -200% center; }
}

/* Brand shell */
.sb-shell {
    background: linear-gradient(145deg, rgba(99, 102, 241, 0.14) 0%, rgba(15, 23, 42, 0.92) 55%);
    border: 1px solid var(--mg-border);
    border-radius: 16px;
    padding: 18px 16px 14px;
    margin-bottom: 14px;
    position: relative;
    overflow: hidden;
}
.sb-shell::after {
    content: "";
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 2px;
    background: linear-gradient(90deg, transparent, var(--mg-primary), var(--mg-accent), transparent);
    background-size: 200% auto;
    animation: sbShimmer 4s linear infinite;
}
.sb-logo-row {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 10px;
}
.sb-logo-ring {
    width: 48px;
    height: 48px;
    border-radius: 14px;
    background: var(--mg-gradient);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 22px;
    box-shadow: 0 8px 24px rgba(99, 102, 241, 0.45);
    flex-shrink: 0;
}
.sb-brand-title {
    font-family: 'Orbitron', sans-serif;
    font-size: 1.05rem;
    font-weight: 800;
    letter-spacing: 2px;
    color: #f8fafc !important;
    line-height: 1.2;
    margin: 0;
}
.sb-brand-sub {
    font-size: 11px;
    color: #94a3b8 !important;
    margin: 2px 0 0;
    letter-spacing: 0.3px;
}
.sb-stats {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 8px;
    margin-top: 12px;
}
.sb-stat {
    background: rgba(0, 0, 0, 0.35);
    border: 1px solid rgba(148, 163, 184, 0.12);
    border-radius: 10px;
    padding: 8px 10px;
    text-align: center;
}
.sb-stat-num {
    font-family: 'Orbitron', sans-serif;
    font-size: 1.1rem;
    font-weight: 700;
    color: var(--mg-accent) !important;
    display: block;
}
.sb-stat-lbl {
    font-size: 9px;
    text-transform: uppercase;
    letter-spacing: 0.8px;
    color: #64748b !important;
}

/* Live status strip */
.sb-status {
    display: flex;
    align-items: center;
    justify-content: space-between;
    background: var(--mg-success-bg);
    border: 1px solid rgba(16, 185, 129, 0.35);
    border-radius: 999px;
    padding: 6px 12px;
    margin-bottom: 16px;
    font-size: 11px;
    font-family: 'JetBrains Mono', monospace;
}
.sb-status-dot {
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background: var(--mg-success);
    animation: sbPulse 2s ease-in-out infinite;
    margin-right: 8px;
    flex-shrink: 0;
}
.sb-status-text { color: #6ee7b7 !important; font-weight: 500; }
.sb-status-tag {
    color: #34d399 !important;
    font-weight: 700;
    font-size: 10px;
    letter-spacing: 0.5px;
}

/* Section labels */
.sb-section-label {
    font-family: 'Orbitron', sans-serif;
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 2px;
    color: var(--mg-primary-light) !important;
    margin: 4px 0 10px 2px;
    display: flex;
    align-items: center;
    gap: 8px;
}
.sb-section-label::after {
    content: "";
    flex: 1;
    height: 1px;
    background: linear-gradient(90deg, rgba(129, 140, 248, 0.5), transparent);
}

/* Tips panel */
.sb-tips-panel {
    background: rgba(2, 6, 23, 0.55);
    border: 1px solid rgba(99, 102, 241, 0.2);
    border-radius: 14px;
    padding: 12px 10px 8px;
    margin-top: 4px;
    max-height: 220px;
    overflow-y: auto;
    scrollbar-width: thin;
    scrollbar-color: #6366f1 transparent;
}
.sb-tips-panel::-webkit-scrollbar { width: 4px; }
.sb-tips-panel::-webkit-scrollbar-thumb {
    background: #6366f1;
    border-radius: 4px;
}

.sb-tip-item {
    display: flex;
    align-items: flex-start;
    gap: 10px;
    padding: 10px 10px;
    margin-bottom: 6px;
    border-radius: 10px;
    background: rgba(30, 41, 59, 0.45);
    border-left: 3px solid transparent;
    transition: all 0.25s ease;
}
.sb-tip-item:hover {
    background: rgba(99, 102, 241, 0.15);
    border-left-color: var(--mg-primary);
    transform: translateX(3px);
}
.sb-tip-num {
    font-family: 'Orbitron', sans-serif;
    font-size: 10px;
    font-weight: 700;
    color: var(--mg-primary-light) !important;
    background: rgba(99, 102, 241, 0.18);
    border-radius: 6px;
    padding: 4px 6px;
    min-width: 26px;
    text-align: center;
    flex-shrink: 0;
}
.sb-tip-icon { font-size: 14px; line-height: 1.4; flex-shrink: 0; }
.sb-tip-text {
    font-size: 12px;
    color: #cbd5e1 !important;
    line-height: 1.45;
    margin: 0;
}

/* Rule-based AI engine panel */
.sb-ai-panel {
    margin-top: 14px;
    padding: 14px;
    border-radius: var(--mg-radius);
    background: linear-gradient(160deg, rgba(99, 102, 241, 0.18) 0%, rgba(6, 9, 19, 0.95) 100%);
    border: 1px solid var(--mg-border);
    box-shadow: 0 8px 28px rgba(0, 0, 0, 0.35), inset 0 1px 0 rgba(34, 211, 238, 0.08);
    position: relative;
    overflow: hidden;
}
.sb-ai-panel::before {
    content: "";
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 1px;
    background: var(--mg-gradient-h);
}
.sb-ai-head {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 12px;
}
.sb-ai-icon-wrap {
    width: 42px;
    height: 42px;
    border-radius: 12px;
    background: var(--mg-gradient);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 20px;
    box-shadow: 0 6px 20px var(--mg-glow);
    flex-shrink: 0;
}
.sb-ai-title {
    font-family: 'Orbitron', sans-serif;
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 1.5px;
    color: var(--mg-accent) !important;
    margin: 0;
    line-height: 1.3;
}
.sb-ai-sub {
    font-size: 10px;
    color: var(--mg-text-muted) !important;
    margin: 3px 0 0;
}
.sb-ai-pipeline {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 4px;
    margin-bottom: 12px;
    padding: 10px 8px;
    background: rgba(0, 0, 0, 0.35);
    border-radius: 10px;
    border: 1px solid rgba(99, 102, 241, 0.2);
}
.sb-ai-node {
    flex: 1;
    text-align: center;
    font-family: 'JetBrains Mono', monospace;
    font-size: 9px;
    font-weight: 600;
    letter-spacing: 0.5px;
    text-transform: uppercase;
    color: var(--mg-text-muted) !important;
    padding: 6px 4px;
    border-radius: 8px;
    border: 1px solid transparent;
}
.sb-ai-node span { display: block; color: inherit !important; }
.sb-ai-node.active {
    color: var(--mg-accent) !important;
    background: rgba(99, 102, 241, 0.2);
    border-color: var(--mg-border-accent);
    box-shadow: 0 0 12px var(--mg-glow-accent);
}
.sb-ai-arrow {
    color: var(--mg-primary-light) !important;
    font-size: 12px;
    font-weight: 700;
    flex-shrink: 0;
}
.sb-ai-chips {
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
    margin-bottom: 12px;
}
.sb-chip {
    font-family: 'JetBrains Mono', monospace;
    font-size: 9px;
    font-weight: 600;
    letter-spacing: 0.4px;
    padding: 4px 8px;
    border-radius: 6px;
    color: var(--mg-primary-light) !important;
    background: rgba(99, 102, 241, 0.15);
    border: 1px solid var(--mg-border);
}
.sb-ai-coverage-top {
    display: flex;
    justify-content: space-between;
    font-size: 10px;
    color: var(--mg-text-muted) !important;
    margin-bottom: 6px;
}
.sb-ai-coverage-top span:last-child {
    color: var(--mg-accent) !important;
    font-family: 'Orbitron', sans-serif;
    font-weight: 700;
    font-size: 9px;
}
.sb-ai-bar {
    height: 6px;
    background: rgba(15, 23, 42, 0.9);
    border-radius: 999px;
    overflow: hidden;
    border: 1px solid var(--mg-border);
}
.sb-ai-bar-fill {
    height: 100%;
    width: 100%;
    background: var(--mg-gradient);
    border-radius: 999px;
    box-shadow: 0 0 10px var(--mg-glow-accent);
}

/* Footer card */
.sb-footer {
    margin-top: 10px;
    padding: 12px 14px;
    border-radius: 12px;
    background: var(--mg-bg-card);
    border: 1px dashed var(--mg-border);
}
.sb-footer-row {
    display: flex;
    align-items: center;
    gap: 8px;
    font-size: 11px;
    color: var(--mg-text-muted) !important;
    margin: 5px 0;
    line-height: 1.35;
}
.sb-footer-row strong { color: var(--mg-text) !important; font-weight: 600; }

[data-testid="stSidebar"] hr {
    border: none !important;
    height: 1px !important;
    background: linear-gradient(90deg, transparent, rgba(129, 140, 248, 0.35), transparent) !important;
    margin: 14px 0 !important;
}
[data-testid="stSidebar"] .stMarkdown p,
[data-testid="stSidebar"] .stMarkdown h3 {
    color: inherit;
}

/* ── HEADINGS ────────────────────────────────── */
.main-title {
    font-family: 'Orbitron', sans-serif;
    font-size: 2.2rem;
    font-weight: 900;
    background: var(--mg-gradient-h);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    text-align: center;
    margin-bottom: 2px;
    letter-spacing: 1px;
}

.subtitle {
    text-align: center;
    color: var(--mg-text-muted);
    font-size: 15px;
    margin-bottom: 25px;
    font-weight: 400;
}

/* ── CHAT WINDOW CONTAINER ───────────────────── */
.chat-container {
    background: var(--mg-bg-card);
    backdrop-filter: blur(12px);
    border-radius: var(--mg-radius);
    padding: 20px;
    margin-bottom: 20px;
    border: 1px solid var(--mg-border-accent);
    max-height: 480px;
    overflow-y: auto;
    box-shadow: inset 0 0 20px var(--mg-glow-accent), 0 10px 30px rgba(0,0,0,0.4);
}

/* ── USER & BOT BUBBLES ──────────────────────── */
.user-bubble {
    background: var(--mg-gradient);
    color: white;
    border-radius: 16px 16px 2px 16px;
    padding: 12px 18px;
    margin: 10px 0 10px auto;
    max-width: 75%;
    font-size: 15px;
    line-height: 1.5;
    box-shadow: 0 4px 15px var(--mg-glow);
    border: 1px solid rgba(255,255,255,0.1);
}

.bot-bubble {
    background: rgba(15, 23, 42, 0.9);
    color: #e2e8f0;
    border-radius: 16px 16px 16px 2px;
    padding: 14px 18px;
    margin: 10px auto 10px 0;
    max-width: 75%;
    border-left: 4px solid var(--mg-accent);
    border-top: 1px solid var(--mg-border-accent);
    border-right: 1px solid rgba(99, 102, 241, 0.12);
    border-bottom: 1px solid rgba(99, 102, 241, 0.12);
    font-size: 15px;
    line-height: 1.6;
    white-space: pre-wrap;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
}

/* ── BUTTON STYLING (OVERRIDE STREAMLIT) ─────── */
.stButton > button, div[data-testid="stFormSubmitButton"] button {
    background: linear-gradient(135deg, rgba(15, 23, 42, 0.9) 0%, rgba(30, 41, 59, 0.85) 100%) !important;
    color: var(--mg-accent) !important;
    border: 1px solid var(--mg-border) !important;
    border-radius: 10px !important;
    padding: 12px 20px !important;
    width: 100%;
    text-align: center;
    font-family: 'Orbitron', sans-serif !important;
    font-size: 14px !important;
    font-weight: 600 !important;
    letter-spacing: 0.5px;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
}

.stButton > button:hover, div[data-testid="stFormSubmitButton"] button:hover {
    background: var(--mg-gradient) !important;
    color: var(--mg-bg) !important;
    border-color: var(--mg-accent) !important;
    box-shadow: 0 0 20px var(--mg-glow) !important;
    transform: translateY(-2px);
}

.stButton > button:active, div[data-testid="stFormSubmitButton"] button:active {
    transform: translateY(0);
}

/* ── INPUT FIELD STYLING ─────────────────────── */
.stTextInput > div > div > input {
    background-color: rgba(15, 23, 42, 0.8) !important;
    color: #f1f5f9 !important;
    border: 1px solid var(--mg-border) !important;
    border-radius: 10px !important;
    padding: 12px 16px !important;
    font-size: 15px !important;
    font-family: 'Outfit', sans-serif;
    transition: all 0.3s ease;
}

.stTextInput > div > div > input:focus {
    border-color: var(--mg-accent) !important;
    box-shadow: 0 0 15px var(--mg-glow-accent) !important;
}

/* ── MULTISELECT STYLING ─────────────────────── */
.stMultiSelect > div {
    background-color: rgba(15, 23, 42, 0.8) !important;
    border: 1px solid var(--mg-border) !important;
    border-radius: 10px !important;
}

/* ── PROGRESS BAR ────────────────────────────── */
.stProgress > div > div > div {
    background: var(--mg-gradient) !important;
    height: 8px !important;
    border-radius: 4px;
}

/* ── SCORE BADGE ─────────────────────────────── */
.score-badge {
    display: inline-block;
    background: var(--mg-gradient);
    color: var(--mg-bg);
    border-radius: 30px;
    padding: 8px 24px;
    font-family: 'Orbitron', sans-serif;
    font-weight: 700;
    font-size: 24px;
    margin-top: 15px;
    box-shadow: 0 0 20px var(--mg-glow);
}

/* ── HIDE STREAMLIT BRANDING ─────────────────── */
#MainMenu  { visibility: hidden; }
footer     { visibility: hidden; }
header     { visibility: hidden; }

/* ── MAIN AREA RADIO (non-sidebar) ───────────── */
div:not([data-testid="stSidebar"]) div[data-testid="stRadio"] > div {
    background: rgba(15, 23, 42, 0.5);
    border-radius: 12px;
    padding: 10px;
    border: 1px solid rgba(255, 255, 255, 0.05);
}
div:not([data-testid="stSidebar"]) div[data-testid="stRadio"] label {
    font-family: 'Outfit', sans-serif;
    font-weight: 500 !important;
    font-size: 15px !important;
    padding: 8px 12px !important;
    border-radius: 8px;
    transition: all 0.2s ease;
}
div:not([data-testid="stSidebar"]) div[data-testid="stRadio"] label:hover {
    background: rgba(99, 102, 241, 0.12);
    color: var(--mg-accent) !important;
}

/* ── INFO/ALERT BOXES ────────────────────────── */
.stAlert {
    background-color: rgba(15, 23, 42, 0.8) !important;
    border: 1px solid var(--mg-border-accent) !important;
    border-radius: 12px !important;
    color: #cbd5e1 !important;
}

/* ── DIVIDER STYLE ───────────────────────────── */
hr {
    border-color: var(--mg-border-accent) !important;
    margin: 16px 0 !important;
}

/* ── CUSTOM CYBER CONTAINERS & QUIZ ──────────── */
.cyber-card {
    background: var(--mg-bg-card);
    backdrop-filter: blur(12px);
    border: 1px solid var(--mg-border-accent);
    border-radius: var(--mg-radius);
    padding: 24px;
    margin-bottom: 20px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.3);
}

.terminal-title {
    font-family: 'Orbitron', sans-serif;
    font-size: 14px;
    color: var(--mg-accent);
    font-weight: 700;
    margin-bottom: 12px;
    letter-spacing: 1px;
    text-transform: uppercase;
}

.cyber-badge {
    background: rgba(99, 102, 241, 0.12);
    color: var(--mg-accent);
    border: 1px solid var(--mg-border);
    padding: 4px 10px;
    border-radius: 6px;
    font-family: 'Orbitron', sans-serif;
    font-size: 11px;
    font-weight: 600;
}

.risk-pill-high {
    background: rgba(244, 63, 94, 0.12) !important;
    color: var(--mg-danger) !important;
    border: 1px solid rgba(244, 63, 94, 0.35) !important;
    padding: 6px 12px;
    border-radius: 20px;
    font-weight: 700;
    font-size: 13px;
    display: inline-block;
}

.risk-pill-medium {
    background: rgba(245, 158, 11, 0.1) !important;
    color: var(--mg-warning) !important;
    border: 1px solid rgba(245, 158, 11, 0.3) !important;
    padding: 6px 12px;
    border-radius: 20px;
    font-weight: 700;
    font-size: 13px;
    display: inline-block;
}

.risk-pill-low {
    background: var(--mg-success-bg) !important;
    color: var(--mg-success) !important;
    border: 1px solid rgba(16, 185, 129, 0.35) !important;
    padding: 6px 12px;
    border-radius: 20px;
    font-weight: 700;
    font-size: 13px;
    display: inline-block;
}

/* ── SIDEBAR NAV BUTTONS ─────────────────────── */
[data-testid="stSidebar"] .nav-btn-wrap {
    margin-bottom: 4px;
}
[data-testid="stSidebar"] .stButton > button {
    animation: none !important;
    text-align: left !important;
    justify-content: flex-start !important;
    padding: 11px 14px !important;
    font-family: 'Outfit', sans-serif !important;
    font-size: 13.5px !important;
    font-weight: 500 !important;
    border-radius: 12px !important;
    border: 1px solid var(--mg-border) !important;
    background: rgba(15, 23, 42, 0.75) !important;
    color: var(--mg-text-muted) !important;
}
[data-testid="stSidebar"] .stButton > button:hover {
    border-color: var(--mg-primary-light) !important;
    color: var(--mg-text) !important;
    background: rgba(99, 102, 241, 0.15) !important;
    transform: none !important;
    box-shadow: none !important;
}
[data-testid="stSidebar"] .stButton > button[kind="primary"],
[data-testid="stSidebar"] .stButton > button[data-testid="baseButton-primary"] {
    background: var(--mg-gradient) !important;
    color: var(--mg-bg) !important;
    border-color: var(--mg-accent) !important;
    font-weight: 600 !important;
    box-shadow: 0 4px 16px var(--mg-glow) !important;
}
[data-testid="stSidebar"] .sb-nav-hint {
    font-size: 10px;
    color: var(--mg-text-muted) !important;
    margin: 0 0 10px 2px;
    font-family: 'JetBrains Mono', monospace;
}

/* ── MAIN PAGE LAYOUT ────────────────────────── */
.page-shell {
    max-width: 1100px;
    margin: 0 auto;
    padding: 0 8px 32px;
}
.page-hero {
    display: flex;
    align-items: center;
    gap: 20px;
    padding: 22px 26px;
    margin-bottom: 22px;
    background: var(--mg-bg-card);
    border: 1px solid var(--mg-border-accent);
    border-radius: var(--mg-radius);
    box-shadow: 0 12px 40px rgba(0, 0, 0, 0.35);
}
.page-hero-icon {
    width: 56px;
    height: 56px;
    border-radius: 16px;
    background: var(--mg-gradient);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 28px;
    flex-shrink: 0;
    box-shadow: 0 8px 24px var(--mg-glow);
}
.page-hero-title {
    font-family: 'Orbitron', sans-serif;
    font-size: 1.65rem;
    font-weight: 800;
    margin: 0;
    background: var(--mg-gradient-h);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    letter-spacing: 0.5px;
}
.page-hero-sub {
    color: var(--mg-text-muted) !important;
    font-size: 15px;
    margin: 6px 0 0;
    line-height: 1.45;
}
.page-badges {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    margin-top: 10px;
}
.page-badge {
    font-family: 'JetBrains Mono', monospace;
    font-size: 10px;
    font-weight: 600;
    padding: 4px 10px;
    border-radius: 6px;
    color: var(--mg-accent) !important;
    background: rgba(99, 102, 241, 0.15);
    border: 1px solid var(--mg-border);
    letter-spacing: 0.3px;
}
.page-body {
    margin-top: 4px;
}
.page-body .stForm,
.page-body > div[data-testid="stTextInput"],
.page-body > div[data-testid="stMultiSelect"] {
    background: var(--mg-bg-card);
    border: 1px solid var(--mg-border-accent);
    border-radius: var(--mg-radius);
    padding: 16px 18px;
    margin-bottom: 16px;
}
.section-heading {
    font-family: 'Orbitron', sans-serif;
    font-size: 12px;
    color: var(--mg-accent) !important;
    letter-spacing: 1.2px;
    margin: 18px 0 10px;
    font-weight: 700;
}
.welcome-card {
    background: linear-gradient(135deg, rgba(99, 102, 241, 0.12), rgba(34, 211, 238, 0.06));
    border: 1px solid var(--mg-border-accent);
    border-radius: var(--mg-radius);
    padding: 18px 22px;
    margin-bottom: 20px;
    line-height: 1.6;
}
.welcome-card-title {
    font-family: 'Orbitron', sans-serif;
    font-size: 13px;
    color: var(--mg-accent) !important;
    font-weight: 700;
    letter-spacing: 1px;
    margin: 0 0 8px;
}
.welcome-card p {
    color: var(--mg-text) !important;
    margin: 0;
    font-size: 15px;
}
.input-card {
    background: var(--mg-bg-card);
    border: 1px solid var(--mg-border-accent);
    border-radius: var(--mg-radius);
    padding: 22px 24px;
    margin-bottom: 20px;
}
.input-card .terminal-title {
    margin-bottom: 16px;
}
.feature-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 12px;
    margin-bottom: 22px;
}
.feature-tile {
    background: rgba(15, 23, 42, 0.6);
    border: 1px solid var(--mg-border);
    border-radius: 12px;
    padding: 14px 16px;
    text-align: center;
}
.feature-tile-icon { font-size: 22px; margin-bottom: 6px; }
.feature-tile-label {
    font-size: 11px;
    color: var(--mg-text-muted) !important;
    text-transform: uppercase;
    letter-spacing: 0.8px;
}
.feature-tile-value {
    font-family: 'Orbitron', sans-serif;
    font-size: 1.1rem;
    color: var(--mg-accent) !important;
    font-weight: 700;
    margin-top: 4px;
}
.quiz-progress-label {
    font-family: 'Orbitron', sans-serif;
    font-size: 12px;
    color: var(--mg-accent) !important;
    letter-spacing: 1px;
    margin-bottom: 8px;
}

</style>
""", unsafe_allow_html=True)


# ────────────────────────────────────────
#  SECTION 4: SESSION STATE INITIALIZATION
#
#  Streamlit re-runs the full script on
#  every user interaction (click/type).
#  Session State stores variables that
#  must PERSIST between re-runs.
#
#  Think of it like the app's memory.
# ────────────────────────────────────────

# ── Chatbot state ──
if "chat_history" not in st.session_state:
    # Stores list of tuples: ("user", message) or ("bot", message)
    st.session_state.chat_history = []

# ── Quiz state ──
if "quiz_started" not in st.session_state:
    st.session_state.quiz_started   = False   # Has quiz begun?
    st.session_state.quiz_done      = False   # Is quiz finished?
    st.session_state.quiz_index     = 0       # Current question number
    st.session_state.quiz_score     = 0       # Running score
    st.session_state.quiz_answered  = False   # Has current Q been answered?
    st.session_state.quiz_selected  = None    # Which option was chosen
    # Pick 7 random questions from the 10 available
    st.session_state.quiz_questions = random.sample(
        QUIZ_QUESTIONS, min(7, len(QUIZ_QUESTIONS))
    )

if "page" not in st.session_state:
    st.session_state.page = "💬 Chatbot"

NAV_ITEMS = [
    "💬 Chatbot",
    "🧠 Security Quiz",
    "🔍 App Permission Checker",
    "💪 PIN Strength Checker",
]

TIP_ICONS = ["🔄", "🔐", "📶", "🛒", "🛡️", "💾", "📡", "🔍"]


def show_html(content: str) -> None:
    """Render HTML without markdown code-block escaping."""
    if hasattr(st, "html"):
        st.html(content)
    else:
        st.markdown(content, unsafe_allow_html=True)


def page_hero(icon: str, title: str, subtitle: str, badges: list | None = None) -> None:
    badge_html = "".join(
        f'<span class="page-badge">{html_lib.escape(b)}</span>' for b in (badges or [])
    )
    show_html(
        f'<div class="page-hero">'
        f'<div class="page-hero-icon">{icon}</div>'
        f'<div><h1 class="page-hero-title">{html_lib.escape(title)}</h1>'
        f'<p class="page-hero-sub">{html_lib.escape(subtitle)}</p>'
        f'<div class="page-badges">{badge_html}</div></div></div>'
    )


def render_security_tips() -> None:
    parts = ['<div class="sb-tips-panel">']
    for i, tip in enumerate(QUICK_TIPS, start=1):
        icon = TIP_ICONS[i - 1] if i <= len(TIP_ICONS) else "💡"
        parts.append(
            '<div class="sb-tip-item">'
            f'<span class="sb-tip-num">{i:02d}</span>'
            f'<span class="sb-tip-icon">{icon}</span>'
            f'<p class="sb-tip-text">{html_lib.escape(tip)}</p>'
            '</div>'
        )
    parts.append('</div>')
    show_html(''.join(parts))


# ════════════════════════════════════════
#  SECTION 5: SIDEBAR
#  Renders on ALL pages — always visible.
#  Contains: logo, navigation, tips, footer
# ════════════════════════════════════════
with st.sidebar:

    # ── Brand header card ──
    show_html("""
    <div class="sb-shell">
        <div class="sb-logo-row">
            <div class="sb-logo-ring">🛡️</div>
            <div>
                <p class="sb-brand-title">MOBILEGUARD</p>
                <p class="sb-brand-sub">Mobile Security Command Center</p>
            </div>
        </div>
        <div class="sb-stats">
            <div class="sb-stat">
                <span class="sb-stat-num">4</span>
                <span class="sb-stat-lbl">Modules</span>
            </div>
            <div class="sb-stat">
                <span class="sb-stat-num">8</span>
                <span class="sb-stat-lbl">Live Tips</span>
            </div>
        </div>
    </div>
    <div class="sb-status">
        <span style="display:flex;align-items:center;">
            <span class="sb-status-dot"></span>
            <span class="sb-status-text">System Online</span>
        </span>
        <span class="sb-status-tag">SECURE</span>
    </div>
    """)

    show_html('<p class="sb-section-label">NAVIGATION</p>')
    show_html('<p class="sb-nav-hint">Select a module to open</p>')

    for nav_label in NAV_ITEMS:
        is_active = st.session_state.page == nav_label
        if st.button(
            nav_label,
            key=f"nav_{nav_label}",
            use_container_width=True,
            type="primary" if is_active else "secondary",
        ):
            if not is_active:
                st.session_state.page = nav_label
                st.rerun()

    show_html('<p class="sb-section-label">SECURITY INTEL</p>')
    render_security_tips()

    show_html('<p class="sb-section-label">AI ENGINE</p>')

    show_html("""
    <div class="sb-ai-panel">
        <div class="sb-ai-head">
            <div class="sb-ai-icon-wrap">🧠</div>
            <div>
                <p class="sb-ai-title">RULE-BASED AI CHATBOT</p>
                <p class="sb-ai-sub">Keyword scoring · No cloud API · Runs locally</p>
            </div>
        </div>
        <div class="sb-ai-pipeline">
            <div class="sb-ai-node"><span>Input</span></div>
            <div class="sb-ai-arrow">›</div>
            <div class="sb-ai-node"><span>Match</span></div>
            <div class="sb-ai-arrow">›</div>
            <div class="sb-ai-node active"><span>Reply</span></div>
        </div>
        <div class="sb-ai-chips">
            <span class="sb-chip">18 Topics</span>
            <span class="sb-chip">Offline</span>
            <span class="sb-chip">Instant</span>
            <span class="sb-chip">No API Key</span>
        </div>
        <div class="sb-ai-coverage">
            <div class="sb-ai-coverage-top">
                <span>Knowledge coverage</span>
                <span>18 / 18 ACTIVE</span>
            </div>
            <div class="sb-ai-bar"><div class="sb-ai-bar-fill"></div></div>
        </div>
    </div>
    <div class="sb-footer">
        <div class="sb-footer-row">📘 <strong>AICS</strong> · Assignment 3 · 2025-26</div>
        <div class="sb-footer-row">🎯 <strong>Topic</strong> · Mobile Security</div>
        <div class="sb-footer-row">👤 <strong>Student</strong> · Tirth</div>
    </div>
    """)

page = st.session_state.page


# ════════════════════════════════════════
#  SECTION 6: PAGE — 💬 CHATBOT
# ════════════════════════════════════════
if "💬 Chatbot" in page:

    show_html('<div class="page-shell">')
    page_hero(
        "💬",
        "MobileGuard Chatbot",
        "Ask anything about mobile & smartphone security.",
        ["18 Topics", "Rule-Based AI", "Instant Replies"],
    )

    show_html("""
    <div class="feature-grid">
        <div class="feature-tile"><div class="feature-tile-icon">🛡️</div>
            <div class="feature-tile-label">Coverage</div><div class="feature-tile-value">18 Topics</div></div>
        <div class="feature-tile"><div class="feature-tile-icon">⚡</div>
            <div class="feature-tile-label">Engine</div><div class="feature-tile-value">Keyword AI</div></div>
        <div class="feature-tile"><div class="feature-tile-icon">🔒</div>
            <div class="feature-tile-label">Privacy</div><div class="feature-tile-value">Local Only</div></div>
    </div>
    """)

    show_html('<div class="page-body">')

    if not st.session_state.chat_history:
        show_html("""
        <div class="welcome-card">
            <p class="welcome-card-title">👋 WELCOME TO MOBILEGUARD</p>
            <p>I'm your mobile security assistant. Ask about Android &amp; iOS security,
            app permissions, public Wi-Fi, malware, 2FA, SIM swap attacks, and more.</p>
        </div>
        """)

        show_html('<p style="color:#94a3b8;font-weight:600;margin-bottom:12px;">💡 Try asking one of these:</p>')
        suggestions = [
            "How do I secure my Android phone?",
            "Is public Wi-Fi safe on my phone?",
            "What app permissions are dangerous?",
            "How do I detect malware on my phone?",
        ]

        # Arrange 4 buttons in a 2x2 grid
        col1, col2 = st.columns(2)
        for i, suggestion in enumerate(suggestions):
            target_col = col1 if i % 2 == 0 else col2
            if target_col.button(suggestion, key=f"sug_{i}", use_container_width=True):
                # When clicked, process as if user typed it
                bot_reply = get_response(suggestion)
                st.session_state.chat_history.append(("user", suggestion))
                st.session_state.chat_history.append(("bot", bot_reply))
                st.rerun()   # Refresh to show new chat

    # ── Chat History Display ──
    if st.session_state.chat_history:
        # Build HTML for all messages at once
        chat_html = '<div class="chat-container">'
        for role, msg in st.session_state.chat_history:
            safe = html_lib.escape(msg).replace('\n', '<br>')
            if role == "user":
                chat_html += f'<div class="user-bubble">🧑 {safe}</div>'
            else:
                chat_html += f'<div class="bot-bubble">🤖 {safe}</div>'
        chat_html += '</div>'
        show_html(chat_html)

    show_html('<p class="section-heading">💬 SEND A MESSAGE</p>')
    with st.form("chat_form", clear_on_submit=True):
        col_input, col_btn = st.columns([5, 1])
        with col_input:
            user_input = st.text_input(
                "Your question",
                placeholder="e.g. How do I enable two-factor authentication on my phone?",
                label_visibility="collapsed",
                key="chat_input"
            )
        with col_btn:
            send_clicked = st.form_submit_button("Send 📨", use_container_width=True)

        if send_clicked and user_input.strip():
            bot_reply = get_response(user_input.strip())
            st.session_state.chat_history.append(("user", user_input.strip()))
            st.session_state.chat_history.append(("bot", bot_reply))
            st.rerun()

    # ── Clear Chat Button ──
    if st.session_state.chat_history:
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("🗑️ Clear Chat History"):
            st.session_state.chat_history = []
            st.rerun()

    show_html('</div></div>')


# ════════════════════════════════════════
#  SECTION 7: PAGE — 🧠 SECURITY QUIZ
# ════════════════════════════════════════
elif "🧠 Security Quiz" in page:

    show_html('<div class="page-shell">')
    page_hero(
        "🧠",
        "Mobile Security Quiz",
        "Test your smartphone security knowledge with 7 random questions.",
        ["7 Questions", "Instant Feedback", "Security Grade"],
    )
    show_html('<div class="page-body">')

    # Shorthand variables for cleaner code
    qs  = st.session_state.quiz_questions
    idx = st.session_state.quiz_index

    # ── STATE 0: START SCREEN ──
    if not st.session_state.quiz_started:
        st.markdown("""
        <div class="cyber-card">
            <div class="terminal-title">📋 SYSTEM PROTOCOL: MOBILE SECURITY ASSESSMENT</div>
            <div style="color: #cbd5e1; line-height: 1.6;">
                <p>• <b>7 randomized questions</b> targeting smartphone and mobile device threat vectors.</p>
                <p>• Choose the best defensive response for each security query.</p>
                <p>• Threat mitigation analysis and detailed security concepts are provided after every answer.</p>
                <p>• Diagnostic report card and security grade calculated upon completion.</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("---")
        if st.button("🚀 Start Security Audit", use_container_width=True):
            st.session_state.quiz_started = True
            st.rerun()
        show_html('</div></div>')

    # ── STATE 3: RESULTS SCREEN ──
    elif st.session_state.quiz_done:
        score  = st.session_state.quiz_score
        total  = len(qs)
        pct    = int((score / total) * 100)

        # Determine grade based on percentage
        if pct >= 80:
            grade, color, emoji = "System Secure", "#10b981", "🏆"
        elif pct >= 50:
            grade, color, emoji = "Threat Warning", "#22d3ee", "⚠️"
        else:
            grade, color, emoji = "Breach Detected", "#f43f5e", "🚨"

        # Results display
        st.markdown(f"""
        <div class="cyber-card" style='text-align:center;'>
            <div class="terminal-title">DIAGNOSTIC REPORT SUMMARY</div>
            <div style='font-size: 4.5rem; margin: 15px 0;'>{emoji}</div>
            <div style='font-size: 2.2rem; font-weight:900;
                        color:{color}; margin: 10px 0; font-family: "Orbitron", sans-serif; letter-spacing: 1px;'>{grade}</div>
            <div style='font-size: 1.2rem; color:#cbd5e1;'>
                Successful Mitigations: <b>{score}</b> / <b>{total}</b>
            </div>
            <br>
            <div class='score-badge'>{pct}% SECURE</div>
        </div>
        """, unsafe_allow_html=True)

        # Progress bar showing percentage
        st.progress(pct / 100)
        st.markdown("<br>", unsafe_allow_html=True)

        # Encouragement message for low scorers
        if pct < 80:
            st.warning(
                "💡 Mitigation Advice: Read the sidebar security tips and "
                "chat with MobileGuard to patch critical knowledge gaps!"
            )

        # Restart button — resets ALL quiz state
        if st.button("🔄 Initiate New Audit", use_container_width=True):
            st.session_state.quiz_index     = 0
            st.session_state.quiz_score     = 0
            st.session_state.quiz_started   = False
            st.session_state.quiz_done      = False
            st.session_state.quiz_answered  = False
            st.session_state.quiz_selected  = None
            # New random set of questions
            st.session_state.quiz_questions = random.sample(
                QUIZ_QUESTIONS, min(7, len(QUIZ_QUESTIONS))
            )
            st.rerun()
        show_html('</div></div>')

    # ── STATE 1 & 2: QUESTION SCREEN ──
    else:
        current_q = qs[idx]   # Get current question dict

        show_html(
            f'<p class="quiz-progress-label">AUDIT THREAT VECTOR {idx + 1} OF {len(qs)}</p>'
        )
        st.progress((idx + 1) / len(qs))
        st.markdown("<br>", unsafe_allow_html=True)

        # Render question inside a cyber card
        st.markdown(f"""
        <div class="cyber-card">
            <div class="terminal-title">THREAT INTEL SCENARIO</div>
            <div style="font-size: 1.15rem; font-weight: 500; color: #f1f5f9; line-height: 1.5;">{current_q['question']}</div>
        </div>
        """, unsafe_allow_html=True)

        answered = st.session_state.quiz_answered
        selected = st.session_state.quiz_selected

        # ── Display 4 Option Buttons ──
        for i, option in enumerate(current_q["options"]):
            label = option

            # After answering: add ✅ or ❌ prefix
            if answered:
                if i == current_q["answer"]:
                    label = "✅ [CORRECT] " + option
                elif i == selected:
                    label = "❌ [INCORRECT] " + option

            # disabled=True after answering prevents re-clicking
            if st.button(
                label,
                key=f"opt_{idx}_{i}",
                disabled=answered,
                use_container_width=True
            ):
                # Record the user's choice
                st.session_state.quiz_selected = i
                st.session_state.quiz_answered = True
                # Award point if correct
                if i == current_q["answer"]:
                    st.session_state.quiz_score += 1
                st.rerun()

        # ── Show Result After Answering ──
        if answered:
            st.markdown("<br>", unsafe_allow_html=True)
            if selected == current_q["answer"]:
                st.success(f"🎉 **Correct Mitigation!** {current_q['explanation']}")
            else:
                st.error(f"❌ **Threat Successful!** {current_q['explanation']}")

            st.markdown("<br>", unsafe_allow_html=True)

            # Next Question button
            if st.button("Proceed to Next Threat Vector ➡️", use_container_width=True):
                if idx + 1 >= len(qs):
                    # All questions done — go to results
                    st.session_state.quiz_done = True
                else:
                    # Move to next question
                    st.session_state.quiz_index    += 1
                    st.session_state.quiz_answered  = False
                    st.session_state.quiz_selected  = None
                st.rerun()

    show_html('</div></div>')


# ════════════════════════════════════════
#  SECTION 8: PAGE — 🔍 APP PERMISSION CHECKER
# ════════════════════════════════════════
elif "🔍 App Permission Checker" in page:

    show_html('<div class="page-shell">')
    page_hero(
        "🔍",
        "App Permission Checker",
        "Analyse which app permissions are safe, suspicious, or dangerous.",
        ["12 Permissions", "Risk Levels", "Action Advice"],
    )
    show_html("""
    <div class="welcome-card" style="margin-bottom:20px;">
        <p class="welcome-card-title">🕵️ HOW IT WORKS</p>
        <p>Enter the app name and select every permission it requests.
        MobileGuard categorises each one as high, medium, or low risk.</p>
    </div>
    <div class="page-body">
    <p class="section-heading">📋 APP DETAILS</p>
    """)

    # ── Permission Database ──
    # Format: "Display Name": ("risk_level", "explanation")
    PERMISSIONS = {
        "📍 Location (Fine / GPS)": (
            "high",
            "Precise GPS is only needed for maps/navigation apps. "
            "A flashlight or game app should NEVER need your exact location."
        ),
        "🎙️ Microphone": (
            "high",
            "Only calling, recording, or voice-command apps need microphone. "
            "Very suspicious if a utility or gaming app requests this."
        ),
        "📨 SMS / Messages": (
            "high",
            "MOST DANGEROUS — apps with SMS access can read your OTPs and "
            "2FA codes, giving hackers full account access."
        ),
        "📒 Contacts": (
            "high",
            "Spyware commonly harvests contact lists. "
            "Only messaging or dialer apps genuinely need contacts."
        ),
        "📞 Call Logs": (
            "high",
            "Exposes your full call history. No game, utility, or "
            "shopping app should ever request call log access."
        ),
        "🪪 Device ID / Phone Number": (
            "high",
            "Allows permanent tracking of your device across apps. "
            "Very suspicious when requested by games or free utilities."
        ),
        "📷 Camera": (
            "medium",
            "Needed for photo/video apps. Suspicious if a keyboard, "
            "calculator, or simple utility requests camera access."
        ),
        "🗂️ Storage / Files": (
            "medium",
            "Common but review carefully — does this app truly need to "
            "read and write your personal files?"
        ),
        "📡 Wi-Fi / Network State": (
            "low",
            "Generally harmless — most apps check for internet connectivity "
            "before loading content."
        ),
        "🔔 Notifications": (
            "low",
            "Normal for most apps. Only disable for apps that send excessive spam."
        ),
        "🔋 Battery / Device Info": (
            "low",
            "Mostly harmless — used by performance optimization or utility apps."
        ),
        "🌐 Internet Access": (
            "low",
            "Almost every app needs internet. Alone, this is not concerning."
        ),
    }

    # ── Input: App Name ──
    app_name = st.text_input(
        "📦 Enter App Name:",
        placeholder="e.g. FlashlightPro, FreeVPN, GameApp..."
    )

    # ── Input: Permission Selection ──
    selected_perms = st.multiselect(
        "☑️ Select all permissions this app requests:",
        options=list(PERMISSIONS.keys()),
        help="Select every permission shown in the app's install screen"
    )

    if st.button("🔍 Analyse Permissions", use_container_width=True):

        # Validation: ensure both fields are filled
        if not app_name.strip():
            st.warning("⚠️ Please enter the app name first.")
        elif not selected_perms:
            st.warning("⚠️ Please select at least one permission to analyse.")
        else:
            # Categorize selected permissions by risk level
            high_risk   = [(p, PERMISSIONS[p][1]) for p in selected_perms
                           if PERMISSIONS[p][0] == "high"]
            medium_risk = [(p, PERMISSIONS[p][1]) for p in selected_perms
                           if PERMISSIONS[p][0] == "medium"]
            low_risk    = [(p, PERMISSIONS[p][1]) for p in selected_perms
                           if PERMISSIONS[p][0] == "low"]

            st.markdown("---")
            st.markdown(f"""
            <div class="cyber-card">
                <div class="terminal-title">PERMANENT DEFENSE ANALYSIS FOR: {app_name.upper()}</div>
            </div>
            """, unsafe_allow_html=True)

            # ── Show HIGH RISK results ──
            if high_risk:
                st.markdown(f'<div style="margin-bottom:10px;"><span class="risk-pill-high">🚨 CRITICAL THREAT VECTORS ({len(high_risk)})</span></div>', unsafe_allow_html=True)
                for perm, reason in high_risk:
                    st.markdown(f"""
                    <div style="background: rgba(244, 63, 94, 0.08); padding: 12px 18px; border-radius: 8px; border-left: 3px solid #f43f5e; margin-bottom: 10px;">
                        <b style="color: #f43f5e;">{perm}</b><br>
                        <span style="color: #cbd5e1; font-size: 14px;">{reason}</span>
                    </div>
                    """, unsafe_allow_html=True)

            # ── Show MEDIUM RISK results ──
            if medium_risk:
                st.markdown(f'<div style="margin-bottom:10px;"><span class="risk-pill-medium">⚠️ WARNING THREAT VECTORS ({len(medium_risk)})</span></div>', unsafe_allow_html=True)
                for perm, reason in medium_risk:
                    st.markdown(f"""
                    <div style="background: rgba(245, 158, 11, 0.05); padding: 12px 18px; border-radius: 8px; border-left: 3px solid #f59e0b; margin-bottom: 10px;">
                        <b style="color: #f59e0b;">{perm}</b><br>
                        <span style="color: #cbd5e1; font-size: 14px;">{reason}</span>
                    </div>
                    """, unsafe_allow_html=True)

            # ── Show LOW RISK results ──
            if low_risk:
                st.markdown(f'<div style="margin-bottom:10px;"><span class="risk-pill-low">✅ STABLE CHANNELS ({len(low_risk)})</span></div>', unsafe_allow_html=True)
                low_perms_html = "".join([f"<li style='color: #10b981; font-size:14px;'>{perm}</li>" for perm, _ in low_risk])
                st.markdown(f"""
                <div style="background: rgba(16, 185, 129, 0.05); padding: 12px 18px; border-radius: 8px; border-left: 3px solid #10b981; margin-bottom: 10px;">
                    <ul style="margin: 0; padding-left: 20px;">{low_perms_html}</ul>
                </div>
                """, unsafe_allow_html=True)

            # ── Final Recommendation ──
            st.markdown("<br>", unsafe_allow_html=True)
            if high_risk:
                st.markdown(f"""
                <div class="stAlert" style="border: 1px solid #f43f5e !important; padding: 15px; border-radius: 10px; background: rgba(244, 63, 94, 0.08);">
                    <b style="color: #f43f5e; font-size: 16px;">🛑 ACTION REQUIRED: INSTALLATION BLOCKED</b><br>
                    <span style="color: #cbd5e1;">Do NOT install <b>'{app_name}'</b>. If already installed, immediately revoke all high-risk permissions under <i>Settings → Apps → {app_name} → Permissions</i> to prevent potential data exploitation.</span>
                </div>
                """, unsafe_allow_html=True)
            elif medium_risk:
                st.markdown(f"""
                <div class="stAlert" style="border: 1px solid #f59e0b !important; padding: 15px; border-radius: 10px; background: rgba(245, 158, 11, 0.05);">
                    <b style="color: #f59e0b; font-size: 16px;">⚠️ WARNING: PROCEED WITH CAUTION</b><br>
                    <span style="color: #cbd5e1;">Install <b>'{app_name}'</b> only if you verified the developer profile. Manually deny access to any permissions that do not align with core app utilities.</span>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div class="stAlert" style="border: 1px solid #10b981 !important; padding: 15px; border-radius: 10px; background: rgba(16, 185, 129, 0.05);">
                    <b style="color: #10b981; font-size: 16px;">✅ ANALYSIS SECURE: DEPLOYMENT STABLE</b><br>
                    <span style="color: #cbd5e1;"><b>'{app_name}'</b> requests standard safe permissions and is verified for installation. Always maintain updates from official repositories.</span>
                </div>
                """, unsafe_allow_html=True)

    show_html('</div></div>')


# ════════════════════════════════════════
#  SECTION 9: PAGE — 💪 PIN STRENGTH CHECKER
# ════════════════════════════════════════
elif "💪 PIN Strength Checker" in page:

    show_html('<div class="page-shell">')
    page_hero(
        "💪",
        "PIN / Password Strength",
        "Check how strong your mobile lock screen PIN or password is.",
        ["6 Criteria", "Weak PIN Blocklist", "Local Check"],
    )
    show_html("""
    <div class="welcome-card" style="margin-bottom:20px;">
        <p class="welcome-card-title">🔒 PRIVACY NOTICE</p>
        <p>Your PIN or password is never stored, sent, or logged.
        All checking happens locally in your browser session only.</p>
    </div>
    <div class="page-body">
    <p class="section-heading">🔑 ENTER CREDENTIAL</p>
    """)

    pin_input = st.text_input(
        "PIN or password",
        type="password",
        placeholder="e.g. MySecure@Phone2024",
        label_visibility="collapsed",
    )

    def check_pin_strength(p):
        """
        Evaluates the strength of a PIN or password.

        Checks 6 criteria, each worth 1 point:
        1. Length >= 8
        2. Length >= 12
        3. Has uppercase letter
        4. Has lowercase letter
        5. Has digit
        6. Has special character

        Returns: (score: int, feedback: list of strings)
        """
        score    = 0
        feedback = []

        # Criterion 1: Minimum length
        if len(p) >= 8:
            score += 1
        else:
            feedback.append("❌ Too short — use at least 8 characters")

        # Criterion 2: Good length
        if len(p) >= 12:
            score += 1
        else:
            feedback.append("⚠️ Longer is better — aim for 12+ characters")

        # Criterion 3: Uppercase letter
        if re.search(r"[A-Z]", p):
            score += 1
        else:
            feedback.append("❌ Add at least one UPPERCASE letter (A–Z)")

        # Criterion 4: Lowercase letter
        if re.search(r"[a-z]", p):
            score += 1
        else:
            feedback.append("❌ Add at least one lowercase letter (a–z)")

        # Criterion 5: Number
        if re.search(r"\d", p):
            score += 1
        else:
            feedback.append("❌ Add at least one number (0–9)")

        # Criterion 6: Special character
        if re.search(r'[!@#$%^&*()\-_=+\[\]{};:\'",.<>?/\\|`~]', p):
            score += 1
        else:
            feedback.append("❌ Add at least one special character (!@#$...)")

        # ── Blacklist common weak PINs ──
        WEAK_PINS = [
            "0000", "1111", "2222", "3333", "4444",
            "5555", "6666", "7777", "8888", "9999",
            "1234", "4321", "0123", "123456", "654321",
            "111111", "000000", "password", "pass123",
        ]
        if p.lower() in WEAK_PINS:
            score = 0   # Override score to zero
            feedback.insert(
                0,
                "🚨 This is one of the most commonly used PINs! "
                "Change it immediately — hackers try these first."
            )

        return score, feedback

    # ── Strength Level Definitions ──
    # (min_score, label, hex_color)
    STRENGTH_LEVELS = [
        (6, "Very Strong", "#10b981"),
        (5, "Strong",      "#22d3ee"),
        (4, "Good",        "#6366f1"),
        (3, "Fair",        "#f59e0b"),
        (2, "Weak",        "#f97316"),
        (1, "Very Weak",   "#f43f5e"),
    ]

    # ── Run checker only when input exists ──
    if pin_input:
        score, feedback = check_pin_strength(pin_input)

        # Determine label and color
        level_label = "Very Weak"
        level_color = "#f43f5e"
        for min_score, label, color in STRENGTH_LEVELS:
            if score >= min_score:
                level_label = label
                level_color = color
                break

        bar_pct = int((score / 6) * 100)   # Convert score to percentage

        # ── Strength Bar (custom HTML) ──
        st.markdown(f"""
        <div class="cyber-card">
            <div class="terminal-title">CRYPTOGRAPHIC STRENGTH EVALUATION</div>
            <div style='margin: 10px 0;'>
                <b style='color:#cbd5e1;'>Entropy Index:</b>
                <span style='color:{level_color};
                             font-size:1.3rem;
                             font-weight:700;
                             margin-left:10px;
                             font-family: "Orbitron", sans-serif;
                             text-shadow: 0 0 10px {level_color}44;'>{level_label.upper()}</span>
                <div style='background:rgba(15, 23, 42, 0.8);
                            border: 1px solid rgba(255,255,255,0.05);
                            border-radius:8px;
                            height:14px;
                            margin-top:10px;
                            overflow:hidden;'>
                    <div style='width:{bar_pct}%;
                                background: linear-gradient(90deg,
                                    {level_color}aa, {level_color});
                                height:14px;
                                border-radius:8px;
                                transition: width 0.5s ease;'>
                    </div>
                </div>
                <small style='color:#94a3b8; display:block; margin-top:8px;'>Score: {score} / 6 security criteria met</small>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # ── Feedback / Suggestions ──
        if feedback:
            st.markdown(f"""
            <div class="cyber-card">
                <div class="terminal-title" style="color: #f43f5e;">⚠️ SUGGESTED SECURITY PATCHES</div>
            </div>
            """, unsafe_allow_html=True)
            for item in feedback:
                st.markdown(f"- {item}")
        else:
            st.markdown(f"""
            <div class="stAlert" style="border: 1px solid #10b981 !important; padding: 15px; border-radius: 10px; background: rgba(16, 185, 129, 0.08);">
                <b style="color: #10b981; font-size: 16px;">🏆 CRYPTOGRAPHIC SECURITY VERIFIED</b><br>
                <span style="color: #cbd5e1;">Perfect! Your passcode meets all 6 threat mitigation standards. Excellent job securing your terminal!</span>
            </div>
            """, unsafe_allow_html=True)

        st.divider()

    # ── Mobile PIN Security Tips (always shown) ──
    st.markdown(f"""
    <div class="cyber-card">
        <div class="terminal-title">🛡️ MOBILE PROTECTION PROTOCOLS</div>
    </div>
    """, unsafe_allow_html=True)
    
    pin_tips = [
        "Never use your date of birth, phone number, or repeated digits as your PIN.",
        "Use a 6-digit PIN minimum — never use a 4-digit PIN for important accounts.",
        "Enable biometric lock (fingerprint or face ID) as a convenience layer on top of PIN.",
        "Set your phone to auto-lock after 30 seconds of inactivity.",
        "Never share your PIN with anyone — including friends, family, or 'tech support'.",
        "Change your PIN every 3–6 months as a good security habit.",
        "Use a different PIN for your phone lock and banking apps.",
    ]
    for tip in pin_tips:
        show_html(
            f'<div class="sb-tip-item" style="margin-bottom:8px;">'
            f'<span class="sb-tip-icon">✅</span>'
            f'<p class="sb-tip-text">{html_lib.escape(tip)}</p></div>'
        )

    show_html('</div></div>')
