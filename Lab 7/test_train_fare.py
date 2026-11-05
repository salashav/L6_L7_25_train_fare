from hypothesis import given, strategies as st
from train_fare import parse_pnr, journey_distance, berth_type


@given(st.one_of(st.text(), st.none()))
def test_parse_pnr_no_crash(s):
    parse_pnr(s)


@given(st.one_of(st.text(), st.none()))
def test_journey_distance_no_crash(s):
    journey_distance(s)


@given(st.one_of(st.text(), st.none()))
def test_berth_type_no_crash(s):
    berth_type(s)