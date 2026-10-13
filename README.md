# Moringa School Labs

Lab work from the Moringa School Cyber Security course.

## Contents

| Folder | What's inside |
|---|---|
| [`IP Addressing/`](IP%20Addressing/) | IP addressing assignment and a Wireshark lab write-up (Word documents) |
| [`Python_Functions/`](Python_Functions/) | Six Python exercises (`q1.py`–`q6.py`), their data files and terminal screenshots |
| `Python_Functions_Group 6.zip` | Zipped copy of the Python Functions submission |

## Python Functions

Each exercise has a matching screenshot (`qN terminal.png`) showing a sample run.

### Q1 – Career fair sign-up (`q1.py`)
Asks for a name, course and mode of learning (part-time/full-time), appends the record to `attendees.txt`, and prints a confirmation with a ticket number based on how many people have already signed up.

### Q2 – Password checker (`q2.py`)
Keeps asking for a password until it is strong. Each attempt gets feedback on four rules:
- at least 8 characters
- at least one uppercase letter
- at least one number
- at least one special character

### Q3 – Guessing game (`q3.py`)
The player gets 3 tries to guess the lucky number. Winners are saved to `winners.txt`, and a name that is already on the list isn't added again.

### Q4 – WiFi questionnaire (`q4.py`)
Reads network names and passwords from `wifi.txt`.
- **Staff** enter their department (Finance, Marketing, IT or Operations) and get that department's WiFi details. The script keeps asking until the department is valid.
- **Guests** get the guest network only if they confirm they have signed in at the front desk.

### Q5 – Brute-force detection (`q5.py`)
Writes a list of login events to `logs.txt`, then reads them back and counts failed logins per IP address. When any IP reaches 3 failures, it prints a brute-force alert and stops.

### Q6 – Study groups (`q6.py`)
Works with `CSFB-FT11 Study Groups.xlsx` through a small menu:
1. **Split the groups:** writes one file per group into `study_groups/` (`group1.txt` … `group8.txt`), listing each member as `Name - email`. Names come from the email address (for example `mark.juma1@…` becomes `Mark Juma`).
2. **Find your group:** search by full email or by name (the start of a first or last name works), and the script shows that student's group and all its members.
3. **Exit**

## Running the scripts

Requires Python 3. Only Q6 needs an extra package:

```bash
cd Python_Functions
python -m venv venv
venv\Scripts\activate        # Windows
pip install openpyxl
python q6.py
```

The other scripts run on their own, e.g. `python q2.py`.

> **Note:** `q1.py`, `q3.py`, `q5.py` and `q6.py` use full Windows file paths (`C:\Users\ngiog\...`) for their data files. To run them on another machine, change those paths, or point them at the script's own folder the way `q4.py` does.
