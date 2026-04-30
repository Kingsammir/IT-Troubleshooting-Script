# 🛠️ IT Troubleshooting Assistant

A command-line tool that guides users through diagnosing and resolving common IT issues — step by step.

Built by **Oyalana Samuel** | [LinkedIn](https://linkedin.com) |

---

## 💡 What It Does

Instead of Googling generic fixes, this tool walks you through a structured diagnostic process for the most common IT problems:

| # | Issue |
|---|-------|
| 1 | No Internet Connection |
| 2 | Slow Computer / High CPU Usage |
| 3 | Cannot Connect to a Website |
| 4 | Printer Not Responding |
| 5 | Application Crashing / Not Opening |
| 6 | Full System Diagnostics Report |

---

## 🚀 Getting Started

### Requirements
- Python 3.7+
- Optional: `psutil` for CPU/memory monitoring

```bash
pip install psutil
```

### Run the tool

```bash
python troubleshoot.py
```

---

## 📸 Screenshot

```
  ╔══════════════════════════════════════════╗
  ║       IT TROUBLESHOOTING ASSISTANT       ║
  ║         by Oyalana Samuel                ║
  ╚══════════════════════════════════════════╝

  Select an issue to diagnose:
    [1] No Internet Connection
    [2] Slow Computer / High CPU Usage
    [3] Cannot Connect to a Website
    [4] Printer Not Responding
    [5] Application Crashing / Not Opening
    [6] Run Full System Diagnostics
    [0] Exit
```

---

## 🔍 How It Works

Each issue triggers a structured diagnostic flow:

1. **Automated checks** — pings, DNS lookups, system metrics
2. **Colour-coded results** — green (OK), yellow (warning), red (fail)
3. **Actionable recommendations** — specific steps tailored to what was found

---

## 🎮 Usage Walkthrough

### Step 1 — Launch the tool
```bash
python troubleshoot.py
```

You'll see the welcome banner and a menu:
```
  ╔══════════════════════════════════════════╗
  ║       IT TROUBLESHOOTING ASSISTANT       ║
  ║         by Oyalana Samuel                ║
  ╚══════════════════════════════════════════╝

  Select an issue to diagnose:
    [1] No Internet Connection
    [2] Slow Computer / High CPU Usage
    [3] Cannot Connect to a Website
    [4] Printer Not Responding
    [5] Application Crashing / Not Opening
    [6] Run Full System Diagnostics
    [0] Exit
```

---

### Example: Diagnosing No Internet (Option 1)

Type `1` and press Enter. The tool runs live checks automatically:

```
──────────────────────────────────────────────────
  Diagnosing: No Internet Connection
──────────────────────────────────────────────────
  [i] Step 1 of 4 — Checking local network gateway (8.8.8.8)…
  [✔] Gateway reachable. Your local network is working.

  [i] Step 2 of 4 — Testing DNS resolution (google.com)…
  [✔] DNS is resolving correctly.

  [i] Step 3 of 4 — Pinging google.com…
  [✔] External ping successful. Internet is reachable.

  [i] Step 4 of 4 — Browser check reminder
     • Clear browser cache and cookies.
     • Try a different browser (Chrome, Firefox, Edge).
     • Disable browser extensions one by one.
  [✔] Diagnostics complete.
```

If a step **fails**, it shows a red ✘ with specific recommended fixes tailored to what went wrong.

---

### Example: Cannot Connect to a Website (Option 3)

Type `3`, then enter the website when prompted:

```
  Enter the website URL (e.g. google.com): twitter.com

  [i] Step 1 — DNS lookup for 'twitter.com'…
  [✔] DNS resolved successfully for twitter.com.

  [i] Step 2 — Pinging 'twitter.com'…
  [!] Server not responding to ping (may be intentionally blocked).
     • Try opening the site in a different browser.
     • Disable VPN / proxy.
     • Check if it's down globally: https://isitdownrightnow.com
```

---

### Example: Full System Diagnostics (Option 6)

Type `6` for a complete snapshot of your system:

```
──────────────────────────────────────────────────
  Full System Diagnostics Report
──────────────────────────────────────────────────
  [i] Operating System:
     Windows 11 — 10.0.22621
     Machine: AMD64 | Processor: Intel Core i5

  [i] Network:
     Gateway reachable : ✔
     DNS resolution    : ✔
     Internet access   : ✔

  [i] Performance:
     CPU Usage : 18.3%
     Memory    : 4200 MB used / 16384 MB total (25.6%)

  [i] Host:
     Hostname : SAMUEL-PC
     Local IP : 192.138.1.109

  [✔] Full diagnostics complete.
```

---

## 🧠 Skills Demonstrated

- Python scripting (subprocess, socket, platform modules)
- Network diagnostics (ping, DNS resolution)
- System monitoring (CPU/memory via psutil)
- IT support methodology (structured troubleshooting)
- User-facing CLI design

---

## 📁 Project Structure

```
it-troubleshooter/
│
├── troubleshoot.py   ← Main script
└── README.md         ← This file
```

---

## 📬 Contact

**Oyalana Samuel** — oyalanasam@gmail.com  
Open to IT Support, Technical Operations, and AI-related roles.
