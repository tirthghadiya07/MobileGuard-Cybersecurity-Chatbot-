# ============================================================
#  chatbot.py — MobileGuard Knowledge Base & Response Logic
#  Student   : Tirth
#  Topic     : Mobile Security Chatbot
#  Subject   : AICS Assignment 3 | 2025-26
# ============================================================

import random   # Used for selecting random fallback messages


# ════════════════════════════════════════════════════════════
#  SECTION 1: QUICK SIDEBAR TIPS
#  These 8 tips are displayed in the sidebar on every page.
#  Imported in app.py as: from chatbot import QUICK_TIPS
# ════════════════════════════════════════════════════════════

QUICK_TIPS = [
    "Update your phone OS regularly.",
    "Use a 6+ digit PIN or biometrics.",
    "Avoid unknown public Wi-Fi networks.",
    "Download apps from official stores only.",
    "Enable 2FA on all important accounts.",
    "Back up your phone data every week.",
    "Turn off Bluetooth when not in use.",
    "Review app permissions every 3 months.",
]


# ════════════════════════════════════════════════════════════
#  SECTION 2: FALLBACK MESSAGES
#  Shown when no keyword match is found.
#  random.choice() picks one randomly each time.
# ════════════════════════════════════════════════════════════

FALLBACK_RESPONSES = [
    (
        "🤔 I'm not sure about that specific topic. Try asking about:\n"
        "• Android or iOS security\n"
        "• App permissions\n"
        "• Public Wi-Fi safety\n"
        "• Mobile malware detection\n"
        "• SIM swap or 2FA\n"
        "• Lost or stolen phone"
    ),
    (
        "📱 That's a bit outside my mobile security expertise!\n"
        "You can ask me about:\n"
        "• Securing your Android or iPhone\n"
        "• Bluetooth and NFC safety\n"
        "• PIN and password strength\n"
        "• VPN usage on mobile\n"
        "• Phishing SMS (smishing)"
    ),
    (
        "🛡️ I didn't quite understand that question.\n"
        "Try rephrasing it, or ask about:\n"
        "• Mobile malware signs\n"
        "• Safe app downloads\n"
        "• Data backup strategies\n"
        "• What to do if your phone is stolen\n"
        "• Two-factor authentication (2FA)"
    ),
]


# ════════════════════════════════════════════════════════════
#  SECTION 3: MAIN KNOWLEDGE BASE
#
#  18 topics across 8 categories:
#  ─────────────────────────────
#  CAT 1 — Android Security     (Topics 1–2)
#  CAT 2 — iOS Security         (Topics 3–4)
#  CAT 3 — Mobile Malware       (Topics 5–6)
#  CAT 4 — OTP & Auth Fraud     (Topics 7–8)
#  CAT 5 — Passwords & PINs     (Topics 9–10)
#  CAT 6 — Safe Browsing        (Topics 11–12)
#  CAT 7 — Mobile Privacy       (Topics 13–14)
#  CAT 8 — Backup & Recovery    (Topics 15–18)
# ════════════════════════════════════════════════════════════

