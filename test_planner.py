import pytest
from planner import load_places, generate_itinerary

def test_load_places():
    places = load_places()
    assert len(places) >= 15
    first = places[0]
    assert "name" in first
    assert "duration_outside" in first
    assert "duration_inside" in first
    assert "categories" in first

def test_generate_itinerary_days():
    plan = generate_itinerary(days=2)
    assert len(plan) == 2
    assert plan[0]["day"] == 1
    assert plan[1]["day"] == 2
    assert plan[0]["total_minutes"] <= 360
    assert plan[1]["total_minutes"] <= 360
    assert len(plan[0]["places"]) > 0

def test_invalid_days():
    with pytest.raises(ValueError):
        generate_itinerary(days=0)
