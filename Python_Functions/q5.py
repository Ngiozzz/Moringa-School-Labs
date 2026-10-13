# Q5: Brute-force detection

logs = [
    "192.168.1.50 - successful login",
    "10.0.0.15 - failed login",
    "192.168.1.50 - successful login",
    "10.0.0.15 - failed login",
    "172.16.0.4 - successful login",
    "10.0.0.15 - failed login",
    "10.0.0.15 - failed login"
]

#LOG_FILE = "logs.txt"
LOG_FILE = r"C:\Users\ngiog\Desktop\Moringa School\Lab Works\Python_Functions\logs.txt"

# Step 1: write each log to the file, one per line
with open(LOG_FILE, "w") as file:
    for log in logs:
        file.write(log + "\n")

# Step 2: read the file and count failed logins per IP
failed_counts = {}

with open(LOG_FILE, "r") as file:
    for line in file:
        line = line.strip()

        if "failed login" in line:
            ip = line.split()[0]   # first word on the line is the IP
            failed_counts[ip] = failed_counts.get(ip, 0) + 1

            # Step 3: alert and stop as soon as an IP hits 3 failures
            if failed_counts[ip] >= 3:
                print(f"ALERT: Brute-force detected from IP {ip}")
                break