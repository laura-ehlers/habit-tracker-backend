from flask import Flask, jsonify, request
from flask_cors import CORS
import json
import uuid

from habit import Habit
import time

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r"/*": {"origins": "*"}})

HABITS = [
    {
        "id": uuid.uuid4().hex,
        "habit_name": "Drink water",
        "category": "Health",
        "periodicity": "Daily",
        "date_created": str(time.time()).split(".")[0],
        "streak": 0,
        "checked": True,
    },
    {
        "id": uuid.uuid4().hex,
        "habit_name": "Exercise",
        "category": "Fitness",
        "periodicity": "Daily",
        "date_created": str(time.time()).split(".")[0],
        "streak": 0,
        "checked": False,
    },
    {
        "id": uuid.uuid4().hex,
        "habit_name": "Read",
        "category": "Personal Development",
        "periodicity": "Daily",
        "date_created": "1709293664",
        "streak": 0,
        "checked": True,
    },
    {
        "id": uuid.uuid4().hex,
        "habit_name": "Meditate",
        "category": "Mental Health",
        "periodicity": "Daily",
        "date_created": str(time.time()).split(".")[0],
        "streak": 0,
        "checked": False,
    },
    {
        "id": uuid.uuid4().hex,
        "habit_name": "Write",
        "category": "Creativity",
        "periodicity": "Daily",
        "date_created": str(time.time()).split(".")[0],
        "streak": 0,
        "checked": True,
    },
]


@app.route("/habits", methods=["GET", "POST"])
def add_habit():
    response_object = {"status": "success"}
    if request.method == "POST":
        post_data = request.get_json()
        HABITS.append(
            {
                "uuid": uuid.uuid4().hex,
                "habit_name": post_data.get("habit_name"),
                "category": post_data.get("category"),
                "periodicity": post_data.get("periodicity"),
                "date_created": str(time.time()).split(".")[0],
                "streak": post_data.get("streak"),
                "checked": post_data.get("checked"),
            }
        )
        response_object["message"] = "Habit added!"
    else:
        response_object["habits"] = HABITS
    return jsonify(response_object)
    # habit = Habit("Drink water", "Health", "Daily", date_created)

    # return json.dumps(habit.__dict__)


@app.route("/habits/<habit_id>", methods=["PUT", "DELETE"])
def single_habit(habit_id):
    response_object = {"status": "success"}
    if request.method == "PUT":
        post_data = request.get_json()
        remove_habit(habit_id)
        HABITS.append(
            {
                "uuid": uuid.uuid4().hex,
                "habit_name": post_data.get("habit_name"),
                "category": post_data.get("category"),
                "periodicity": post_data.get("periodicity"),
                "date_created": post_data.get("date_created"),
                "streak": post_data.get("streak"),
                "checked": post_data.get("checked"),
            }
        )
        response_object["message"] = "Habit updated!"
    if request.method == "DELETE":
        remove_habit(habit_id)
        response_object["message"] = "Habit removed!"

    return jsonify(response_object)


def remove_habit(habit_id):
    for habit in HABITS:
        if habit["id"] == habit_id:
            HABITS.remove(habit)
            return True
    return False
