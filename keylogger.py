import psutil
import time

# List of suspicious process names
SUSPICIOUS_PROCESSES = [
    "keylogger.exe",
    "logger.exe",
    "spy.exe",
    "hook.exe",
    "keyboard.exe"
]

def monitor_system():
    print("=" * 50)
    print("    KEYLOGGER DETECTION & SYSTEM MONITORING")
    print("=" * 50)

    while True:
        print("\nChecking running processes...\n")

        found = False

        for process in psutil.process_iter(['pid', 'name']):
            try:
                process_name = process.info['name']

                if process_name and process_name.lower() in SUSPICIOUS_PROCESSES:
                    print("⚠ ALERT!")
                    print("Suspicious Process Detected")
                    print("PID :", process.info['pid'])
                    print("Name:", process_name)
                    found = True

            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass

        if not found:
            print("✔ No suspicious process detected.")

        print("\nCPU Usage:", psutil.cpu_percent(), "%")
        print("Memory Usage:", psutil.virtual_memory().percent, "%")

        print("-" * 50)
        time.sleep(10)

if __name__ == "__main__":
    monitor_system()