KNOWLEDGE_BASE = [

    # ─────────────────────────────────────────
    #  CATEGORY 1: ANDROID SECURITY
    # ─────────────────────────────────────────

    {
        "category": "Android Security",
        "keywords": [
            "secure", "android", "phone", "basic", "start",
            "tips", "general", "protect", "android phone",
            "smartphone", "safety", "safe"
        ],
        "response": (
            "🔐 Top Ways to Secure Your Android Phone:\n\n"
            "1. Keep Android OS updated:\n"
            "   Settings → System → System Update\n\n"
            "2. Download apps ONLY from Google Play Store.\n"
            "   Never install APK files from unknown websites.\n\n"
            "3. Enable Google Play Protect:\n"
            "   Play Store → Menu → Play Protect → Turn ON\n"
            "   It scans all apps daily for malware.\n\n"
            "4. Use a strong lock screen:\n"
            "   6-digit PIN + fingerprint lock.\n\n"
            "5. Enable Find My Device:\n"
            "   Settings → Google → Find My Device → ON\n"
            "   Lets you remotely wipe phone if stolen.\n\n"
            "6. Turn off Bluetooth and Wi-Fi when not in use.\n\n"
            "7. Encrypt your storage:\n"
            "   Settings → Security → Encryption & Credentials"
        ),
    },

    {
        "category": "Android Security",
        "keywords": [
            "play protect", "google play", "play store", "google protect",
            "malware scan", "android scan", "app scan"
        ],
        "response": (
            "🛡️ What is Google Play Protect?\n\n"
            "Google Play Protect is Android's built-in security scanner.\n"
            "It automatically scans ALL installed apps — even those\n"
            "downloaded from outside the Play Store.\n\n"
            "✅ What it does:\n"
            "• Runs daily background scans on all apps\n"
            "• Warns you about harmful or suspicious apps\n"
            "• Can disable dangerous apps automatically\n"
            "• Checks apps before you install them\n\n"
            "🔧 How to enable it:\n"
            "   Google Play Store → Menu (☰) →\n"
            "   Play Protect → Turn ON\n\n"
            "⚠️ If it finds a threat:\n"
            "   Immediately uninstall the flagged app!"
        ),
    },

    # ─────────────────────────────────────────
    #  CATEGORY 2: iOS SECURITY
    # ─────────────────────────────────────────

    {
        "category": "iOS Security",
        "keywords": [
            "ios", "iphone", "apple", "ipad", "secure iphone",
            "apple security", "ios security", "iphone safety",
            "iphone security", "apple phone", "how to secure iphone",
            "iphone tips", "iphone safe", "secure my iphone",
            "my iphone", "my apple", "protect iphone", "iphone protect"
        ],
        "response": (
            "🍎 iOS / iPhone Security Best Practices:\n\n"
            "1. Always update to the latest iOS:\n"
            "   Settings → General → Software Update\n\n"
            "2. Enable Face ID or Touch ID + 6-digit PIN\n"
            "   (Never use 4-digit PIN — too easy to guess)\n\n"
            "3. Install apps ONLY from the Apple App Store.\n"
            "   Apple reviews every app before publishing.\n\n"
            "4. Turn on iCloud Keychain:\n"
            "   Securely stores and fills your passwords.\n\n"
            "5. Enable Find My iPhone:\n"
            "   Settings → [Your Name] → Find My → ON\n\n"
            "6. Check for unknown device profiles:\n"
            "   Settings → General → VPN & Device Management\n"
            "   Delete any profile you didn't install yourself.\n\n"
            "7. Never jailbreak your iPhone.\n"
            "   Jailbreaking removes Apple's security protections."
        ),
    },

    {
        "category": "iOS Security",
        "keywords": [
            "jailbreak", "jailbreaking", "root", "rooting",
            "unlock iphone", "bypass ios", "cydia"
        ],
        "response": (
            "⚠️ Jailbreaking — Why It's Very Dangerous!\n\n"
            "Jailbreaking = Removing Apple's built-in security restrictions.\n"
            "Rooting = Same concept on Android.\n\n"
            "🚨 Risks of jailbreaking your iPhone:\n\n"
            "• Malware can access system files with no restrictions\n"
            "• No more automatic Apple security updates\n"
            "• Apps from outside App Store can steal your data\n"
            "• Hackers can remotely control your device\n"
            "• Your Apple warranty is permanently voided\n"
            "• Banking apps stop working (they detect jailbreak)\n"
            "• Phone becomes unstable and crash-prone\n\n"
            "✅ Advice:\n"
            "Never jailbreak your phone.\n"
            "The risks far outweigh any benefits."
        ),
    },

    # ─────────────────────────────────────────
    #  CATEGORY 3: MOBILE MALWARE
    # ─────────────────────────────────────────

    {
        "category": "Mobile Malware",
        "keywords": [
            "malware", "virus", "spyware", "detect", "infected",
            "hack", "hacked", "suspicious", "trojan", "adware",
            "signs", "symptoms", "malicious", "harmful app"
        ],
        "response": (
            "🦠 Signs Your Phone May Have Malware:\n\n"
            "🚩 Warning Signs:\n"
            "• Battery draining unusually fast\n"
            "• Phone heats up even when idle\n"
            "• Unknown apps you never installed\n"
            "• Excessive background data usage\n"
            "• Random ads popping up outside apps\n"
            "• Phone running much slower than normal\n"
            "• Calls or texts you never made\n"
            "• Screen turning on by itself\n\n"
            "🛡️ What To Do If Infected:\n\n"
            "Step 1: Run Google Play Protect scan\n"
            "Step 2: Uninstall all suspicious/unknown apps\n"
            "Step 3: Change all important passwords\n"
            "        (from a clean device!)\n"
            "Step 4: If problem continues → Factory Reset\n"
            "Step 5: Restore from a clean backup\n\n"
            "⚠️ Prevention:\n"
            "Only install apps from official stores."
        ),
    },

    {
        "category": "Mobile Malware",
        "keywords": [
            "spyware", "spy", "stalkerware", "monitoring",
            "track", "tracked", "someone watching", "keylogger",
            "recording secretly", "hidden app"
        ],
        "response": (
            "👁️ What is Mobile Spyware?\n\n"
            "Spyware is hidden software that secretly monitors\n"
            "your phone without your knowledge.\n\n"
            "🚨 What spyware can do:\n"
            "• Record your phone calls\n"
            "• Read all your messages (WhatsApp, SMS)\n"
            "• Track your live GPS location\n"
            "• Steal saved passwords and bank details\n"
            "• Take photos/screenshots silently\n"
            "• Send all data to an attacker's server\n\n"
            "🔍 How to detect spyware:\n"
            "• Battery drains fast with no reason\n"
            "• High data usage in background\n"
            "• Phone warm even when not in use\n"
            "• Unknown apps in app list\n\n"
            "✅ Prevention:\n"
            "• Only install trusted apps\n"
            "• Check app permissions regularly\n"
            "• Use a reputable mobile antivirus\n"
            "• Factory Reset if strongly suspected"
        ),
    },

    # ─────────────────────────────────────────
    #  CATEGORY 4: OTP & AUTHENTICATION FRAUD
    # ─────────────────────────────────────────

    {
        "category": "OTP & Auth Fraud",
        "keywords": [
            "sim swap", "sim swapping", "sim hijack", "sim attack",
            "no service", "number transfer", "carrier attack",
            "lost network", "phone number stolen"
        ],
        "response": (
            "📲 SIM Swap Attack — A Serious Mobile Threat!\n\n"
            "What is it?\n"
            "An attacker convinces your mobile carrier to transfer\n"
            "YOUR phone number to THEIR SIM card.\n"
            "Result: They receive all your SMS OTPs and 2FA codes.\n\n"
            "🚩 Warning Signs:\n"
            "• Your phone suddenly shows 'No Service'\n"
            "• You cannot make calls or send texts\n"
            "• You receive emails about SIM or account changes\n\n"
            "🛡️ Protection Steps:\n\n"
            "1. Set a carrier PIN/passcode:\n"
            "   Call your carrier and set a security PIN\n"
            "   required for any account changes.\n\n"
            "2. Switch from SMS OTP to Authenticator App:\n"
            "   Google Authenticator or Authy are much safer.\n\n"
            "3. If you suspect SIM swap:\n"
            "   Call your carrier IMMEDIATELY.\n"
            "   Change all critical passwords at once."
        ),
    },

    {
        "category": "OTP & Auth Fraud",
        "keywords": [
            "2fa", "two factor", "two-factor", "authentication",
            "otp", "verify", "authenticator", "mfa",
            "multi factor", "login security", "account security"
        ],
        "response": (
            "🔑 Two-Factor Authentication (2FA) on Mobile\n\n"
            "What is 2FA?\n"
            "A second step added to your login process.\n"
            "Even if hackers steal your password, they still\n"
            "cannot access your account without the second factor.\n\n"
            "📊 2FA Methods — Ranked Safest to Weakest:\n\n"
            "1. 🥇 Authenticator App (BEST)\n"
            "   → Google Authenticator, Authy, Microsoft Auth\n"
            "   → Generates time-based codes offline\n\n"
            "2. 🥈 Hardware Key\n"
            "   → YubiKey — physically plug in to verify\n\n"
            "3. 🥉 Push Notification\n"
            "   → Approve login on your phone\n\n"
            "4. ⚠️ SMS OTP (WEAKEST)\n"
            "   → Vulnerable to SIM swap attacks\n"
            "   → Avoid for banking and critical accounts\n\n"
            "✅ Enable 2FA on everything:\n"
            "Gmail, WhatsApp, Instagram, banking apps, UPI!"
        ),
    },

    # ─────────────────────────────────────────
    #  CATEGORY 5: PASSWORDS & PINs
    # ─────────────────────────────────────────

    {
        "category": "Passwords & PINs",
        "keywords": [
            "password", "pin", "lock", "screen lock", "passcode",
            "strong password", "weak password", "change password",
            "mobile password", "phone lock", "pattern lock"
        ],
        "response": (
            "🔏 Securing Your Phone Lock Screen\n\n"
            "✅ Best Practices:\n\n"
            "• Use a 6-digit PIN minimum\n"
            "  (Never use 4-digit — too easy to crack)\n\n"
            "• Better: use an alphanumeric password\n"
            "  Example: Mobile@Safe2024\n\n"
            "• Enable biometric (fingerprint or face ID)\n"
            "  as a fast daily layer on top of PIN\n\n"
            "• Set auto-lock to 30 seconds of inactivity\n\n"
            "• Disable lock screen notifications that\n"
            "  show sensitive message previews\n\n"
            "❌ Never use these PINs:\n"
            "• 123456, 0000, 1111, 4321\n"
            "• Your birth date or year\n"
            "• Your phone number\n"
            "• Repeated digits: 222222\n\n"
            "💡 Strong PIN example: 748392\n"
            "💡 Strong Password: T!rth@Mob!le24"
        ),
    },

    {
        "category": "Passwords & PINs",
        "keywords": [
            "fingerprint", "face id", "biometric", "touch id",
            "face unlock", "facial recognition", "thumb", "iris"
        ],
        "response": (
            "🖐️ Biometric Security on Mobile\n\n"
            "Types of biometric locks:\n"
            "• Fingerprint Scanner (most common, very reliable)\n"
            "• Face ID (Apple) — 3D face mapping, very secure\n"
            "• Face Unlock (Android) — 2D, less secure\n"
            "• Iris Scanner (some Android phones)\n\n"
            "✅ Best Practice: Use BOTH!\n"
            "• Biometric = fast, convenient for daily use\n"
            "• PIN = essential backup when biometrics fail\n\n"
            "⚠️ Biometric Limitations:\n"
            "• Fingerprint can be copied from surfaces\n"
            "• Face unlock can fail with glasses/mask\n"
            "• In some countries, police can legally\n"
            "  force biometric unlock (not PIN)\n\n"
            "💡 For maximum security:\n"
            "Use fingerprint for speed +\n"
            "strong 6-digit PIN as your backup."
        ),
    },

    # ─────────────────────────────────────────
    #  CATEGORY 6: SAFE BROWSING
    # ─────────────────────────────────────────

    {
        "category": "Safe Browsing",
        "keywords": [
            "public wifi", "public wi-fi", "wifi safe", "hotspot",
            "free wifi", "open network", "coffee shop wifi",
            "airport wifi", "hotel wifi", "unsecured network"
        ],
        "response": (
            "📡 Public Wi-Fi is DANGEROUS!\n\n"
            "What's the risk?\n"
            "Hackers perform 'Man-in-the-Middle' (MITM) attacks.\n"
            "They position themselves between you and the router\n"
            "and can see ALL your internet traffic.\n\n"
            "🚨 What they can steal:\n"
            "• Passwords you type\n"
            "• Banking session data\n"
            "• Personal photos/files\n"
            "• WhatsApp or email messages\n\n"
            "✅ How to Stay Safe on Public Wi-Fi:\n\n"
            "1. Always use a VPN — encrypts all traffic\n"
            "2. Avoid banking or shopping on public Wi-Fi\n"
            "3. Turn OFF auto-connect to open networks\n"
            "4. Prefer 4G/5G mobile data over public Wi-Fi\n"
            "5. Check the real network name — hackers create\n"
            "   fake 'AirportWifi' or 'CafeGuest' networks\n"
            "6. Look for HTTPS in website URLs"
        ),
    },

    {
        "category": "Safe Browsing",
        "keywords": [
            "phishing", "smishing", "fake link", "sms phishing",
            "fake sms", "spam sms", "suspicious message",
            "fake message", "phishing text", "click link sms",
            "suspicious sms", "sms scam", "text scam",
            "sms fraud", "fake bank sms", "spam text"
        ],
        "response": (
            "🎣 Smishing — SMS Phishing on Mobile\n\n"
            "What is Smishing?\n"
            "Phishing attacks sent through SMS text messages.\n"
            "Attackers impersonate banks, courier services,\n"
            "or government agencies to trick you.\n\n"
            "📱 Common Smishing Examples:\n"
            "• 'Your bank account is locked! Click: bit.ly/xyz'\n"
            "• 'Your parcel is held. Verify here: fake-link.com'\n"
            "• 'You won Rs 50,000! Claim now: scam.co'\n"
            "• 'KYC update required or account closed'\n\n"
            "🚩 Red Flags to Spot:\n"
            "• Urgent language and threats\n"
            "• Shortened or suspicious links\n"
            "• Unknown sender numbers\n"
            "• Requests for OTP, password, or card number\n\n"
            "✅ Golden Rules:\n"
            "• Banks NEVER ask for passwords via SMS\n"
            "• Never click links in unexpected SMS messages\n"
            "• Go directly to the official app instead\n"
            "• Report spam to your carrier: forward to 1909"
        ),
    },

    # ─────────────────────────────────────────
    #  CATEGORY 7: MOBILE PRIVACY
    # ─────────────────────────────────────────

    {
        "category": "Mobile Privacy",
        "keywords": [
            "permission", "permissions", "app access", "allow",
            "deny", "dangerous permission", "risky permission",
            "what permissions", "which permissions", "app permission"
        ],
        "response": (
            "⚠️ App Permissions — What to Watch Out For\n\n"
            "🚨 HIGH RISK — Deny unless absolutely necessary:\n\n"
            "• 📨 SMS Access\n"
            "  → Can read your OTPs and 2FA codes\n\n"
            "• 🎙️ Microphone\n"
            "  → Can secretly record your conversations\n\n"
            "• 📒 Contacts\n"
            "  → Spyware harvests your contact lists\n\n"
            "• 📍 Fine Location (GPS)\n"
            "  → Tracks your precise movements 24/7\n\n"
            "• 📞 Call Logs\n"
            "  → Exposes your complete call history\n\n"
            "• 🪪 Device ID / Phone Number\n"
            "  → Enables permanent device tracking\n\n"
            "✅ The Golden Rule:\n"
            "Ask yourself: Does this app REALLY need this?\n"
            "A calculator app NEVER needs your microphone.\n"
            "A flashlight app NEVER needs your contacts.\n\n"
            "Review permissions: Settings → Apps → [App] → Permissions"
        ),
    },

    {
        "category": "Mobile Privacy",
        "keywords": [
            "check permission", "how to check", "revoke",
            "remove permission", "permission settings",
            "review permission", "app setting", "privacy setting"
        ],
        "response": (
            "📋 How to Check & Revoke App Permissions\n\n"
            "🤖 On Android:\n"
            "Method 1 — By App:\n"
            "Settings → Apps → [App Name] →\n"
            "Permissions → Review and toggle each one\n\n"
            "Method 2 — By Permission Type:\n"
            "Settings → Privacy → Permission Manager →\n"
            "Select permission → See which apps have it\n\n"
            "🍎 On iPhone / iOS:\n"
            "Settings → Privacy & Security →\n"
            "Select permission type (e.g. Location, Camera) →\n"
            "See all apps with that access → Toggle to deny\n\n"
            "✅ Best Practices:\n"
            "• Review permissions every 3 months\n"
            "• Use 'Only While Using' for location apps\n"
            "• Deny permissions you never consciously granted\n"
            "• Uninstall apps that demand unnecessary access\n\n"
            "💡 Tip: After any new app install,\n"
            "immediately check its permissions!"
        ),
    },

    # ─────────────────────────────────────────
    #  CATEGORY 8: BACKUP & RECOVERY
    # ─────────────────────────────────────────

    {
        "category": "Backup & Recovery",
        "keywords": [
            "backup", "data backup", "restore", "cloud backup",
            "how to backup", "save data", "phone backup",
            "backup android", "backup iphone", "icloud backup"
        ],
        "response": (
            "☁️ Mobile Data Backup Best Practices\n\n"
            "🤖 Android Backup:\n"
            "Settings → Google → Backup →\n"
            "Enable Google One Backup → Back Up Now\n"
            "Backs up: contacts, apps, settings, photos\n\n"
            "🍎 iOS / iPhone Backup:\n"
            "Settings → [Your Name] → iCloud →\n"
            "iCloud Backup → Back Up Now\n"
            "Or: connect to computer → iTunes/Finder backup\n\n"
            "📸 Photos Specifically:\n"
            "• Android → Google Photos (free 15GB)\n"
            "• iPhone → iCloud Photos or Google Photos\n\n"
            "💬 WhatsApp Backup:\n"
            "WhatsApp → Settings → Chats →\n"
            "Chat Backup → Back Up Now\n\n"
            "✅ Follow the 3-2-1 Backup Rule:\n"
            "3 copies of data\n"
            "2 different storage types\n"
            "1 offsite/cloud backup\n\n"
            "⏰ Back up WEEKLY at minimum!\n"
            "If your phone is stolen & wiped — you lose nothing."
        ),
    },

    {
        "category": "Backup & Recovery",
        "keywords": [
            "stolen", "lost phone", "theft", "find my",
            "remote wipe", "missing phone", "phone stolen",
            "lost iphone", "lost android", "locate phone",
            "phone lost", "my phone stolen", "phone was stolen",
            "phone is stolen", "phone missing", "stole my phone"
        ],
        "response": (
            "🚨 Your Phone is Lost or Stolen — Act NOW!\n\n"
            "⏱️ You have MINUTES — act immediately!\n\n"
            "🤖 Android:\n"
            "1. Go to: android.com/find\n"
            "2. Sign in with your Google account\n"
            "3. Options:\n"
            "   • Play Sound (if nearby)\n"
            "   • Secure Device (lock + message)\n"
            "   • Erase Device (WIPE all data)\n\n"
            "🍎 iPhone / iOS:\n"
            "1. Go to: icloud.com/find\n"
            "2. Sign in with your Apple ID\n"
            "3. Options:\n"
            "   • Lost Mode (lock + contact info)\n"
            "   • Erase iPhone (WIPE all data)\n\n"
            "📋 After Wiping / Reporting:\n"
            "✅ Change Gmail / Apple ID password\n"
            "✅ Change banking app passwords\n"
            "✅ Call carrier to block your SIM\n"
            "✅ File police report with IMEI number\n"
            "   (Dial *#06# to find your IMEI)\n"
            "✅ Inform your bank about possible access"
        ),
    },

    {
        "category": "Backup & Recovery",
        "keywords": [
            "vpn", "virtual private network", "privacy browsing",
            "browse safely", "encrypted connection", "hide ip",
            "vpn app", "best vpn", "free vpn", "mobile vpn"
        ],
        "response": (
            "🌐 VPN on Mobile — Why You Need It\n\n"
            "What is a VPN?\n"
            "A Virtual Private Network encrypts ALL your\n"
            "phone's internet traffic and hides your real IP.\n"
            "It creates a secure tunnel between your phone\n"
            "and the internet.\n\n"
            "✅ When to use a VPN:\n"
            "• On public Wi-Fi (cafes, airports, hotels)\n"
            "• To hide browsing from your ISP\n"
            "• When traveling abroad\n"
            "• To access geo-restricted content safely\n\n"
            "🔍 Trusted VPN Apps:\n"
            "Free:  ProtonVPN, Windscribe\n"
            "Paid:  Mullvad, ExpressVPN, NordVPN\n\n"
            "⚠️ Warning about Free VPNs:\n"
            "Many free VPNs SELL your browsing data!\n"
            "Never use random free VPNs from Play Store.\n"
            "Stick to reputable, privacy-audited providers.\n\n"
            "💡 ProtonVPN is the safest free option."
        ),
    },

    {
        "category": "Backup & Recovery",
        "keywords": [
            "update", "patch", "upgrade", "software update",
            "latest version", "security update", "os update",
            "android update", "ios update", "firmware"
        ],
        "response": (
            "🔄 Why Mobile Updates Are Critical for Security\n\n"
            "Why update immediately?\n"
            "Every software update patches known security holes.\n"
            "Unpatched phones are easy targets — hackers actively\n"
            "search for devices running old software versions.\n\n"
            "📊 Real Example:\n"
            "The Pegasus spyware (2021) exploited an iOS bug\n"
            "that Apple patched within days. Unupdated iPhones\n"
            "remained vulnerable for months afterward.\n\n"
            "✅ Best Update Practices:\n"
            "• Update within 24–48 hours of any security patch\n"
            "• Enable automatic updates for OS and all apps\n"
            "• Never ignore 'Security Update' notifications\n"
            "• Check manually if auto-update seems stuck\n\n"
            "🤖 Android:\n"
            "Settings → System → System Update\n\n"
            "🍎 iOS:\n"
            "Settings → General → Software Update\n\n"
            "⚠️ Also update your apps — they have their\n"
            "own security patches independent of the OS!"
        ),
    },

    {
        "category": "Backup & Recovery",
        "keywords": [
            "bluetooth", "nfc", "airdrop", "wireless",
            "nearby share", "file transfer", "pair device",
            "bluetooth attack", "bluesnarfing", "blueborne"
        ],
        "response": (
            "📶 Bluetooth & NFC Security on Mobile\n\n"
            "🔵 Bluetooth Risks:\n"
            "• BlueSnarfing: stealing data via Bluetooth\n"
            "• BlueBorne: spreading malware without pairing\n"
            "• Evil Twin: fake Bluetooth device tricks you\n\n"
            "✅ Bluetooth Safety Rules:\n"
            "• Turn OFF Bluetooth when not actively using\n"
            "• Never pair with unknown Bluetooth devices\n"
            "• Set to 'Not Discoverable' in public places\n"
            "• Don't accept files from unknown Bluetooth sources\n\n"
            "📲 NFC (Near Field Communication) Risks:\n"
            "• Attackers can skim NFC data in crowded places\n"
            "• Malicious NFC tags can trigger unwanted actions\n\n"
            "✅ NFC Safety Rules:\n"
            "• Disable NFC when not making payments\n"
            "• Don't tap your phone on unknown NFC tags\n\n"
            "📤 AirDrop (iPhone) Safety:\n"
            "Settings → General → AirDrop →\n"
            "Set to 'Contacts Only' or 'No One' in public\n"
            "to prevent strangers sending you files."
        ),
    },
]


