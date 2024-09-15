Configurable Civic Data Processing Pipeline Framework

Overview
This repository provides a framework for building configurable data processing pipelines. The framework allows users to configure and trigger data pipelines through an API call. It includes several tasks for assessing and validating datasets, such as checking for missing values, identifying duplicate rows, verifying unit specifications, handling column limits, and more.

Features
API Integration: Trigger data pipelines via a REST API.
Configurable Tasks: Execute various data processing tasks based on user-defined parameters.
Dynamic Task Loading: Add or modify tasks easily by creating or updating Python files.
Column Limit Check: Warns if the dataset contains exactly 255 columns, potentially indicating truncation by Apple's Numbers app.

Prerequisites
Python 3.6 or later
Flask
Pandas


Directory Structure
tasks/: Directory containing individual task modules.

__init__.py: (Empty) file to make the directory a package.
identify_missing_values.py: Task to identify missing values in specified columns.
identify_duplicate_rows.py: Task to identify duplicate rows in the dataset.
check_units.py: Task to check for missing unit specifications in the dataset.
check_column_limit.py: Task to check if the dataset has exactly 255 columns.
PipelineApi.py: Flask application to handle API requests and run tasks.

Task Implementation
Task: identify_missing_values
Checks for missing values in specified columns and compares against a tolerable percentage.

Parameters:

columns: List of column names to check.
thresholds: Dictionary with columns as keys and tolerable percentage of missing values as values.
Task: identify_duplicate_rows
Identifies duplicate rows or duplicate values in specified columns.

Parameters:

columns: List of columns to check for duplicates.
check: Defines whether to check for full row duplicates or column-specific duplicates.
Task: check_units
Identifies columns where unit information is missing.

Parameters:

columns: List of columns to check.
unit_info: Dictionary with column names as keys and unit descriptions as values.
Task: check_column_limit
Checks if the dataset contains exactly 255 columns and warns if so.

Parameters:

No additional parameters required.


Running the Application

python PipelineApi.py

Send a POST Request to Trigger a Pipeline:

Use a tool like Postman to send a POST request to http://localhost:5000/run_pipeline with the following JSON payload:

{
    "tasks": ["identify_missing_values", "identify_duplicate_rows","check_units","check_column_limit"],
    "file_path": "Assignment Task _ Dataset - Sheet1.csv",
    "identify_missing_values_params": {
        "columns": ["Email", "Name"],
        "thresholds": {
            "Email": 0,
            "Name": 10
        }
    },
    "identify_duplicate_rows_params": {
        "columns": ["Email"]
    },
     "check_units_params": {
        "columns": ["Weight", "Cost"],
        "unit_info": {
            "Weight": "kg",
            "Cost": "Rs"
        }
    }
}


Adding or Modifying Tasks
Add a New Task:

Create a new Python file in the tasks/ directory.
Implement the task function following the provided template.
Ensure the function name matches the task file name.
Modify an Existing Task:

Update the relevant Python file in the tasks/ directory.
Ensure the function name and parameters match those expected in PipelineApi.py.


Testing
Unit Testing: Create test cases for individual tasks to ensure correctness.
Integration Testing: Test the API endpoints with various payloads to validate the end-to-end process.



Contact
For any questions or issues, please contact [surajsinghm16@gmail.com].





