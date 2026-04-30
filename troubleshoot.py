#!/usr/bin/env python3
"""
IT Troubleshooting Assistant
Author: Oyalana Samuel
Description: A command-line tool that guides users through common IT issues
             with step-by-step diagnostics and resolution suggestions.
"""

import subprocess
import platform
import socket
import sys
import os


# ─────────────────────────────────────────────
#  COLOUR HELPERS
# ─────────────────────────────────────────────
class Colors:
    GREEN  = "\033[92m"
    YELLOW = "\033[93m"
    RED    = "\033[91m"
    CYAN   = "\033[96m"
    BOLD   = "\033[1m"
    RESET  = "\033[0m"

def ok(msg):    print(f"{Colors.GREEN}  [✔] {msg}{Colors.RESET}")
def warn(msg):  print(f"{Colors.YELLOW}  [!] {msg}{Colors.RESET}")
def fail(msg):  print(f"{Colors.RED}  [✘] {msg}{Colors.RESET}")
def info(msg):  print(f"{Colors.CYAN}  [i] {msg}{Colors.RESET}")
def header(msg):
    print(f"\n{Colors.BOLD}{Colors.CYAN}{'─'*50}")
    print(f"  {msg}")
    print(f"{'─'*50}{Colors.RESET}")


# ─────────────────────────────────────────────
#  ISSUE CATALOGUE
# ─────────────────────────────────────────────
ISSUES = {
    "1": "No Internet Connection",
    "2": "Slow Computer / High CPU Usage",
    "3": "Cannot Connect to a Website",
    "4": "Printer Not Responding",
    "5": "Application Crashing / Not Opening",
    "6": "Run Full System Diagnostics",
}


