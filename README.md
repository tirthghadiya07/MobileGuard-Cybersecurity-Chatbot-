# 📱 MobileGuard — AI-Powered Mobile Security Chatbot

<div align="center">

![MobileGuard Banner](screenshots/CB1.png)

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=for-the-badge)]()

**An AI-powered cybersecurity chatbot that educates users about smartphone & mobile security threats.**

[🚀 Features](#-features) • [📸 Screenshots](#-screenshots) • [⚙️ Installation](#️-installation) • [💬 Usage](#-usage) • [🛡️ Topics](#️-cybersecurity-topics-covered)

</div>

---

## 🌟 About The Project

**MobileGuard** is a rule-based AI chatbot built with **Python + Streamlit** that acts as a personal mobile cybersecurity assistant. It helps everyday smartphone users understand real-world threats — from SIM swap attacks to dangerous app permissions — and provides actionable protection advice.

> 👤 **Developer:** Tirth Ghadiya
> 🏫 **Department:** Cybersecurity
> 🎯 **Focus:** Smartphone & iOS Security

---

## ✨ Features

| Module | Description |
|--------|-------------|
| 💬 **AI Chatbot** | 19 mobile security topics with keyword-scoring response engine |
| 🧠 **Security Quiz** | 10 questions, 7 shown randomly per session with instant feedback |
| 🔍 **App Permission Checker** | Analyses 12 permissions and rates them HIGH / MEDIUM / LOW risk |
| 💪 **PIN Strength Checker** | 6-criteria scoring with visual strength bar and weak PIN blacklist |
| ⚡ **Security Intel Sidebar** | 8 live security tips always visible across all modules |
| 🌙 **Dark Cyber Theme** | Professional dark navy UI with electric blue accents |

---

## 📸 Screenshots

### 💬 Chatbot — Welcome Screen
![Chatbot Welcome](screenshots/CB1.png)

### 💬 Chatbot — Topics & Responses
![Chatbot Response](screenshots/CB2.png)

### 🧠 Security Quiz
![Security Quiz](screenshots/SQ.png)

### 🔍 App Permission Checker
![Permission Checker](screenshots/APC.png)

### 💪 PIN Strength Checker
![PIN Checker](screenshots/PS.png)

---

## ⚙️ Installation

### Prerequisites
- Python 3.x installed → [python.org](https://python.org)
- pip package manager

### Steps

```bash
# 1. Clone the repository
git clone https://github.com/tirthghadiya07/MobileGuard-Cybersecurity-Chatbot.git

# 2. Navigate into the project folder
cd MobileGuard-Cybersecurity-Chatbot

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the chatbot
streamlit run app.py
```

The app opens automatically at **http://localhost:8501** 🚀

---

## 💬 Usage

Once the app is running:

1. **Chatbot** — Type any mobile security question (e.g. *"What is a SIM swap attack?"*)
2. **Security Quiz** — Click `🚀 Start Security Audit` to test your knowledge
3. **App Permission Checker** — Enter an app name, select its permissions, click Analyse
4. **PIN Checker** — Enter your phone PIN/password to check its strength

---

## 🛡️ Cybersecurity Topics Covered

```
📱 Android Security          🍎 iOS / iPhone Security
🦠 Mobile Malware Detection  📲 SIM Swap Attacks
🔑 2FA & OTP Security        🔏 PIN & Password Security
📡 Public Wi-Fi Dangers      🎣 Smishing (SMS Phishing)
⚠️  Dangerous App Permissions 🔵 Bluetooth & NFC Safety
☁️  Data Backup Strategies    🚨 Stolen Phone Recovery
🌐 VPN on Mobile             🔄 Software Update Importance
👁️  Spyware Detection
```

---

## 🧠 How The Chatbot Works

```
User Input
    ↓
Convert to lowercase
    ↓
Check: Greeting? Thanks? Help?
    ↓
Keyword Scoring Engine
    (For each of 19 knowledge base entries:
     count how many keywords match user input)
    ↓
Return highest-scoring response
    ↓
If score = 0 → Random helpful fallback message
```

**Why Keyword Scoring?**
More flexible than `if/elif` chains — finds the BEST match by scoring all entries, not just the first match.

> 💡 Claude AI was used to help build the keyword scoring logic and chatbot architecture.

---

## 📁 Project Structure

```
MobileGuard-Cybersecurity-Chatbot/
│
├── app.py              ← Main Streamlit UI (4 pages + dark CSS + routing)
├── chatbot.py          ← Knowledge base (19 topics) + response engine
├── quiz.py             ← 10 quiz questions with explanations
├── requirements.txt    ← Python dependencies
├── README.md           ← This file
│
└── screenshots/
    ├── CB1.png         ← Chatbot welcome screen
    ├── CB2.png         ← Chatbot topics list
    ├── CB3.png         ← Chatbot in conversation
    ├── CB4.png         ← Chatbot response example
    ├── SQ.png          ← Security Quiz
    ├── APC.png         ← App Permission Checker
    ├── PS.png          ← PIN Strength Checker
    └── SI.png          ← Security Intel sidebar
```

---

## 🛠️ Built With

| Technology | Purpose |
|-----------|---------|
| **Python 3.x** | Core programming language |
| **Streamlit** | Web UI framework |
| **re (Regex)** | PIN pattern matching |
| **random** | Quiz shuffling + fallback rotation |

---

## 👤 Author

**Tirth Ghadiya**
- 🏫 Department: Cybersecurity
- 🔗 GitHub: [tirthghadiya07](https://github.com/tirthghadiya07)

---

<div align="center">

⭐ **If you found this project helpful, please give it a star!** ⭐

*Built with 💙 using Python + Streamlit*

</div>
