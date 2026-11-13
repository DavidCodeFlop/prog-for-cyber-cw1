"""
Reusable cyber security utilities.

This module provides basic password checks, basic IPv4 format validation
and random password generation. These are learning examples, not a
replacement for production-grade identity or network security controls.
"""

import secrets
import string


def validate_password(password, minimum_length=10):
    """
    Check password length and whether it contains a letter, digit and symbol.

    Args:
        password (str): Password to assess.
        minimum_length (int): Minimum accepted number of characters.

    Returns:
        bool: True if all stated password requirements are met.
    """
    has_letter = any(character.isalpha() for character in password)
    has_digit = any(character.isdigit() for character in password)
    has_symbol = any(not character.isalnum() for character in password)

    return (
        len(password) >= minimum_length
        and has_letter
        and has_digit
        and has_symbol
    )


def validate_ip(ip_address):
    """
    Perform the basic four-octet IPv4 checks used in Task 3.

    Args:
        ip_address (str): Address to check.

    Returns:
        bool: True if there are four numeric octets from 0 to 255.
    """
    cleaned_address = ip_address.strip()

    if cleaned_address.count(".") != 3:
        return False

    octets = cleaned_address.split(".")
    if len(octets) != 4:
        return False

    for octet in octets:
        if not octet.isdigit():
            return False
        if not 0 <= int(octet) <= 255:
            return False

    return True


def generate_strong_password():
    """
    Generate a random password of 10–16 characters with character variety.

    Returns:
        str: A password containing uppercase, lowercase, numeric and symbol
        characters. The secrets module is used for stronger randomness.
    """
    password_length = secrets.randbelow(7) + 10

    # Include one character from each required category.
    password_characters = [
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.digits),
        secrets.choice("!@#$%^&*()-_=+?")
    ]

    # Fill the remaining positions from the combined character pool.
    character_pool = (
        string.ascii_uppercase
        + string.ascii_lowercase
        + string.digits
        + "!@#$%^&*()-_=+?"
    )

    for _ in range(password_length - len(password_characters)):
        password_characters.append(secrets.choice(character_pool))

    # Shuffle the characters so the required categories are not predictable.
    secrets.SystemRandom().shuffle(password_characters)
    return "".join(password_characters)