# ════════════════════════════════════════════════════════════
#  SECTION 4: RESPONSE ENGINE
#
#  get_response(user_input) is the main function called
#  from app.py whenever a user sends a message.
#
#  Algorithm: KEYWORD SCORING
#  ──────────────────────────
#  For each knowledge base entry, we count how many
#  keywords appear in the user's message.
#  The entry with the HIGHEST count wins.
#
#  Example:
#  User: "how do I secure my android phone?"
#  Entry 1 keywords: ["secure","android","phone","basic"]
#    Matches: "secure" ✓, "android" ✓, "phone" ✓ → score = 3
#  Entry 2 keywords: ["ios","iphone","apple"]
#    Matches: none → score = 0
#  Winner: Entry 1 (score 3) → Returns Android security tips
# ════════════════════════════════════════════════════════════

def get_response(user_input: str) -> str:
    """
    Takes the user's message and returns the best matching
    mobile security response from the knowledge base.

    Parameters:
        user_input (str): The raw text typed by the user

    Returns:
        str: The matched response or a fallback message
    """

    # ── Step 1: Normalize input ──────────────────────────
    # Convert to lowercase so "Android" and "android" both match
    text = user_input.lower().strip()

    # ── Step 2: Handle empty input ───────────────────────
    if not text:
        return "❓ Please type a question about mobile security!"

    # ── Step 3: Detect greetings ─────────────────────────
    GREETINGS = [
        "hello", "hey", "good morning", "good evening",
        "good afternoon", "howdy", "sup", "hola", "namaste",
        "what's up", "whats up","jay shree krishna", "greetings"
    ]
    # Only trigger greeting if input is SHORT (under 6 words)
    # Prevents "hello what is smishing" triggering greeting only
    word_count = len(text.split())
    if any(greet in text for greet in GREETINGS) and word_count <= 4:
        return (
            "👋 Hello! I'm MobileGuard, your mobile security assistant!\n\n"
            "I can help you with:\n"
            "📱 Android & iOS security tips\n"
            "🦠 Detecting mobile malware\n"
            "🔑 2FA and OTP fraud protection\n"
            "📡 Public Wi-Fi safety\n"
            "🔍 App permission risks\n"
            "📲 SIM swap attack prevention\n"
            "☁️ Data backup strategies\n"
            "🚨 What to do if phone is stolen\n\n"
            "How can I help you today? Just ask your question!"
        )

    # ── Step 4: Detect thanks / positive feedback ────────
    THANKS_WORDS = [
        "thank", "thanks", "thx", "thank you", "thankyou",
        "great", "awesome", "helpful", "nice", "good", "perfect",
        "brilliant", "excellent", "superb", "well done"
    ]
    if any(word in text for word in THANKS_WORDS):
        return (
            "😊 You're welcome! Happy to help.\n\n"
            "Remember these 3 golden mobile security rules:\n"
            "1. 🔐 Always keep your phone updated\n"
            "2. 📦 Only install apps from official stores\n"
            "3. 🔑 Enable 2FA on all important accounts\n\n"
            "Stay safe and secure out there! 🛡️"
        )

    # ── Step 5: Detect help request ──────────────────────
    HELP_WORDS = ["help", "what can you do", "topics", "options",
                  "menu", "guide", "assist", "what do you know"]
    if any(word in text for word in HELP_WORDS):
        return (
            "🛡️ MobileGuard can answer questions about:\n\n"
            "1. 🤖 Android security\n"
            "2. 🍎 iOS / iPhone security\n"
            "3. 🦠 Mobile malware detection\n"
            "4. 📲 SIM swap attacks\n"
            "5. 🔑 Two-factor authentication (2FA)\n"
            "6. 🔏 PIN and password security\n"
            "7. 📡 Public Wi-Fi dangers\n"
            "8. 🎣 Smishing (SMS phishing)\n"
            "9. ⚠️ Dangerous app permissions\n"
            "10. 🔵 Bluetooth and NFC safety\n"
            "11. ☁️ Data backup strategies\n"
            "12. 🚨 Lost or stolen phone recovery\n"
            "13. 🌐 VPN on mobile\n"
            "14. 🔄 Why software updates matter\n"
            "15. 👁️ Spyware detection\n\n"
            "Just type your question and I'll answer!"
        )

    # ── Step 6: KEYWORD SCORING ENGINE ───────────────────
    best_response = None
    best_score    = 0

    for entry in KNOWLEDGE_BASE:
        # Count how many keywords from this entry appear in user text
        score = sum(1 for keyword in entry["keywords"] if keyword in text)

        # Keep track of highest scoring entry
        if score > best_score:
            best_score    = score
            best_response = entry["response"]

    # ── Step 7: Return result ─────────────────────────────
    if best_response is not None and best_score > 0:
        # Found a matching entry — return its response
        return best_response
    else:
        # No match found — return a random helpful fallback
        return random.choice(FALLBACK_RESPONSES)

#
#  HOW THIS FILE WORKS:
#  ─────────────────────
#  This file contains two things:
#
#  1. KNOWLEDGE_BASE — A list of dictionaries.
#     Each dictionary has:
#       "keywords"  → list of words to match in user input
#       "category"  → topic group (for organisation)
#       "response"  → the full answer to return
#
#  2. get_response() — A function that:
#       Step 1: Converts user input to lowercase
#       Step 2: Checks for greetings / thanks
#       Step 3: Scores each knowledge base entry
#               by counting how many keywords match
#       Step 4: Returns the highest-scoring response
#       Step 5: Returns a fallback if nothing matches
#
#  This approach is called KEYWORD SCORING.
#  It is more flexible than simple if/elif chains
#  because it finds the BEST match, not just any match.
# ============================================================