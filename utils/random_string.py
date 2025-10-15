import random
import string


def generate_random_name() -> str:
    """
    Generate a random string for testing (e.g., fake full name).

    1. Create a random word of 6 alphabetic characters (mixed case).
    2. Create a random 3-digit number.
    3. Join them -> e.g. 'sGeoRD256'
    4. Reverse the final string -> '652DRoeGs'
    """
    # Part 1: random letters (6 total, mixed upper/lower)
    letters = "".join(random.choice(string.ascii_letters) for _ in range(6))

    # Part 2: random 3-digit number (100–999 inclusive)
    digits = str(random.randint(100, 999))

    # Part 3: join both parts
    combined = letters + digits
    print("\n Original combined string:", combined)

    # Part 4: reverse result
    reversed_combined = combined[::-1]

    return reversed_combined  # Could be returned strictly combined[::-1]
