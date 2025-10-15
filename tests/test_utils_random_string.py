import re

from utils.random_string import generate_random_name


# I didn't add this test to workflow, it could be, probably, excessively
def test_generate_random_name_structure():
    result = generate_random_name()

    # Ensure the output length is 9
    assert len(result) == 9, f"Expected length 9, got {len(result)}"

    # Ensure only letters + digits
    assert re.match(r"^[A-Za-z0-9]+$", result), "Contains invalid characters"

    # Check that last 3 characters (before reversing → first 3 digits) are digits
    assert result[:3].isdigit(), f"Expected 3 digits at start, got: {result}"

    # Ensure there are 6 letters after digits
    assert result[3:].isalpha(), f"Expected 6 letters after digits, got: {result}"

    # There could be more unit tests, but for Demonstration purposes it's enough

    print(f"✅ Generated random name: {result}")
