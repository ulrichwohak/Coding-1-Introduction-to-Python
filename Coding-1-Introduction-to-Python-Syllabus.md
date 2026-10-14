# Coding 1: Introduction to Python (ECBS5208)

**Academic year** 2026–2027 · **Term** Fall · **Host unit** Department of Economics
**Course level** 7 · **US credits** 1 · **ECTS credits** 2
**Instructor** Ulrich Wohak, PhD
**Meetings** Wednesdays, 15:40–17:20 · 16 September – 21 October 2026 (6 sessions) · Room TBC
**Course repository** `Coding-1-Introduction-to-Python`

---

## Background and overall aim

**Content.** This course introduces students to the basics of Python programming with a
focus on data handling, visualization, and foundational scripting. It is designed as a
beginner-level coding course specifically for students aiming to analyze and work with
data using Python. The course is built around interactive notebooks and real datasets,
enabling students to learn by doing.

**Relevance.** Python is de facto the lingua franca in data engineering, data science, and
data analytics. Most data solutions are deployed in production environments in Python, so
anyone looking for a position in the data world must be able to code in this language.

**Position in the sequence.** Coding 1 is the foundational course of the coding sequence.
Its purpose is to build the baseline programming literacy that every later course assumes:
reading code, writing it by hand, and reasoning about why it fails. Coding 2 (ECBS5306),
which follows in the same term, builds on this foundation and is where AI-assisted coding
is introduced. See the AI policy below.

## Course prerequisites

- Mathematics pre-session course.
- Students are expected to bring their own laptops to follow the coding classes.

No prior programming experience is assumed. Students should complete the environment setup
described in `modules/module00-intro/setup.md` before or during Session 1.

## Waiting list handling

MS in Business Analytics students and MA in Economics, Data and Policy students have first
priority. All other students will be placed on the waiting list.

## Learning outcomes

**Key outcomes.** By the end of the course, students will be able to:

- Write and debug basic Python programs.
- Use key data structures like lists and dictionaries.
- Read from and write to files.
- Work with structured datasets using pandas.
- Create visualizations using matplotlib and plotnine.
- Use loops, conditionals, and functions to automate tasks.
- Inspect and summarize data with pandas. Further exploratory data analysis is optional.

**Other outcomes.** The course will also help develop skills in the following areas:

- *Critical thinking* — reproduce errors and debug broken code.
- *Quantitative reasoning* — break down tasks into manageable components.
- *Technology skills* — learn Python's modelling tools and plotting libraries.
- *Interpersonal communication skills* — ability to interpret and communicate outputs.

**Supporting outcomes specific to this delivery.** Students will additionally be able to
work in a reproducible project environment managed by `uv`, use JupyterLab as a structured
environment for exploratory coding, construct reliable file paths with basic encoding
awareness. Exception handling is available as an optional extension outside the exam scope.

## Learning activities and teaching methods

The course will be conducted as a series of interactive sessions during which we go through
concepts and applications together. In addition, students will have in-class quizzes and
graded in-class assignments at the end of Sessions 2, 3, 5, and 6. The Session 4
assignment on 7 October did not take place and does not count towards the grade.

Each session follows the same shape:

1. A short start-of-class quiz on the previous session (from Session 2 onward).
2. Live-coded walkthrough of the session's module notebook(s) from `modules/`.
3. A 10-minute graded in-class assignment, completed and committed before you leave the
   room (Sessions 2, 3, 5, and 6; the Session 4 assignment was cancelled).

All materials are distributed through the course repository. Students clone the repository,
create the environment with `uv sync`, download external datasets with
`uv run python scripts/fetch_data.py`, and work in JupyterLab. Students type their own code:
notebooks are worked through by hand, not by pasting completed solutions.

**Voluntary practice.** The repository also contains a set of short practice notebooks in
`exercises/`, one or two per module. These are optional, are not collected, and are not
graded. They exist purely so that you can rehearse the material at your own pace. Work
through them at home if you find them useful, and skip them if you do not.

The no-AI policy applies to them as it does to everything else in this course. They are
where you build the syntax recall that the closed-book exam tests, so they are precisely the
place where handing the work to a tool costs you most.

## Assessment

Grading will be based on the total score out of 100, in line with CEU Department of
Economics and Business grading guidelines. In particular:

