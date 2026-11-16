"""Fuzz malformed inputs and preserve the application's valid-input behavior."""

from string import ascii_letters

from hypothesis import given, settings, strategies as st

from highway_toll import parse_plate, trip_cost, axle_class


# Repeatable generation and one minimized failure per test keep the lab output
# easy to inspect. Exceptions are deliberately allowed to fail the tests.
fuzz_settings = settings(
    max_examples=200,
    derandomize=True,
    report_multiple_bugs=False,
    deadline=None,
)


@fuzz_settings
@given(st.text() | st.none())
def test_parse_plate_no_crash(s):
    parse_plate(s)


@fuzz_settings
@given(st.text() | st.none())
def test_trip_cost_no_crash(s):
    trip_cost(s)


@fuzz_settings
@given(st.text() | st.none())
def test_axle_class_no_crash(s):
    axle_class(s)


@fuzz_settings
@given(
    state=st.text(alphabet=ascii_letters, min_size=2, max_size=2),
    district=st.integers(min_value=0, max_value=99),
    series=st.text(alphabet=ascii_letters, min_size=1, max_size=3),
    number=st.integers(min_value=0, max_value=9999),
)
def test_valid_plate_returns_normalized_fields(state, district, series, number):
    plate = f"{state}-{district:02d}-{series}-{number:04d}"
    assert parse_plate(plate) == (state.upper(), district, number)


@fuzz_settings
@given(
    count=st.integers(min_value=0, max_value=10**9),
    rate=st.integers(min_value=0, max_value=10**9),
    separator=st.sampled_from(["x", "X"]),
)
def test_valid_trip_cost_is_product(count, rate, separator):
    assert trip_cost(f"{count}{separator}{rate}") == count * rate


@fuzz_settings
@given(
    case=st.sampled_from(
        [(2, "car"), (3, "truck"), (4, "truck"), (5, "heavy"), (100, "heavy")]
    )
)
def test_valid_axle_class_boundaries(case):
    axles, expected = case
    assert axle_class(str(axles)) == expected
