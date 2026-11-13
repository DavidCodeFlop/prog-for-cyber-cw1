"""
Task 5: Main programme for the reusable cyber security utilities.
"""

import security_tools


def main():
    """Collect user input and demonstrate the imported utility functions."""
    print("REUSABLE CYBER SECURITY UTILITIES")

    entered_password = input("Enter a password to check: ")
    if security_tools.validate_password(entered_password):
        print("Password meets the minimum strength checks.")
    else:
        print("Password does not meet the strength checks.")
        print(
            "Suggested strong password: "
            f"{security_tools.generate_strong_password()}"
        )

    entered_ip = input("\nEnter an IP address to check: ")
    if security_tools.validate_ip(entered_ip):
        print("IP address passed the basic format checks.")
    else:
        print("IP address failed the basic format checks.")


if __name__ == "__main__":
    main()