a. The median student can expect to get a B+.
b. Probably not more than 1/3 of the students can expect to get an A or A−.
c. The passing grade is 50%.

The final grade is based on:

| Component | Weight | Detail |
| --- | --- | --- |
| Start-of-the-class quiz | 20% | 5 quizzes at the start of Sessions 2–6, 4% each. Short, closed-book, on the previous session's material. |
| In-class assignments | 20% | 4 assignments, 5% each, at the end of Sessions 2, 3, 5, and 6 (23 September, 30 September, 14 October, and 21 October). The 7 October assignment did not take place and is excluded, not scored as zero. Completed and committed during class; nothing is done or submitted from home. |
| Closed-book final exam | 60% | Written, closed-book, no computer. Covers the core course material; optional Modules 08–10 are excluded. **Friday, 6 November 2026 at 13:30.** The exam is separate from the six teaching sessions. |

### In-class assignments

The last ten minutes of Sessions 2, 3, 5, and 6 are a short, graded assignment.
It asks you to *read* code rather than write it, which is the harder and more useful skill
at this stage.

The assignment planned for Session 4 (7 October) could not take place because the
assignment repository was unavailable to students. It is excluded for everyone, with
no penalty. Each of the four remaining assignments contributes 5% of the final grade,
so the assignment component remains 20%.

**What you will do.** At the end of the session I publish a small assignment repository and
give you the link. You **fork** it to your own GitHub account, which gives you your own copy
to work in. It contains a README with the task and a short Python script, typically five or
six lines of code, using the concepts we covered that day. Question prompts may already be
included as comments; you add your own answers below them. Depending on the session, that means
one of:

- **Naming the mechanism.** Against each block, say which concept from the module it relies
  on and what it produces.
- **Predicting, then verifying.** Before running anything, write down the value you expect a
  line to produce. Commit that. Then run the script and, in a second commit, correct the
  predictions you got wrong. Being wrong costs you nothing here; not trying does.
- **Explaining a failure.** The script raises an error. On the offending line, say why.
  Do not fix it.
- **Documenting a function.** Write a docstring that states what the function takes, what it
  returns, and what it assumes.

Then you commit your work and push it to your fork before you leave the room. That is the
whole assignment. You do not need to send me anything: GitHub lists the forks of a
repository, so I collect them from there. Give me your GitHub username once, in Session 1,
and that is the last piece of admin you owe me. There is nothing to finish at home, nothing
to hand in later, and no deadline to track: it is done when the session ends.

You will not be marked on prose style, spelling, or how much you wrote. A good comment says
*why* a line exists or names the mechanism at work; a poor one restates the syntax. Marking
is coarse, out of two points:

- **2** — comments explain intent or name the mechanism at work.
- **1** — comments are present but restate the syntax (`# loop over the list`).
- **0** — no commit inside the class window, or no comments added.

Session 1 has no graded assignment. It is used instead to walk through the setup and the
submission workflow, so that the mechanics are not what costs you marks in Session 2.

From time to time I will ask someone to talk me through one of their own comments.

Because the final exam is closed-book and handwritten, the quizzes and these assignments
are deliberately designed to build recall and comprehension rather than reliance on lookup.

## AI policy

**The use of AI is not allowed in this course.**

This course is introductory, and we are mostly going to be learning a lot of basic syntax.
For that reason, the use of AI is not permitted for any part of the course: the
start-of-class quizzes, the in-class assignments, the final exam, and the voluntary practice
notebooks alike. You are expected to write your code by hand, read error messages yourself,
and work out what went wrong. That difficulty is the point — it is where the learning
happens, and the closed-book final exam is set on the assumption that you have done it.

The prohibition covers the voluntary practice notebooks even though they are never
collected. That is not an oversight. Those notebooks are your rehearsal for an exam you will
sit without a computer, and they are the one place where the cost of using a tool falls
entirely on you.

I define "AI" here as LLM and other machine learning methods including ChatGPT, GitHub
Copilot, Bard, Claude, Grammarly, DeepL, and any other available tools. This includes
AI-completion features built into editors: if you use VS Code, disable Copilot and any
inline AI suggestions for your course work.

**This policy is specific to Coding 1, and it changes in the next course.** Coding 2
(ECBS5306) permits AI as an assistant that helps you code and debug faster, rather than as a
substitute for doing the work. The reason for the order is straightforward: you can only
judge whether an AI-generated solution is correct, efficient, or appropriate if you can
already read and write the code yourself. Coding 1 builds that judgment; Coding 2 puts it to
use.

