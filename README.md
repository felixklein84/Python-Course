# Applied Python Course

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-Apache%202.0-lightgrey)
![Sessions](https://img.shields.io/badge/Sessions-7-green)

A hands-on Python course for beginners in data analysis. Originally developed and taught at a university in India, the course takes students from zero programming experience to building interactive data dashboards across 7 sessions.

The materials are structured as a complete teaching resource: each session has a lecture notebook, exercises, and solutions. Everything can also be used independently for self-study.

---

## What You Will Learn

| Session | Topic | Skills |
|---------|-------|--------|
| 1 | Syntax and data types | Variables, types, basic operations |
| 2 | Functions and Jupyter | Control flow, functions, notebook workflow |
| 3 | NumPy | Arrays, vectorized computation, random numbers |
| 4 | Pandas and Matplotlib | DataFrames, data cleaning, basic plots |
| 5 | Seaborn and Plotly | Statistical plots, interactive visualizations |
| 6 | Code quality | Linting with pylint, formatting with Black, docstrings |
| 7 | Dash applications | Building interactive web dashboards |

---

## Who This Is For

- Beginners with no prior programming experience
- Students who want to apply Python to real data problems
- Instructors looking for a complete, ready-to-use course structure

No prior coding knowledge required. Basic familiarity with spreadsheets is helpful.

---

## Repository Structure

```
Python-Course/
├── lec01/              # Syntax and data types (plain Python scripts)
│   ├── agenda.md       # Session plan
│   ├── *.py            # Lecture scripts and exercises
├── lec02/              # Functions and Jupyter setup
│   ├── *.md            # Setup guides
│   └── *.ipynb         # Lecture and exercise notebooks
├── lec03/              # NumPy
├── lec04/              # Pandas and Matplotlib
├── lec05/              # Seaborn and Plotly
├── lec06/              # Code quality tooling
├── lec07/              # Dash application
├── exams/
│   ├── zertifikat1/    # Certificate exam 1 (with dataset)
│   └── zertifikat2/    # Certificate exam 2 (with dataset)
├── mock_exam/          # Practice exam (with dataset)
├── pyproject.toml      # Dependency management via Poetry
├── poetry.lock
└── SetupIDE_Environment.md
```

Each lecture folder follows the same pattern:
- `*_empty.ipynb` — lecture notebook (blank, for live coding)
- `*_filled.ipynb` — lecture notebook (with solutions)
- `*_exercise.ipynb` — exercise for students
- `*_exercise_solution.ipynb` — solution to the exercise
- `agenda.md` — session plan with time estimates

---

## Setup

### Prerequisites

- [Python 3.8+](https://www.python.org/downloads/)
- [Poetry](https://python-poetry.org/docs/#installation)
- [VS Code](https://code.visualstudio.com) (recommended)

For a full step-by-step walkthrough, see [SetupIDE_Environment.md](SetupIDE_Environment.md).

### Quick Start

```shell
# 1. Clone the repository
git clone https://github.com/<your-username>/python-course.git
cd python-course

# 2. Configure Poetry to create the virtual environment inside the project
poetry config virtualenvs.in-project true

# 3. Install all dependencies
poetry install

# 4. Open a notebook
poetry run jupyter notebook
```

The virtual environment is created in `.venv/` inside the project folder. In VS Code, select this interpreter via **Select Python Interpreter** in the Command Palette.

### Dependencies

| Package | Purpose |
|---------|---------|
| `numpy` | Numerical arrays and computation |
| `pandas` | Tabular data handling |
| `matplotlib` | Basic plotting |
| `seaborn` | Statistical visualization |
| `plotly` | Interactive charts |
| `dash` | Web-based dashboards |
| `pylint` | Static code analysis |
| `black` | Code formatting |

---

## Exams

The `exams/` folder contains two graded certificate exams and one mock exam. Each includes a task description (`tasks.md`) and the required dataset.

All exams are open-book, 45 minutes, and cover NumPy, pandas, and visualization.

---

## License

Apache 2.0 — see [LICENSE](LICENSE).
