import nose
import acp_times
import arrow

def test_first_gate():
    assert acp_times.open_time(0, 200, arrow.get("2021-05-01T00:00")) == arrow.get("2021-05-01T00:00")
    assert acp_times.close_time(0, 200, arrow.get("2021-05-01T00:00")) == arrow.get("2021-05-01T01:00")

def test_mid_200km():
    assert acp_times.open_time(100, 200, arrow.get("2021-01-09T06:00")) == arrow.get("2021-01-09T08:56")
    assert acp_times.close_time(100, 200, arrow.get("2021-01-09T06:00")) == arrow.get("2021-01-09T12:40")

def test_end_200km():
    assert acp_times.open_time(200, 200, arrow.get("2021-01-09T06:00")) == arrow.get("2021-01-09T11:53")
    assert acp_times.close_time(200, 200, arrow.get("2021-01-09T06:00")) == arrow.get("2021-01-09T19:30")

def test_mid_1000km():
    assert acp_times.open_time(600, 1000, arrow.get("2000-03-10T12:00")) == arrow.get("2000-03-11T06:48")
    assert acp_times.close_time(600, 1000, arrow.get("2000-03-10T12:00")) == arrow.get("2000-03-12T04:00")

def test_end_1000km():
    assert acp_times.open_time(1000, 1000, arrow.get("2000-03-10T12:00")) == arrow.get("2000-03-11T21:05")
    assert acp_times.close_time(1000, 1000, arrow.get("2000-03-10T12:00")) == arrow.get("2000-03-13T15:00")