What is permitted in Coding 1: the official documentation for Python, pandas, plotnine, and
matplotlib; the course notebooks; textbooks and course notes; and discussing concepts with
classmates. What is not permitted: generating, completing, translating, or explaining code
with an AI tool.

## Course contents

The course runs over six 100-minute sessions. Teaching units live in `modules/`; a session
can cover more than one module. Pandas continues through Session 4. Session 5 covers
conditionals and control flow, followed immediately by functions, and Session 6 covers
graphing. Sessions 2, 3, 5, and 6 end with a graded in-class assignment. The Session 4
assignment was cancelled and is not counted.
The practice notebooks in `exercises/` are voluntary and are never collected.

### Sessions 1–3

**Session 1 — 16 September · Setup and general coding principles**

- Python, JupyterLab, and VS Code; the `uv`-managed project environment; running a script
  from the console.
- Version control: what Git and GitHub are for, why tracking changes matters, and where
  they sit in a working data project. This is an overview, not a Git course — you will learn
  the tool properly later in the program. What we do cover in full is the one workflow you
  need here: fork the assignment repository, edit it, commit, push. Every in-class assignment
  from Session 2 onward is handed in that way, so we walk through it end to end and make sure
  it works on your laptop before you are graded on it. Bring a GitHub account, or create one
  in this session.
- General coding principles: how to name variables, why and how to comment scripts.
- Variables, assignment, and the primitive types (integers, floats, booleans); expressions
  and operators; string manipulation and formatting.
- Materials: `modules/module00-intro`, `modules/module01-coding-basics`.
- Voluntary practice: `exercises/module01-coding-basics-i.ipynb`,
  `exercises/module01-coding-basics-ii.ipynb`.
- **No graded assignment.** The session closes with a walkthrough of the submission
  workflow and a first practice commit, so the mechanics are settled before they carry
  marks.

**Session 2 — 23 September · Basic data structures and file I/O**

- The four Python collections: lists, tuples, sets, dictionaries. Inspecting, searching,
  modifying, and iterating; set operations; casting between collection types.
- JSON strings to dictionaries and back.
- Opening files for reading, reading text line by line, handling encodings; writing,
  appending, and overwriting; working directories, listing files, OS-specific paths,
  creating directories.
- Materials: `modules/module02-basic-structures`, `modules/module03-data-IO`.
- Voluntary practice: `exercises/module02-basic-structures-i.ipynb` through
  `exercises/module03-data-io-ii.ipynb`.
- **In-class assignment (10 min):** predict-then-verify. Read a short script using variables,
  a dictionary lookup, and simple arithmetic. Comment the code, predict its two printed
  values, commit, then run and correct any wrong prediction.

**Session 3 — 30 September · Data containers: pandas**

- Creating `Series` and `DataFrame`s from series, dictionaries, and lists; access with `loc`
  and `iloc`; resetting the index; renaming columns; reading DataFrame metadata.
- Data munging: adding variables, splitting a character variable, type conversion, string
  methods on Series, filtering and tabulating values, missing values, replacing values,
  handling duplicates, chaining operations, and sorting.
- Data: hotels-vienna, hotels-europe.
- Materials: `modules/module04-pandas-basics`.
- Voluntary practice: `exercises/module04-pandas-basics-i.ipynb` through
  `exercises/module04-pandas-munging-ii.ipynb`.
- **In-class assignment 3 (10 min):** the lists exercise originally called `backup`.
  Predict the printed values, explain indexing, and identify the Python types. This
  replaced the planned pandas assignment.

### Sessions 4–6

**Session 4 — 7 October · Pandas continued**

- Inspecting the hotel DataFrame: columns, shape, data types, unique hotels, and value counts.
- Selecting and copying columns; calculating price per night; inspecting numerical
  summaries and missing ratings.
- Boolean filters: selecting affordable rooms and combining price and rating conditions
  to find good deals.
- Live class material: `modules/module04-pandas-basics/01_pandas_basics_duplicate.ipynb`.
- Voluntary practice: `exercises/module04-pandas-basics-i.ipynb`,
  `exercises/module04-pandas-basics-ii.ipynb`.
