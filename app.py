from flask import Flask, request, jsonify
from bose.launch_tasks import launch_tasks
from src import tasks_to_be_run
from src.config import queries


app = Flask(__name__)

@app.post("/search")
def search():
    if request.is_json:
        query = request.get_json()
        industry = query["industry"]
        location = query["location"]
        max_count = query["max_count"]

        keyword = industry + " in " + location
        queries[0]["keyword"] = keyword
        queries[0]["max_results"] = max_count
        launch_tasks(*tasks_to_be_run)
        return query, 201
    return {"error": "Request must be JSON"}, 415