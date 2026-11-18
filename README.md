# Erasmus-sds
The main idea of this project is to develop a Travel Guide, which will be a software application designed to help travelers plan their visits to Poznan according to their interests and preferences. It provides informations about points of interest, such as monuments, museums, parks, and cultural or sports venues, and helps users organize their activities during their trip.

## Roles and Responsabilities
- Diego de Francisco (Product Owner) is responsible for:
  - Backlog Management: Prioritize, refine, and maintain user stories and features.
  - Developing and communicating Product Goal
  - Defining acceptance criteria (Definition of Done)
  - Review and approve completed sprint increments

- Ilies Guerda (Scrum Master & Developer) is responsible for:
  - making sure that communication works
  - making sure that we organize retrospectives
  - making sure that Scrum practices are followed
  - testing application features
  - reviewing code

- Gonzalo Martin (Developer) is responsible for:
  - Designing and implementing front-end user interfaces and back-end application features.
  - Implementing search, filtering, and personalized activity/itinerary planning logic based on user preferences.
  - Writing clean, maintainable, and well-documented code following team coding standards.
  - Collaborating with the Product Owner and Scrum Master to refine project requirements and acceptance criteria.
  - Developing and integrating features for points of interest (monuments, museums, parks, cultural, and sports venues).

- Rocío Gómez (Developer) is responsible for:
  - Designing and maintaining the data model and the catalog of Poznań points of interest (`places.json`).
  - Verifying the accuracy of place information (descriptions, official websites, visit durations).
  - Maintaining the project documentation (README, Definition of Done, data model, installation manual).
  - Implementing and testing the features assigned to her during Sprint Planning.

## Communication Strategy
We'll use a WhatsApp group chat for everyday communication, and video calls for our discussions and working sessions.

## Definition of Done
A Product Backlog Item is done when:
- All its acceptance criteria are satisfied and can be shown in a live demo.
- All non-trivial backend methods are unit-tested (`pytest`) and the tests pass automatically in GitHub Actions CI.
- The maximum response time to generate a visiting plan is under 5 seconds.
- The code is pushed to the `main` branch and the application runs following the installation manual.

## Data model (`places.json`)
Each point of interest is stored as one JSON object:

| Field | Type | Description |
|---|---|---|
| `id` | integer | Unique identifier of the place |
| `name` | string | Name of the place |
| `description` | string | Short description shown to the traveler |
| `website` | string (URL) | Official or tourist information website |
| `duration_outside` | integer (minutes) | Time needed to visit the place from the outside |
| `duration_inside` | integer (minutes) | Time needed to visit the inside (0 if not applicable) |
| `importance` | integer (0-100) | Priority used to order places in the plan (higher = more important) |
| `categories` | list of strings | Tags such as `historical`, `modern`, `art`, `culture`, `music`, `sport`, `park`, `bike`, `children`, `adults`, `sportsmen` |

## Installation manual
1. **Clone the repository:**
   ```bash
     git clone https://github.com/diedefsim/Erasmus-sds.git
    cd Erasmus-sds
   ```

2. **Create and activate a virtual environment (recommended):**
   ```bash
   python -m venv venv
   ```
   - Windows: `venv\Scripts\activate`
   - macOS / Linux: `source venv/bin/activate`

3. **Install required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run unit tests (optional verification):**
   ```bash
   pytest
   ```

5. **Start the application server:**
   ```bash
   python app.py
   ```

6. **Open in browser:**
   Navigate to `http://127.0.0.1:5000` in your web browser.