- **No graded assignment:** the planned assignment could not take place and is excluded
  from the grade. The other four assignments each carry 5% of the final grade.

**Session 5 — 14 October · Conditionals and control flow then functions**

- Conditionals and control flow: `if`/`elif`/`else`, `for` loops, `while` loops, and
  list comprehensions. A deliberate `while True` loop demonstrates manual interruption.
- Functions follow immediately: structure, arguments, return values, docstrings, `help`,
  `lambda` functions, and refactoring repeated code into reusable helpers.
- Materials, in order: `modules/module05-conditionals`, `modules/module06-functions`.
- Voluntary practice: `exercises/module05-control-flow-i.ipynb`,
  `exercises/module05-control-flow-ii.ipynb`, `exercises/module06-functions-i.ipynb`,
  `exercises/module06-functions-ii.ipynb`.
- **In-class assignment 4 (10 min):** predict the output of a short loop with an `if`
  condition and a function call, then explain `return` versus `print`. Answer two
  questions in comments without changing the code.

**Session 6 — 21 October · Graphing and wrap-up**

- matplotlib first: the `Figure` and `Axes` objects, line and bar plots, axis limits,
  labels, and legends. Students see the explicit, step-by-step plotting model first.
- plotnine second: the grammar of graphics, mappings, layers, and basic chart types.
- Course review and preparation for the closed-book final exam.
- Materials: `modules/module07-graphs-basics`; start with `02_matplotlib_intro.ipynb`,
  then use `01_plotnine_intro.ipynb`.
- Voluntary practice: `exercises/module07-matplotlib.ipynb`,
  `exercises/module07-plotnine-i.ipynb`, `exercises/module07-plotnine-ii.ipynb`.
- **In-class assignment (10 min):** comment a figure script, explaining what each call adds.

### Optional modules outside the exam scope

- **Module 08 — Data exploration:** further descriptive statistics, grouped summaries,
  distributions, hypothesis tests, and association. Materials:
  `modules/module08-data-exploration`; practice: `exercises/module08-data-exploration-i.ipynb`
  and `exercises/module08-data-exploration-ii.ipynb`.
- **Module 09 — Exception handling:** `try`/`except`, exception types, and responding to
  errors. Materials: `modules/module09-exception-handling`; practice:
  `exercises/module09-exceptions.ipynb`.
- **Module 10 — Introduction to regression:** a preview of Coding 2, including simple
  regression, predictions, and residuals. Materials: `modules/module10-intro-to-regression`;
  practice: `exercises/module10-regression-i.ipynb` and `exercises/module10-regression-ii.ipynb`.

These three modules are optional and are not examined in Coding 1. Basic pandas inspection,
summaries, and filtering already taught in Module 04 remain core material.

## Software and course materials

The course uses Python 3.12 with an environment managed by `uv`. After cloning the
repository:

```bash
uv sync
uv run python scripts/fetch_data.py
uv run jupyter lab
```

Do not use `pip`, `pipenv`, or `%pip`/`!pip` inside notebooks to manage the course
environment; `uv` is the only supported workflow, and the repository's checks enforce this.

Core packages: `pandas`, `numpy`, `plotnine`, `matplotlib`, `scipy`, `statsmodels`,
`skimpy`, `stargazer`, `jupyterlab`.

Datasets are not stored in the repository. `scripts/fetch_data.py` downloads them into
`data/raw/`: hotels-vienna, hotels-europe (prices and features), sp500, and billion-prices.
Sources are documented in `data/README.md`.

## Readings and further material

There is no required textbook. The following are supplementary and optional:

- Békés, G. and Kézdi, G., *Data Analysis for Business, Economics, and Policy* — the source
  of the datasets and case studies used throughout the course.
- Turrell, A., *Coding for Economists* — a useful companion for data exploration.
- The official documentation for Python, pandas, plotnine, and matplotlib. Learning to read
  documentation is itself a course objective.

Individual module READMEs list further material specific to each topic.

## Attribution

Selected module materials are adapted from the MIT-licensed
`gabors-data-analysis/da-coding-python` course materials, which credit Peter Duronelly,
Adam Vig, Agoston Reguly, and Gabor Bekes. See `NOTICE.md` for details.

## Contact details

Ulrich Wohak, PhD — instructor. <wohaku@ceu.edu>. Office hours to be announced.
