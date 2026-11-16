"""Validate toll inputs, returning None for invalid data instead of crashing."""


def _nonnegative_int(value):
    # Reject booleans and floats rather than silently converting them to counts.
    if type(value) is int:
        return value if value >= 0 else None
    if not isinstance(value, str):
        return None
    value = value.strip()
    if not value or not value.isascii() or not value.isdecimal():
        return None
    try:
        return int(value)
    except ValueError:
        # Python can reject excessively long integer strings.
        return None


def parse_plate(plate):
    """Parse STATE-DISTRICT-SERIES-NUMBER, or return None if malformed."""
    if not isinstance(plate, str):
        return None
    parts = plate.strip().split('-')
    if len(parts) != 4:
        return None
    state, district, series, number = (part.strip() for part in parts)
    if not all(part.isascii() and part.isalpha() for part in (state, series)):
        return None
    district = _nonnegative_int(district)
    number = _nonnegative_int(number)
    if district is None or number is None:
        return None
    return state.upper(), district, number

def trip_cost(text):
    """Price nonnegative integer trips x rate, or return None if invalid."""
    if not isinstance(text, str):
        return None
    parts = text.lower().split('x')
    if len(parts) != 2:
        return None
    count, rate = (_nonnegative_int(part) for part in parts)
    if count is None or rate is None:
        return None
    return count * rate

def axle_class(axles):
    """Classify integer axle counts of at least two; otherwise return None."""
    n = _nonnegative_int(axles)
    if n is None or n < 2:
        return None
    if n == 2:
        return 'car'
    if n <= 4:
        return 'truck'
    return 'heavy'

def main():
    print("==== Running parse_plate ====")
    user_input = input("Enter a plate (e.g. KA-05-AB-1234): ")
    result = parse_plate(user_input)
    if result is None:
        print("Invalid plate. Expected a plate such as KA-05-AB-1234.")
    else:
        print("State, District and Number:", result)

    print("\n==== Running trip_cost ====")
    user_input = input("Enter trips x rate (e.g. 3x150): ")
    result = trip_cost(user_input)
    if result is None:
        print("Invalid trip input. Expected nonnegative integers, such as 3x150.")
    else:
        print("Trip Cost:", result)

    print("\n==== Running axle_class ====")
    user_input = input("Enter an axle count (e.g. 3): ")
    result = axle_class(user_input)
    if result is None:
        print("Invalid axle count. Expected an integer of at least 2.")
    else:
        print("Vehicle Class:", result)

if __name__ == "__main__":
    main()
