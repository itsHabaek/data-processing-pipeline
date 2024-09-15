from flask import Flask, request, jsonify
import pandas as pd
from collections import OrderedDict
import importlib
import os

app = Flask(__name__)

# Dynamically load tasks
def load_tasks():
    task_dir = 'tasks'
    tasks = {}
    for filename in os.listdir(task_dir):
        if filename.endswith('.py') and filename != '__init__.py':
            task_name = filename[:-3]
            module = importlib.import_module(f'tasks.{task_name}')
            # Function name should match the task file name exactly
            func_name = task_name  # e.g., 'identify_duplicate_rows'
            if hasattr(module, func_name):
                tasks[task_name] = getattr(module, func_name)
                print(f"Loaded function '{func_name}' from module '{module}'")
            else:
                print(f"Function '{func_name}' not found in module '{module}'")
    return tasks

task_library = load_tasks()

@app.route('/run_pipeline', methods=['POST'])
def run_pipeline():
    data = request.json
    tasks = data.get('tasks', [])
    file_path = data.get('file_path', '')
    df = pd.read_csv(file_path)
    report = OrderedDict()

    for task in tasks:
        task_params = data.get(f"{task}_params", {})
        if task in task_library:
            task_function = task_library[task]
            result = task_function(df, task_params)
            report[task] = result
        else:
            report[task] = "Task function not found"
    
    return jsonify(report)

if __name__ == '__main__':
    app.run(debug=True)
