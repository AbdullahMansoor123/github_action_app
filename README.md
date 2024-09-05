# GitHub Action Test App

### Overview
This is a Python application designed to demonstrate Continuous Integration (CI) automation using GitHub Actions.

### Objective
The objective of this project is to understand how to set up and automate CI processes using GitHub Actions.

### Steps to Follow

1. **Open VS Code**: Launch Visual Studio Code to begin working on your project.
2. **Open Project Folder**: Navigate to the folder where your project will reside.
3. **Activate Your Environment**: Set up and activate your Python virtual environment (e.g., `python -m venv venv` and `source venv/bin/activate` or `venv\Scripts\activate` on Windows).
4. **Create a `requirements.txt` File**: List the dependencies required for your project in a `requirements.txt` file. Then, install them using `pip install -r requirements.txt`.
5. **Create a `README.md` File**: Write some basic information about your project, including the title and objective.
6. **Initialize a Git Repository**: Run `git init` to create a new Git repository.
7. **Set Up the GitHub Repository**: Follow the instructions in GitHub after creating a new repository to connect it to your local project in VS Code.
8. **Create a `src` Directory**:
   - Add a Python file (e.g., `math_operations.py`) in the `src` folder where you define your app functions.
   - Also, add an `__init__.py` file inside the `src` folder to make the functions callable from other files.
9. **Create a `tests` Directory**:
   - Name of directory should be `tests` because this is requirement of pytest to find this folder and run test functions.
   - Add a Python test file in the `tests` folder (e.g., `test_math_operations.py`) where you will write `pytest` functions to test the functions in `math_operations.py`.
   - Add an `__init__.py` file inside the `tests` folder.
10. **Set Up GitHub Actions**:
    - Create a directory for GitHub Actions workflows: `.github/workflows/`.
    - Inside it, create a YAML file (e.g., `python-app.yml`) to define the CI pipeline for your app.
    - To understand how to write this YAML file, check out [this video](https://youtu.be/ciqWMIf7Pz0?t=3956), which explains the YAML file's content and how to run it.
11. **Push Your Changes**:
    - After creating the YAML file and pushing your commits to GitHub, the CI process will start automatically.
    - You can monitor the progress in the **Actions** tab on GitHub.

---


