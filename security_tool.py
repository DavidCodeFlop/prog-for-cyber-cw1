"""
Task 1: Security Tool
A menu-driven demonstration of basic security controls.
"""


def security_event_counter():
    """Collect ten password entries and report correct and incorrect totals."""
    correct_password = "CyberSecure123!"
    correct_count = 0
    incorrect_count = 0

    print("\n--- Security Event Counter ---")
    for attempt in range(1, 11):
        entered_password = input(f"Entry {attempt}/10 - Enter password: ")

        if entered_password == correct_password:
            correct_count += 1
            print("Correct password.")
        else:
            incorrect_count += 1
            print("Incorrect password.")

    incorrect_percentage = (incorrect_count / 10) * 100

    print(f"\nCorrect entries: {correct_count}")
    print(f"Incorrect entries: {incorrect_count}")
    print(f"Incorrect percentage: {incorrect_percentage:.1f}%")

    if incorrect_percentage > 50:
        print("ALERT: More than 50% of password entries were incorrect.")
    else:
        print("No security alert: incorrect entries did not exceed 50%.")


def brute_force_simulation():
    """Simulate password guessing with a fixed maximum number of attempts."""
    predefined_password = "BlueTeam#2026"
    maximum_attempts = 5
    attempts = 0

    print("\n--- Brute-Force Simulation ---")
    print(f"You have a maximum of {maximum_attempts} attempts.")

    while attempts < maximum_attempts:
        guess = input("Enter your password guess: ")
        attempts += 1

        if guess == predefined_password:
            print(f"Access granted after {attempts} attempt(s).")
            break

        remaining = maximum_attempts - attempts
        print(f"Incorrect password. Attempts remaining: {remaining}")

    if attempts == maximum_attempts and guess != predefined_password:
        print("Access denied. Maximum attempts reached.")


def login_authentication():
    """Allow three failed logins before reporting a 24-hour account freeze."""
    valid_username = "securityadmin"
    valid_password = "Admin2026"
    maximum_failed_logins = 3
    failed_logins = 0

    print("\n--- Login Authentication ---")

    while failed_logins < maximum_failed_logins:
        username = input("Username: ")
        password = input("Password: ")

        if username == valid_username and password == valid_password:
            print("Authentication successful. Welcome.")
            return

        failed_logins += 1
        print(f"Authentication failed ({failed_logins}/{maximum_failed_logins}).")

    print("Maximum failed logins reached. The account is frozen for 24 hours.")


def display_menu():
    """Display the available security functions."""
    print("\n========== SECURITY TOOL ==========")
    print("1. Security Event Counter")
    print("2. Brute-Force Simulation")
    print("3. Login Authentication")
    print("4. Exit")


def main():
    """Authenticate the operator, then run the selected menu function."""
    operator_username = "operator"
    operator_password = "SecureEntry#1"

    print("Please authenticate to access the security tool.")
    username = input("Username: ")
    password = input("Password: ")

    if username != operator_username or password != operator_password:
        print("Authentication failed. The security tool will close.")
        return

    print("Authentication successful.")

    while True:
        display_menu()

        try:
            choice = int(input("Select an option (1-4): "))
        except ValueError:
            print("Invalid input. Please enter a whole number from 1 to 4.")
            continue

        if choice == 1:
            security_event_counter()
        elif choice == 2:
            brute_force_simulation()
        elif choice == 3:
            login_authentication()
        elif choice == 4:
            print("Thank you for using the security tool")
            break
        else:
            print("Invalid selection. Please choose an option from 1 to 4.")


if __name__ == "__main__":
    main()
