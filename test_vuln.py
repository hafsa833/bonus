import subprocess

def run_bandit_scan():
    print("🔍 Running bandit security scan on app.py...")
    result = subprocess.run(["bandit", "-r", "app.py"], capture_output=True, text=True)
    print(result.stdout)
    return result.returncode

if __name__ == "__main__":
    exit_code = run_bandit_scan()
    if exit_code == 0:
        print("✅ No vulnerabilities found.")
    else:
        print("❌ Vulnerabilities detected!")
    exit(exit_code)
