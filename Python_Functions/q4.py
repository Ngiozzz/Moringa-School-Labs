# Q4: WiFi questionnaire
import os

# Look for wifi.txt next to this script, wherever you run it from
WIFI_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "wifi.txt")

# Load the data into a dictionary: {"finance": ("Corp_Finance_Secure", "password"), ...}
wifi = {}
with open(WIFI_FILE, "r") as file:
    for line in file:
        line = line.strip()
        if line:
            department, ssid, password = line.split(",")
            wifi[department.lower()] = (ssid, password)

user_type = input("Are you staff or a guest? ").strip().lower()

if user_type == "staff":
    while True:
        dept = input("Which department do you work in? ").strip().lower()

        if dept in wifi and dept != "guest":
            ssid, password = wifi[dept]
            print(f"\nWiFi Name: {ssid}")
            print(f"Password: {password}")
            break
        else:
            print("Department not recognized. Please enter a valid department "
                  "(Finance, Marketing, IT or Operations).")

elif user_type == "guest":
    signed_in = input("Have you signed in at the front desk? (yes/no) ").strip().lower()

    if signed_in == "yes":
        ssid, password = wifi["guest"]
        print(f"\nWiFi Name: {ssid}")
        print(f"Password: {password}")
    else:
        print("Please go and sign in at the front desk first as to get the connection details.")

else:
    print("Please answer with 'staff' or 'guest'.")