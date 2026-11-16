# L6_L7_36 — Highway Toll Calculator

Lab 7: Fuzz Testing

## About

A small Python module that reads vehicle plates, prices trips and classifies vehicles by axle count.

## Files

| File | Description |
|------|-------------|
| `highway_toll.py` | The code under test |
| `test_highway_toll.py` | Starter test file |

## Deliverables

- `output/pdf/Lab_7_Fuzz_Testing_Report.pdf`: the four recorded screenshot checkpoints.
- `highway_toll.py`: the fixed application.
- `test_highway_toll.py`: the completed Hypothesis test suite.

The handout's generic names `processor.py` and `test_processor.py` correspond
to `highway_toll.py` and `test_highway_toll.py` in this assigned repository.

## Results and fixes

Before the fixes, the suite reported **3 failed, 3 passed**. Hypothesis found
`None` inputs that caused `AttributeError` in plate parsing and trip pricing,
and `TypeError` in axle classification. Valid-input properties already passed.
After fixing the application, the same six tests report **6 passed**.

Invalid function inputs now return `None`; the interactive application prints
a validation message and continues to the next prompt. Valid behavior remains:

- Plates contain four hyphen-separated fields. State and series must contain
  ASCII letters; district and number must contain nonnegative ASCII integers.
  Surrounding whitespace is accepted, and the returned state is uppercase.
- Trips use two nonnegative ASCII integers separated by `x` or `X`.
- Axle counts must be integers of at least two: 2 is a car, 3-4 a truck,
  and 5 or more heavy. Booleans and floats are rejected.

Type checks, field-count checks, numeric checks, and a narrow conversion-error
handler prevent malformed input from reaching unsafe string operations or
integer conversion. These checks validate this lab's input structure; they do
not verify whether a plate is registered or whether its state code exists.

The three crash properties generate Unicode text and `None`. The other three
check valid plate normalization, trip multiplication, and axle boundaries.
Hypothesis uses repeatable generation with up to 200 examples per property;
finite strategies may exhaust their examples earlier. Exceptions are not
suppressed in the tests, and finite fuzzing does not prove every input safe.

## Run

From `lab7`, using the environment prepared for this lab:

```bash
.venv/bin/python highway_toll.py
.venv/bin/python -m pytest test_highway_toll.py -v --tb=short
```

For a fresh environment with Python 3.8 or later, install the test dependencies
in your chosen environment with `python -m pip install hypothesis pytest`.
Recorded versions: Python 3.13.5, Hypothesis 6.170.15, pytest 8.3.4.

## Recorded checkpoints

1. `screenshots/01_original_application.png`: original valid-input output.
2. `screenshots/02_failing_tests.png`: failures before hardening.
3. `screenshots/03_fixed_application.png`: invalid inputs handled without a traceback.
4. `screenshots/04_passing_test.png`: all six tests pass after hardening.
