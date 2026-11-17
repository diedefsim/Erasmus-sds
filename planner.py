import json
import os

DAILY_LIMIT_MINUTES = 360  # Standard 6-hour daily sightseeing limit


def load_places(filepath=None):
    if filepath is None:
        filepath = os.path.join(os.path.dirname(__file__), "places.json")
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)


def generate_itinerary(days, places=None):
    if days < 1:
        raise ValueError("Number of days must be at least 1.")
    if places is None:
        places = load_places()

    sorted_places = sorted(places, key=lambda p: p.get("importance", 0), reverse=True)

    itinerary = []
    used_ids = set()

    for day_num in range(1, days + 1):
        day_places = []
        current_time = 0

        for place in sorted_places:
            if place["id"] in used_ids:
                continue
            total_visit_time = place["duration_outside"] + place["duration_inside"]
            if current_time + total_visit_time <= DAILY_LIMIT_MINUTES:
                place_copy = dict(place)
                place_copy["total_duration"] = total_visit_time
                day_places.append(place_copy)
                used_ids.add(place["id"])
                current_time += total_visit_time

        itinerary.append({
            "day": day_num,
            "total_minutes": current_time,
            "total_hours_str": f"{current_time // 60}h {current_time % 60:02d}m",
            "places": day_places
        })

    return itinerary