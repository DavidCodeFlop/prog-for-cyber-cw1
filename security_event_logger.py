"""
Task 2: Security Event Logger
Records each login attempt with an event ID and timestamp.
"""

from datetime import datetime


def main():
    """Request credentials until a valid login is supplied and log each attempt."""
    valid_username = "admin"
    valid_password = "CyberAdmin#26"
    event_logs = []
    event_id = 1

    print("SECURITY EVENT LOGGER")
    print("Enter the correct credentials to finish the session.\n")

    while True:
        username = input("Username: ")
        password = input("Password: ")

        if username == valid_username and password == valid_password:
            event_type = "Successful login"
        else:
            event_type = "Failed login"

        event = {
            "event_id": event_id,
            "username": username,
            "ip_address": "127.0.0.1",
            "event": event_type,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        event_logs.append(event)

        print("\n--- Event log entry ---")
        for field, value in event.items():
            print(f"{field.replace('_', ' ').title()}: {value}")
        print()

        event_id += 1

        if event_type == "Successful login":
            print("Correct credentials supplied. Logging session complete.")
            break

    print("\n========== COMPLETE EVENT LOG ==========")
    for event in event_logs:
        print(
            f"ID: {event['event_id']} | User: {event['username']} | "
            f"IP: {event['ip_address']} | Event: {event['event']} | "
            f"Time: {event['timestamp']}"
        )


if __name__ == "__main__":
    main()
