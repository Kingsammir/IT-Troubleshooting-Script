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
