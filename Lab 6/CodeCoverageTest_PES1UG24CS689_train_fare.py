
import pytest
from train_fare import base_fare, concession, tatkal_charge


def test_base_fare_valid_class():
    assert base_fare("SL", 500) == 500


def test_base_fare_minimum_fare():
    assert base_fare("SL", 10) == 50


def test_base_fare_unknown_class():
    with pytest.raises(ValueError):
        base_fare("INVALID", 500)


def test_base_fare_invalid_distance():
    with pytest.raises(ValueError):
        base_fare("SL", 0)


def test_concession_tatkal():
    assert concession(5, "M", True) == 0


def test_concession_child_under_five():
    assert concession(4, "M", False) == 100


def test_concession_child():
    assert concession(10, "M", False) == 50


def test_concession_senior_female():
    assert concession(65, "F", False) == 50


def test_concession_senior_male():
    assert concession(65, "M", False) == 40


def test_concession_adult():
    assert concession(30, "M", False) == 0


def test_tatkal_sleeper():
    assert tatkal_charge("SL", 500) == 100


def test_tatkal_other_class():
    assert tatkal_charge("3A", 500) == 150


def test_tatkal_charge_maximum():
    assert tatkal_charge("3A", 2000) == 400


def test_tatkal_charge_minimum():
    assert tatkal_charge("3A", 100) == 100
