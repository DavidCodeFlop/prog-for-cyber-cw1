"""
Task 4: Security Incident Manager
Demonstrates creating, reading, updating and deleting dictionary entries.
"""


def main():
    """Manage a single example security incident using a dictionary."""
    # Store the initial details for one security incident.
    incident = {
        "username": "analyst01",
        "ip_address": "192.168.1.45",
        "event_type": "Multiple failed logins",
        "risk_level": "Medium"
    }

    # Display the two fields specifically requested.
    print("Initial incident details")
    print(f"Username: {incident['username']}")
    print(f"IP address: {incident['ip_address']}")

    # Add a status field and update the risk level.
    incident["status"] = "Under investigation"
    incident["risk_level"] = "High"

    # Remove the event type field to demonstrate deletion.
    del incident["event_type"]

    # Display every key-value pair remaining in the dictionary.
    print("\nUpdated incident record")
    for key, value in incident.items():
        print(f"{key.replace('_', ' ').title()}: {value}")

    # len() returns the number of key-value pairs in the dictionary.
    print(f"\nTotal number of key-value pairs: {len(incident)}")


if __name__ == "__main__":
    main()
