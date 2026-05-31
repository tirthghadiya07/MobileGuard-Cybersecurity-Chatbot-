# ============================================================
#  quiz.py — Mobile Security Quiz Questions
#  Student   : Tirth
#  Topic     : Mobile Security Chatbot
#  Subject   : AICS Assignment 3 | 2025-26
# ============================================================

QUIZ_QUESTIONS = [

    # ── QUESTION 1 ────────────────────────────────────────
    {
        "question": (
            "What is the SAFEST place to download apps on your Android phone?"
        ),
        "options": [
            "Any website that offers an APK file for free",
            "Google Play Store — the official Android app store",
            "Third-party app stores like APKPure or Aptoide",
            "WhatsApp download links shared by friends",
        ],
        "answer": 1,
        # Index 1 = "Google Play Store" is correct
        "explanation": (
            "Google Play Store scans every app using Google Play Protect "
            "before and after installation. APK files from unknown websites "
            "or third-party stores have NO security scanning and commonly "
            "contain malware, spyware, or ransomware."
        ),
    },

    # ── QUESTION 2 ────────────────────────────────────────
    {
        "question": (
            "Which type of Two-Factor Authentication (2FA) is the MOST secure "
            "for protecting your mobile accounts?"
        ),
        "options": [
            "SMS OTP — a one-time code sent via text message",
            "Email OTP — a one-time code sent to your email",
            "Authenticator App — like Google Authenticator or Authy",
            "Security Question — like 'What is your pet's name?'",
        ],
        "answer": 2,
        # Index 2 = "Authenticator App" is correct
        "explanation": (
            "Authenticator Apps generate time-based one-time passwords "
            "(TOTP) completely offline. SMS OTP is the weakest because "
            "attackers can perform SIM swap attacks to intercept your text "
            "messages. Security questions are easily guessed from social media."
        ),
    },

    # ── QUESTION 3 ────────────────────────────────────────
    {
        "question": (
            "You receive this SMS: 'Your bank account is LOCKED! "
            "Verify immediately: bit.ly/secure-bank'. What should you do?"
        ),
        "options": [
            "Click the link immediately to unlock your account",
            "Reply to the SMS with your account number to verify",
            "Ignore and delete it — this is a smishing (SMS phishing) scam",
            "Forward it to all your contacts to warn them",
        ],
        "answer": 2,
        # Index 2 = "Ignore and delete" is correct
        "explanation": (
            "This is a classic smishing attack — phishing via SMS. "
            "Legitimate banks NEVER send links asking for credentials "
            "via text message. The urgency and suspicious shortened URL "
            "are major red flags. Always go directly to your bank's "
            "official app or website instead."
        ),
    },

    # ── QUESTION 4 ────────────────────────────────────────
    {
        "question": (
            "A free flashlight app requests the following permissions: "
            "Camera, Contacts, SMS Access, and Microphone. What should you do?"
        ),
        "options": [
            "Accept all permissions — apps always need full access to work",
            "Accept only Camera — a flashlight needs the camera flash",
            "Deny all permissions and uninstall — a flashlight needs NONE of these",
            "Accept Microphone only since it seems the least risky",
        ],
        "answer": 2,
        # Index 2 = "Deny all and uninstall" is correct
        "explanation": (
            "A legitimate flashlight app only needs camera/flash hardware access "
            "to function. Requesting Contacts, SMS, and Microphone is a major "
            "red flag — this is likely spyware disguised as a utility. "
            "SMS access can steal your OTPs, microphone can record conversations, "
            "and contacts can be harvested and sold. Always uninstall such apps."
        ),
    },

    # ── QUESTION 5 ────────────────────────────────────────
    {
        "question": (
            "What exactly happens during a SIM Swap attack on your mobile phone?"
        ),
        "options": [
            "The attacker physically steals your SIM card from your phone",
            "Your phone's SIM card gets damaged by a virus",
            "The attacker tricks your carrier into transferring your number "
            "to their SIM so they receive your SMS OTPs",
            "The attacker swaps your phone with an identical one",
        ],
        "answer": 2,
        # Index 2 = "Tricks carrier to transfer number" is correct
        "explanation": (
            "In a SIM swap attack, the attacker calls your mobile carrier "
            "and uses personal information (from social media or data breaches) "
            "to impersonate you. They convince the carrier to port your number "
            "to their SIM. Once successful, they receive all your SMS messages "
            "including banking OTPs and 2FA codes — giving full account access."
        ),
    },

    # ── QUESTION 6 ────────────────────────────────────────
    {
        "question": (
            "Which of the following is the STRONGEST mobile lock screen PIN "
            "or password?"
        ),
        "options": [
            "1234 — easy to remember and type quickly",
            "Your birth year — personal and easy to recall",
            "0000 — simple and fast to unlock",
            "A random alphanumeric password like T!rth@2024",
        ],
        "answer": 3,
        # Index 3 = "Random alphanumeric password" is correct
        "explanation": (
            "Random alphanumeric passwords with special characters are "
            "exponentially harder to crack than simple numeric PINs. "
            "PINs like 1234, 0000, and birth years are the FIRST combinations "
            "attackers try — they appear on every hacker's list of most "
            "commonly used PINs. A passphrase like 'T!rth@Mob!le24' has "
            "uppercase, lowercase, numbers, and special characters."
        ),
    },

    # ── QUESTION 7 ────────────────────────────────────────
    {
        "question": (
            "You are at a coffee shop and need to check your bank account. "
            "What is the SAFEST approach?"
        ),
        "options": [
            "Connect to the free 'CafeWifi' and open your banking app",
            "Use your mobile data (4G/5G) or a VPN on the cafe's Wi-Fi",
            "Ask the cafe staff for the Wi-Fi password — it's more secure",
            "Use the cafe's Wi-Fi but clear your browser history afterward",
        ],
        "answer": 1,
        # Index 1 = "Use mobile data or VPN" is correct
        "explanation": (
            "Public Wi-Fi networks are unencrypted and vulnerable to "
            "Man-in-the-Middle (MITM) attacks where hackers intercept your "
            "traffic. Your mobile data (4G/5G) is encrypted by the carrier "
            "and far safer. If you must use Wi-Fi, always activate a VPN "
            "first — it encrypts all traffic so even the cafe network owner "
            "cannot see what you're doing."
        ),
    },

    # ── QUESTION 8 ────────────────────────────────────────
    {
        "question": (
            "Your Android phone is stolen. What should be your FIRST action?"
        ),
        "options": [
            "Wait 24 hours to see if the thief returns the phone",
            "Buy a new phone immediately and forget about the old one",
            "Go to android.com/find and remotely lock or erase the device",
            "Post about the theft on social media to warn others",
        ],
        "answer": 2,
        # Index 2 = "Use Find My Device remotely" is correct
        "explanation": (
            "Every second counts when a phone is stolen. Go immediately to "
            "android.com/find (or icloud.com/find for iPhone) and use "
            "Lost Mode to lock the device with a message, or Erase Device "
            "to wipe all personal data remotely. After securing the device, "
            "change all passwords, block the SIM with your carrier, and "
            "file a police report with your IMEI number (dial *#06# to find it)."
        ),
    },

    # ── QUESTION 9 ────────────────────────────────────────
    {
        "question": (
            "What is the PRIMARY security risk of jailbreaking an iPhone "
            "or rooting an Android phone?"
        ),
        "options": [
            "The phone battery drains faster than normal",
            "It removes the manufacturer's security protections, "
            "making the phone much more vulnerable to malware",
            "The phone screen brightness decreases permanently",
            "It improves security by giving you full system control",
        ],
        "answer": 1,
        # Index 1 = "Removes security protections" is correct
        "explanation": (
            "Jailbreaking (iOS) and rooting (Android) bypass the operating "
            "system's security sandbox — the protective barrier between apps "
            "and critical system files. Once removed, malicious apps can access "
            "system files freely, automatic security updates stop working, "
            "banking apps detect the compromise and refuse to run, and your "
            "device becomes a prime target for hackers. The risks far outweigh "
            "any customisation benefits."
        ),
    },

    # ── QUESTION 10 ───────────────────────────────────────
    {
        "question": (
            "How soon should you install a security update notification "
            "on your mobile phone?"
        ),
        "options": [
            "Only when the phone starts having problems or slowing down",
            "Every few years when buying a new phone",
            "As soon as possible — within 24 to 48 hours of release",
            "Never — software updates can break existing apps",
        ],
        "answer": 2,
        # Index 2 = "Within 24–48 hours" is correct
        "explanation": (
            "Security updates patch specific, known vulnerabilities. "
            "Once a patch is released publicly, hackers immediately reverse-engineer "
            "it to find the exact weakness it fixes — then target all unpatched "
            "devices. The Pegasus spyware (2021) exploited an iOS bug that Apple "
            "patched quickly, but millions of unupdated iPhones remained vulnerable "
            "for months. Always update within 24–48 hours of any security patch release."
        ),
    },

]


