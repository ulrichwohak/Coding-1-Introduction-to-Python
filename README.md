# Coding 1: Introduction to Python

Course materials for **ECBS5208 Coding 1: Introduction to Python** at CEU, Department of
Economics. The course runs from **September 16, 2026** to **October 21, 2026**.

The full syllabus is in
[`Coding-1-Introduction-to-Python-Syllabus.md`](Coding-1-Introduction-to-Python-Syllabus.md).

## Course Overview

Coding 1 is an introductory programming course for students who are learning to use Python for data management and data analysis. The course focuses on general coding principles, Python syntax, reproducible project workflows, and environment management with `uv`.

The goal is to build a solid programming foundation before students move on to more advanced analytics work. Students will practice writing, reading, debugging, and organizing code in notebooks and small scripts while working with realistic tabular datasets.

This course will **not** use artificial intelligence tools or large language models. The subsequent course will actively use AI and LLMs, but Coding 1 deliberately focuses on programming basics first: understanding code, controlling the Python environment, manipulating data, and reasoning through errors without AI assistance.

## Course Structure

The course meets once per week for 100 minutes, on Wednesdays 15:40-17:20, for six sessions. The ordered plan is in `schedule/session_plan.md`.

The first sessions introduce the Python working environment, notebooks, variables, expressions, strings, core data structures, and file I/O. Pandas continues through 7 October. On 14 October, control flow and conditionals are followed immediately by functions; graphing follows on 21 October. Data exploration, exception handling, and introductory regression remain available as optional material outside the Coding 1 exam scope.

Materials are organized into **modules**, not one folder per class meeting. A session can cover more than one module. The remaining core sequence is:

1. [Module 05: Conditionals and control flow](modules/module05-conditionals/)
2. [Module 06: Functions](modules/module06-functions/)
3. [Module 07: Graphing](modules/module07-graphs-basics/) — matplotlib before plotnine

Assessment weights are 20% quizzes, 20% in-class assignments, and 60% final exam.
The 7 October assignment did not take place and is excluded for everyone. The four
assignments on 23 September, 30 September, 14 October, and 21 October are worth 5%
each; the cancelled assignment is not a zero.

## Course Materials

- `modules/`: adapted module notebooks from `module00-intro` through `module10-intro-to-regression`
- `exercises/`: short 10-20 minute practice notebooks for substantive class sessions
- `data/README.md`: dataset inventory and external source notes
- `scripts/fetch_data.py`: dataset fetch script for external OSF data used by selected modules
- `scripts/check_no_pip.py`: validation script that keeps student-facing materials on the `uv` workflow
- `scripts/check_notebooks.py`: notebook validation for JSON, kernel metadata, imports, syntax, and local data references
- `schedule/session_plan.md`: ordered session plan for the 2026 course
- `Coding-1-Introduction-to-Python-Syllabus.md`: the course syllabus, aligned with the CEU study guide entry for ECBS5208

### Live Class Notebooks

The notebooks ending in `_duplicate.ipynb` contain the code we developed together
in class. They sit alongside the prepared module notebooks:

- [Python basics: variables, numbers, and strings](modules/module01-coding-basics/coding_basics_duplicate.ipynb)
- [Collections: lists, tuples, dictionaries, and sets](modules/module02-basic-structures/basic_structures_duplicate.ipynb)
- [File paths with `os`](modules/module03-data-IO/data_IO_duplicate.ipynb)
- [Pandas: exploring and filtering hotel data](modules/module04-pandas-basics/01_pandas_basics_duplicate.ipynb)

To run them, use `uv sync` and then `uv run jupyter lab` from the repository root.
Run one cell at a time: the basics and collections notebooks retain examples that
raise errors (dividing a string, sorting a list containing numbers and a nested
list, and changing a tuple). After inspecting an error, continue with the next
cell. The control-flow notebook also has a deliberate infinite loop: run that cell
alone and use the notebook toolbar's Interrupt/Stop button to stop it. The pandas
notebooks read the prepared hotel CSV included in `modules/module04-pandas-basics/`.
Saved outputs are cleared before publication; rerun cells to see their results.

## Learning Outcomes

By the end of Coding 1, students should be able to:

- Work with a Python project environment managed by `uv`.
- Use JupyterLab notebooks as a structured environment for exploratory coding.
- Write clear Python code using variables, expressions, strings, functions, and common data structures.
- Read from and write to local files using reliable paths and basic encoding awareness.
- Load, inspect, clean, filter, transform, and summarize tabular data with pandas.
- Create basic visualizations with plotnine and matplotlib.
- Use conditionals, loops, comprehensions, and functions to make code reusable.

Optional extensions, outside the exam scope, cover exception handling, further
exploratory data analysis (including hypothesis tests and association), and introductory
regression. Basic pandas inspection and summaries taught in Module 04 remain core material.

## Pedagogical Position

Coding 1 is intentionally about fundamentals. Students are expected to develop enough fluency to understand what their code does, why errors happen, and how to evaluate data workflow results. AI-assisted programming is useful in later work, but this course first builds the baseline programming literacy needed to use those tools responsibly.

## Attribution

Selected module materials are adapted from the MIT-licensed `gabors-data-analysis/da-coding-python` course materials. See `NOTICE.md` for details.

## AI Attribution

AIA HAb SeCeNc Hin R GPT-5.5 Opus4.7 v1.0

This statement documents how this repository was created. It does not change the course policy: students in Coding 1 will not use artificial intelligence tools or large language models for course work.