# ─────────────────────────────────────────────
#  DIAGNOSTIC HELPERS
# ─────────────────────────────────────────────
def ping_host(host: str) -> bool:
    """Return True if host responds to ping."""
    flag = "-n" if platform.system().lower() == "windows" else "-c"
    result = subprocess.run(
        ["ping", flag, "1", host],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    return result.returncode == 0


def dns_resolve(host: str) -> bool:
    """Return True if DNS can resolve host."""
    try:
        socket.gethostbyname(host)
        return True
    except socket.gaierror:
        return False


def get_cpu_usage() -> float:
    """Return current CPU usage % (cross-platform, no psutil required)."""
    try:
        import psutil
        return psutil.cpu_percent(interval=1)
    except ImportError:
        return -1.0


def get_memory_usage():
    """Return (used_mb, total_mb) or None if psutil unavailable."""
    try:
        import psutil
        mem = psutil.virtual_memory()
        return round(mem.used / 1024**2), round(mem.total / 1024**2)
    except ImportError:
        return None


# ─────────────────────────────────────────────
#  ISSUE HANDLERS
# ─────────────────────────────────────────────
def fix_no_internet():
    header("Diagnosing: No Internet Connection")

    # Step 1 – local gateway
    info("Step 1 of 4 — Checking local network gateway (8.8.8.8)…")
    if ping_host("8.8.8.8"):
        ok("Gateway reachable. Your local network is working.")
    else:
        fail("Cannot reach gateway. Possible causes:")
        print("     • Router/modem is off or restarting")
        print("     • Ethernet cable unplugged / Wi-Fi disconnected")
        print("     • ISP outage in your area")
        print("\n  Recommended steps:")
        print("     1. Restart your router and modem (unplug 30 s, replug).")
        print("     2. Check physical cables / reconnect Wi-Fi.")
        print("     3. Contact your ISP if the problem persists.")
        return

    # Step 2 – DNS
    info("Step 2 of 4 — Testing DNS resolution (google.com)…")
    if dns_resolve("google.com"):
        ok("DNS is resolving correctly.")
    else:
        fail("DNS resolution failed.")
        print("     • Try changing DNS to 8.8.8.8 / 8.8.4.4 (Google DNS).")
        print("     • On Windows: Settings → Network → DNS server.")
        print("     • On Linux/Mac: edit /etc/resolv.conf")
        return

    # Step 3 – external ping
    info("Step 3 of 4 — Pinging google.com…")
    if ping_host("google.com"):
        ok("External ping successful. Internet is reachable.")
    else:
        warn("DNS works but ping blocked — likely a firewall rule.")
        print("     • Disable VPN temporarily.")
        print("     • Check Windows Firewall / iptables rules.")

    # Step 4 – browser hint
    info("Step 4 of 4 — Browser check reminder")
    print("     • Clear browser cache and cookies.")
    print("     • Try a different browser (Chrome, Firefox, Edge).")
    print("     • Disable browser extensions one by one.")
    ok("Diagnostics complete.")


def fix_slow_computer():
    header("Diagnosing: Slow Computer / High CPU Usage")

    cpu = get_cpu_usage()
    mem = get_memory_usage()

    if cpu >= 0:
        label = "High" if cpu > 80 else ("Moderate" if cpu > 50 else "Normal")
        fn = fail if cpu > 80 else (warn if cpu > 50 else ok)
        fn(f"CPU Usage: {cpu:.1f}%  [{label}]")
    else:
        warn("psutil not installed — install with: pip install psutil")
        info("CPU usage could not be measured automatically.")

    if mem:
        used, total = mem
        pct = used / total * 100
        fn = fail if pct > 85 else (warn if pct > 65 else ok)
        fn(f"Memory Usage: {used} MB / {total} MB  ({pct:.1f}%)")

    print()
    info("General recommendations:")
    steps = [
        "Close unused browser tabs and background applications.",
        "Disable startup programs: Task Manager → Startup (Windows).",
        "Run Disk Cleanup or 'sudo apt autoremove' (Linux).",
        "Check for malware with Windows Defender / ClamAV.",
        "Consider upgrading RAM if usage is consistently above 85%.",
        "Restart the computer — clears memory leaks.",
    ]
    for i, s in enumerate(steps, 1):
        print(f"     {i}. {s}")
    ok("Diagnostics complete.")


def fix_website_unreachable():
    header("Diagnosing: Cannot Connect to a Website")

    site = input(f"\n{Colors.CYAN}  Enter the website URL (e.g. google.com): {Colors.RESET}").strip()
    site = site.replace("https://", "").replace("http://", "").split("/")[0]

    info(f"Step 1 — DNS lookup for '{site}'…")
    if dns_resolve(site):
        ok(f"DNS resolved successfully for {site}.")
    else:
        fail(f"DNS cannot resolve '{site}'.")
        print("     • The domain may be misspelled.")
        print("     • Your DNS server may be blocking it.")
        print("     • The website may be down globally.")
        print(f"     • Check: https://downforeveryoneorjustme.com/{site}")
        return

    info(f"Step 2 — Pinging '{site}'…")
    if ping_host(site):
        ok("Server is responding to ping.")
    else:
        warn("Server not responding to ping (may be intentionally blocked).")
        print("     • Try opening the site in a different browser.")
        print("     • Disable VPN / proxy.")
        print(f"     • Check if it's down globally: https://isitdownrightnow.com")

    info("Step 3 — Additional suggestions:")
    print("     • Clear browser cache: Ctrl+Shift+Delete")
    print("     • Try Incognito/Private mode.")
    print("     • Flush DNS cache:")
    print("         Windows → ipconfig /flushdns")
    print("         Mac     → sudo dscacheutil -flushcache")
    print("         Linux   → sudo systemd-resolve --flush-caches")
    ok("Diagnostics complete.")


def fix_printer():
    header("Diagnosing: Printer Not Responding")
    steps = [
        ("Check power & cables", "Ensure printer is ON and USB/network cable is secure."),
        ("Restart devices",      "Turn off printer, restart computer, then turn printer back on."),
        ("Clear print queue",    "Windows: Control Panel → Devices → Printers → right-click → See what's printing → Cancel all."),
        ("Check default printer","Ensure the correct printer is set as default."),
        ("Reinstall driver",     "Download latest driver from manufacturer's website (HP, Canon, Epson, etc.)."),
        ("Network printer",      "Ensure printer and computer are on the same Wi-Fi network."),
        ("Test page",            "Print a test page from printer settings to isolate if issue is hardware or software."),
    ]
    for i, (title, detail) in enumerate(steps, 1):
        print(f"\n  {Colors.BOLD}Step {i}: {title}{Colors.RESET}")
        print(f"     {detail}")
    ok("\nDiagnostics complete.")


def fix_app_crash():
    header("Diagnosing: Application Crashing / Not Opening")
    steps = [
        ("Restart the app",         "Close completely (check Task Manager) and reopen."),
        ("Run as Administrator",    "Right-click the app → Run as administrator."),
        ("Check for updates",       "Update the application to the latest version."),
        ("Clear app cache/data",    "Find app settings and clear cache or temp files."),
        ("Check system logs",       "Windows: Event Viewer → Windows Logs → Application.\n         Linux: journalctl -xe | grep <appname>"),
        ("Reinstall the app",       "Uninstall completely, restart, then reinstall fresh."),
        ("Check compatibility",     "Verify the app supports your OS version."),
        ("Scan for malware",        "Run a full antivirus scan — malware can corrupt apps."),
    ]
    for i, (title, detail) in enumerate(steps, 1):
        print(f"\n  {Colors.BOLD}Step {i}: {title}{Colors.RESET}")
        print(f"     {detail}")
    ok("\nDiagnostics complete.")


def full_diagnostics():
    header("Full System Diagnostics Report")

    # OS info
    info("Operating System:")
    print(f"     {platform.system()} {platform.release()} — {platform.version()}")
    print(f"     Machine: {platform.machine()} | Processor: {platform.processor()}")

    # Network
    info("Network:")
    gateway_ok = ping_host("8.8.8.8")
    dns_ok = dns_resolve("google.com")
    internet_ok = ping_host("google.com")
    print(f"     Gateway reachable : {'✔' if gateway_ok  else '✘'}")
    print(f"     DNS resolution    : {'✔' if dns_ok      else '✘'}")
    print(f"     Internet access   : {'✔' if internet_ok else '✘'}")

    # CPU / Memory
    info("Performance:")
    cpu = get_cpu_usage()
    mem = get_memory_usage()
    print(f"     CPU Usage : {cpu:.1f}%" if cpu >= 0 else "     CPU Usage : N/A (install psutil)")
    if mem:
        used, total = mem
        print(f"     Memory    : {used} MB used / {total} MB total ({used/total*100:.1f}%)")
    else:
        print("     Memory    : N/A (install psutil)")

    # Hostname
    info("Host:")
    print(f"     Hostname : {socket.gethostname()}")
    try:
        print(f"     Local IP : {socket.gethostbyname(socket.gethostname())}")
    except Exception:
        print("     Local IP : Unable to determine")

    ok("Full diagnostics complete.")


# ─────────────────────────────────────────────
#  MAIN MENU
# ─────────────────────────────────────────────
HANDLERS = {
    "1": fix_no_internet,
    "2": fix_slow_computer,
    "3": fix_website_unreachable,
    "4": fix_printer,
    "5": fix_app_crash,
    "6": full_diagnostics,
}

def main():
    print(f"\n{Colors.BOLD}{Colors.CYAN}")
    print("  ╔══════════════════════════════════════════╗")
    print("  ║       IT TROUBLESHOOTING ASSISTANT       ║")
    print("  ║         by Oyalana Samuel                ║")
    print("  ╚══════════════════════════════════════════╝")
    print(Colors.RESET)

    while True:
        print(f"\n{Colors.BOLD}  Select an issue to diagnose:{Colors.RESET}")
        for key, label in ISSUES.items():
            print(f"    {Colors.CYAN}[{key}]{Colors.RESET} {label}")
        print(f"    {Colors.CYAN}[0]{Colors.RESET} Exit\n")

        choice = input("  Your choice: ").strip()

        if choice == "0":
            print(f"\n{Colors.GREEN}  Goodbye! Stay connected. 👋{Colors.RESET}\n")
            sys.exit(0)
        elif choice in HANDLERS:
            HANDLERS[choice]()
        else:
            warn("Invalid choice. Please enter a number from the menu.")


if __name__ == "__main__":
    main()