# ============================================================
#  QUICK REFERENCE — Correct Answers
#  (for testing and viva preparation)
#
#  Q1  → Answer: 1 (Google Play Store)
#  Q2  → Answer: 2 (Authenticator App)
#  Q3  → Answer: 2 (Ignore — smishing scam)
#  Q4  → Answer: 2 (Deny all — uninstall)
#  Q5  → Answer: 2 (Carrier tricks number transfer)
#  Q6  → Answer: 3 (Random alphanumeric password)
#  Q7  → Answer: 1 (Mobile data or VPN)
#  Q8  → Answer: 2 (android.com/find)
#  Q9  → Answer: 1 (Removes security protections)
#  Q10 → Answer: 2 (Within 24–48 hours)
# ============================================================

#
#  HOW THIS FILE WORKS:
#  ─────────────────────
#  This file contains a list called QUIZ_QUESTIONS.
#  Each question is a Python dictionary with 4 keys:
#
#  "question"    → The question text shown to the user
#  "options"     → List of 4 answer choices (strings)
#  "answer"      → Index (0–3) of the CORRECT option
#  "explanation" → Shown after answering, teaches the concept
#
#  In app.py, 7 random questions are picked using:
#      random.sample(QUIZ_QUESTIONS, 7)
#  This means every quiz session is slightly different!
#
#  QUESTION TOPICS COVERED:
#  ─────────────────────────
#  Q1  — Safe app downloads
#  Q2  — Two-factor authentication (2FA) methods
#  Q3  — Smishing / SMS phishing detection
#  Q4  — App permission red flags
#  Q5  — SIM swap attack
#  Q6  — Strong mobile PIN
#  Q7  — Public Wi-Fi safety
#  Q8  — Stolen phone procedure
#  Q9  — Jailbreaking / rooting risks
#  Q10 — Software update importance
# ============================================================