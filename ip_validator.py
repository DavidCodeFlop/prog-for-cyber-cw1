"""
Task 3: IP Address Validator
Performs the basic IPv4 structure and octet-range checks requested.
"""


def validate_ip(ip_address):
    """
    Check whether an input has four numeric octets in the range 0–255.

    Args:
        ip_address (str): The IP address supplied by the user.

    Returns:
        bool: True when the basic format checks pass; otherwise False.
    """
    cleaned_address = ip_address.strip()

    # Three dots must separate the four expected octets.
    if "." not in cleaned_address or cleaned_address.count(".") != 3:
        return False

    octets = cleaned_address.split(".")

    if len(octets) != 4:
        return False

    for octet in octets:
        # Empty sections and non-numeric values are not accepted.
        if not octet.isdigit():
            return False

        octet_value = int(octet)
        if octet_value < 0 or octet_value > 255:
            return False

    return True


def main():
    """Read an address and display the validation result."""
    entered_ip = input("Enter an IP address: ")

    if validate_ip(entered_ip):
        print("Valid IP address")
    else:
        print("Invalid IP address")


if __name__ == "__main__":
    main()
