from flask import Flask, render_template, request
from planner import load_places, generate_itinerary

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    itinerary = None
    city = "Poznań"
    days = 2
    error = None

    if request.method == "POST":
        city = request.form.get("city", "Poznań")
        try:
            days = int(request.form.get("days", 2))
            if days < 1 or days > 7:
                error = "Please enter a number of days between 1 and 7."
            else:
                itinerary = generate_itinerary(days=days)
        except ValueError:
            error = "Invalid number of days."

    all_places = load_places()
    return render_template(
        "index.html",
        city=city,
        days=days,
        itinerary=itinerary,
        all_places=all_places,
        error=error
    )


if __name__ == "__main__":
    app.run(debug=True, port=5000)