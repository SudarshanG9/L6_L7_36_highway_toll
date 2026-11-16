# L6_L7_36 — Highway Toll Calculator

Lab 6: Code and Branch Coverage

## About

A small Python module that calculates toll charges by axle count, peak hours and electronic tag, and advises on monthly passes.

## Files

| File | Description |
|------|-------------|
| `highway_toll.py` | The module under test |
| `test_highway_toll.py` | Latest test suite, collected by default by pytest |
| `CodeCoverageTest_36_highway_toll.py` | Preserved line-coverage test deliverable |
| `BranchCoverageTest_36_highway_toll.py` | Branch-coverage test deliverable |
| `screenshots/line_coverage.png` | Recorded line-coverage results |
| `screenshots/branch_coverage.png` | Recorded branch-coverage results |

## Coverage stages

The assignment identifier `36` in the deliverable filenames comes from the
repository name. The application is unchanged; the tests exercise its behavior.

1. The two starter tests passed with 46% application line coverage.
2. `CodeCoverageTest_36_highway_toll.py` preserves the line-coverage stage:
   21 tests and 93% line coverage (26 of 28 statements). Lines 7 and 35 remained
   untested: the invalid-axle exception and the equal-cost pass recommendation.
   Its recorded terminal output is `screenshots/line_coverage.png`.
3. `BranchCoverageTest_36_highway_toll.py` extends those tests with invalid axle
   counts, exemption precedence, propagated errors, and pass-price boundaries.
   All 33 tests pass, covering all 28 statements and all 18 branch outcomes
   (100% line and branch coverage, with no missing or partial branches).
   Its recorded terminal output is `screenshots/branch_coverage.png`.
   `test_highway_toll.py` contains this latest suite for default pytest discovery.

Run each named suite explicitly so the two stages remain independently
reproducible. Coverage is restricted to `highway_toll`, so test-file execution
does not inflate the application's coverage percentage.

## Run from this folder

Use the same Python interpreter for pytest and coverage. On the current machine,
`/opt/anaconda3/bin/python3` has both installed. For another Python environment,
install them with `python3 -m pip install coverage pytest` and replace the
interpreter path below.

Line coverage:

```bash
/opt/anaconda3/bin/python3 -m coverage run --data-file=.coverage.line --source=highway_toll -m pytest CodeCoverageTest_36_highway_toll.py
/opt/anaconda3/bin/python3 -m coverage report --data-file=.coverage.line -m
```

Branch coverage:

```bash
/opt/anaconda3/bin/python3 -m coverage run --data-file=.coverage.branch --source=highway_toll --branch -m pytest BranchCoverageTest_36_highway_toll.py
/opt/anaconda3/bin/python3 -m coverage report --data-file=.coverage.branch -m
```

In the branch report, `Branch` counts possible decision outcomes and `BrPart`
counts partially covered decision points. With `--branch`, `Cover` combines
statement and branch coverage. A report with `Miss = 0`, `BrPart = 0`, no missing
entries, and `Cover = 100%` demonstrates full statement and branch coverage.

## Screenshot checkpoints and commits

The handout requires terminal screenshots only after each stage reaches at least
90%, with a separate commit for each stage's tests and screenshot.

- Line stage: capture the passing test summary and line report, save
  `screenshots/line_coverage.png`, then commit that stage before changing tests.
- Branch stage: capture the passing test summary and branch report, save
  `screenshots/branch_coverage.png`, then commit the branch stage.

Keep both named test deliverables and both screenshots in the repository.
