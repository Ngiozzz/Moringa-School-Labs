# Q2: Password checker (repeats until the password is strong)

while True:
    password = input("\nEnter your password: ")

    length = len(password)
    upper_count = 0
    digit_count = 0
    special_count = 0

    for char in password:
        if char.isupper():
            upper_count += 1
        elif char.isdigit():
            digit_count += 1
        elif not char.isalnum() and not char.isspace():
            special_count += 1

    print("\nPassword feedback:")

    if length >= 8:
        print(f"Length is OK - {length} characters")
    else:
        print(f"Length is NOT OK - Only {length} characters")

    if upper_count > 0:
        print(f"Letter case is OK - has {upper_count} uppercase character(s)")
    else:
        print("Letter case is NOT OK - has no uppercase characters")

    if digit_count > 0:
        print(f"Presence of numbers is OK - has {digit_count} number(s)")
    else:
        print("Presence of numbers is NOT OK - has no numbers")

    if special_count > 0:
        print(f"Presence of special characters is OK - has {special_count} special character(s)")
    else:
        print("Presence of special characters is NOT OK - has no special characters")

    # Stop only when every criterion is met
    if length >= 8 and upper_count > 0 and digit_count > 0 and special_count > 0:
        print("\nStrong password! Password accepted.")
        break
    else:
        print("\nPassword does not meet all the criteria. Please try again.")