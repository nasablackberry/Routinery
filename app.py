from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# Sample routines data
routines = {
    "Morning Routine": [
        {"task": "Brush", "time": "5 minutes", "description": "Brush teeth"},
        {"task": "Shower", "time": "10 minutes", "description": "Take a quick shower"}
    ],
    "Evening Routine": [
        {"task": "Dinner", "time": "30 minutes", "description": "Have a healthy dinner"},
        {"task": "Read", "time": "20 minutes", "description": "Read a book"}
    ]
}

@app.route('/')
def index():
    return render_template('index.html', routines=json.dumps(routines))

@app.route('/add_routine', methods=['POST'])
def add_routine():
    routine_name = request.form['routine_name']
    if routine_name not in routines:
        routines[routine_name] = []
    return jsonify(routines)

@app.route('/add_task/<routine>', methods=['POST'])
def add_task(routine):
    task_name = request.form['task']
    time = request.form['time']
    description = request.form['description']
    routines[routine].append({"task": task_name, "time": time, "description": description})
    return jsonify(routines)

@app.route('/remove_task/<routine>/<int:task_index>', methods=['POST'])
def remove_task(routine, task_index):
    if routine in routines and 0 <= task_index < len(routines[routine]):
        routines[routine].pop(task_index)
    return jsonify(routines)

@app.route('/remove_routine/<routine>', methods=['POST'])
def remove_routine(routine):
    if routine in routines:
        del routines[routine]
    return jsonify(routines)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
