"""Lab 6, line-coverage stage: normal toll and monthly-pass scenarios."""

import pytest

from highway_toll import toll_for, toll_charge, pass_advice


def test_ambulance_is_exempt():
    assert toll_charge("ambulance", 2, False, False) == 0


def test_two_axle_base_toll():
    assert toll_for(2, False, False) == 100


@pytest.mark.parametrize(
    "axles, is_peak, has_fastag, expected",
    [
        (3, False, False, 150),
        (4, False, False, 250),
        (5, False, False, 400),
        (2, True, False, 125),
        (3, True, False, 187.5),
        (4, True, False, 312.5),
        (5, True, False, 500),
        (2, False, True, 90),
        (3, False, True, 142.5),
        (4, False, True, 237.5),
        (5, False, True, 380),
        (2, True, True, 112.5),
        (3, True, True, 178.12),
        (4, True, True, 296.88),
        (5, True, True, 475),
    ],
)
def test_toll_rates(axles, is_peak, has_fastag, expected):
    # Literal expected prices check the result independently of the implementation.
    assert toll_for(axles, is_peak, has_fastag) == expected


def test_non_exempt_vehicle_pays_toll():
    assert toll_charge("car", 2, True, True) == 112.5


def test_buy_pass_when_trips_cost_more():
    # 100 + 112.50 = 212.50, which exceeds the pass price.
    assert pass_advice([(False, False), (True, True)], 2, 200) == "buy_pass"


def test_pay_per_trip_when_pass_costs_more():
    assert pass_advice([(False, False), (True, True)], 2, 250) == "pay_per_trip"


def test_no_trips_with_paid_pass():
    assert pass_advice([], 2, 100) == "pay_per_trip"
