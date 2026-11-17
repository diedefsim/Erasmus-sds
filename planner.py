import json
import os

def load_places(filepath=None):
    if filepath is None:
        filepath = os.path.join(os.path.dirname(__file__), "places.json")
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)

def generate_itinerary(days, places=None, preferences=None, pace="standard"):
    if days < 1:
        raise ValueError("Number of days must be at least 1.")
    if places is None:
        places = load_places()

    daily_limit = 240 if pace == "relaxed" else 360

    def score_place(p):
        base_score = p.get("importance", 0)
        if preferences:
            matches = sum(1 for pref in preferences if pref in p.get("categories", []))
            base_score += matches * 50
        return base_score

    sorted_places = sorted(places, key=score_place, reverse=True)

    itinerary = []
    used_ids = set()

    for day_num in range(1, days + 1):
        day_places = []
        current_time = 0

        for place in sorted_places:
            if place["id"] in used_ids:
                continue
            total_visit_time = place["duration_outside"] + place["duration_inside"]
            if current_time + total_visit_time <= daily_limit:
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
