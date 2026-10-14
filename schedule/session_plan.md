# Coding 1 2026 Session Plan

**ECBS5208 Coding 1: Introduction to Python**, Fall term 2026-2027.

Six sessions, Wednesdays 15:40-17:20 (100 minutes), 16 September to 21 October 2026. Dates
and times are taken from the TimeEdit allocation for `ECBS5208A_T1_2026`, Group A. Room TBC.

There is no reading week inside the course: the six sessions run on six consecutive
Wednesdays. The final exam takes place on **Friday, 6 November 2026 at 13:30**,
separately from the six teaching sessions.

| Session | Date | Topic | Module materials | In-class assignment | Voluntary practice (at home) |
| --- | --- | --- | --- | --- | --- |
| 1 | Wed 16 Sep | Setup and general coding principles | `modules/module00-intro`, `modules/module01-coding-basics` | none - workflow walkthrough and practice commit | `module01-coding-basics-i`, `module01-coding-basics-ii` |
| 2 | Wed 23 Sep | Basic data structures and file I/O | `modules/module02-basic-structures`, `modules/module03-data-IO` | predict-then-verify on variables, a dictionary lookup, and arithmetic | `module02-basic-structures-i`, `module02-basic-structures-ii`, `module03-data-io-i`, `module03-data-io-ii` |
| 3 | Wed 30 Sep | Data containers: pandas | `modules/module04-pandas-basics` | [Assignment 3: lists, indexing, and types](https://github.com/ulrichwohak/coding1-assignment-03-lists), originally `backup`; used instead of the planned pandas assignment | `module04-pandas-basics-i`, `module04-pandas-basics-ii`, `module04-pandas-munging-i`, `module04-pandas-munging-ii` |
| 4 | Wed 7 Oct | Pandas continued: inspecting and filtering hotel data | `modules/module04-pandas-basics/01_pandas_basics_duplicate.ipynb` (live class notebook) | cancelled: repository unavailable; excluded from grading, not a zero | `module04-pandas-basics-i`, `module04-pandas-basics-ii` |
| 5 | Wed 14 Oct | Conditionals and control flow, then functions | `modules/module05-conditionals`, then `modules/module06-functions` | [Assignment 4: conditionals, loops, and functions](https://github.com/ulrichwohak/coding1-assignment-04-plotting-control-flow); predict the output and explain `return` versus `print` | `module05-control-flow-i`, `module05-control-flow-ii`, `module06-functions-i`, `module06-functions-ii` |
| 6 | Wed 21 Oct | Graphing and wrap-up: matplotlib before plotnine | `modules/module07-graphs-basics` | comment a figure script, explaining what each call adds | `module07-matplotlib`, `module07-plotnine-i`, `module07-plotnine-ii` |

## Optional modules and exam scope

`module08-data-exploration`, `module09-exception-handling`, and
`module10-intro-to-regression` are optional and **outside the final exam scope**.
Their practice notebooks remain available in `exercises/`, with the same module prefixes.
The pandas inspection and summaries already taught in Module 04 remain core material;
making Module 08 optional does not exclude those earlier skills.

## Assessment delivery notes

- **Assignment numbers follow delivery, not session numbers.** Assignment 1 was
  ungraded practice; Assignment 2 ran on 23 September; Assignment 3 (formerly
  `backup`) ran on 30 September. No assignment took place on 7 October, so the
  next assignment on 14 October is Assignment 4, the third graded assignment.
- **Revised assignment weights.** The 7 October assignment did not take place because
  students could not access its repository. It is excluded for everyone, not scored as
  zero. The four assignments in Sessions 2, 3, 5, and 6 each contribute **5%** of the final
  grade (20% combined). The five quizzes remain 20% combined, and the final exam remains 60%.
- **Assignment repositories.** Each holds a README with
  the task, a short uncommented `.py` script using that session's concepts, and a
  rubric. Use `.py` rather than `.ipynb`: a comment-only change to a notebook produces an
  unreadable JSON diff, whereas in a script `git diff` shows exactly the added lines, so
  grading is reading a diff.
- **Distribution is fork-based.** One assignment repository per graded session, published
  at the end of the session; students fork it, commit to their fork, and push. Nothing is
  emailed: GitHub lists a repository's forks, so collection is just enumerating them
  (`gh api repos/OWNER/REPO/forks`), and each fork's compare view against the source shows
  exactly the lines a student added. Collect GitHub usernames in Session 1 to map forks to
  the roster.
- **Forks of a public repository are public.** This is the weak point of the scheme, and it
  is not AI: every student works on the same script, so a late forker can read an earlier
  one's comments. The 10-minute in-class window limits it, but does not close it. Options,
  cheapest first: rely on the window plus the occasional oral spot-check; vary the script
  across two or three variants per session; or make the source repository private and add
  students as collaborators, so forks inherit private visibility, at the cost of managing
  access each session.
- **Git is not taught here, but the submission workflow is.** Students learn Git properly in
  a later course. Session 1 gives an overview of version control and then covers the one
  workflow needed for the in-class assignments end to end: take the link, get the
  repository, edit, commit, push. Getting GitHub authentication working on every laptop is
  the part that will eat the clock. Keep a browser-based fallback ready - editing and
  committing in the GitHub web UI needs no local setup at all - in case the room runs short
  or a student's machine will not cooperate.
- **AI policy is blanket, matching the study guide.** No AI anywhere in the course,
  including the voluntary practice notebooks, even though those are never collected and use
  cannot be verified. The syllabus states the rationale rather than the enforcement.
- **Registrar wording.** The study guide calls the 20% component "Homework submissions".
  The syllabus now calls it "In-class assignments", since nothing is done or submitted from
  home. The weight is unchanged; the label may want aligning with the registrar.

## Notes

- **Exercise filenames follow the module, not the session.** Exercises are named
  `moduleNN-topic.ipynb`, matching the `modules/moduleNN-*` directory they practise.
  Sessions bundle several modules, so one session draws on several prefixes; use the table
  above to see which. This decoupling is deliberate: session packing may change, but an
  exercise always belongs to its module.
- **Session 4 records the actual class.** On 7 October, students developed
  `01_pandas_basics_duplicate.ipynb`: inspecting the hotel DataFrame, selecting columns,
  creating price per night, checking missing ratings, and filtering by price and rating.
- **Session 5 order.** Module 05 (conditionals and control flow) comes immediately before
  Module 06 (functions). The intentional `while True` example is interrupted manually;
  run that cell individually, not with Run All.
- **Session 6 order.** Module 07 starts with `02_matplotlib_intro.ipynb`, followed by
  `01_plotnine_intro.ipynb`, so students see the explicit `Figure`/`Axes` model first.
- **Modules 08–10 are optional** and not examinable in Coding 1. Regression previews
  Coding 2 (ECBS5306).
- **SQL is not taught in this course.** `modules/module01-coding-basics/README.md`,
  `modules/module02-basic-structures/`, and `exercises/module01-coding-basics-ii.ipynb`
  still contain SQL string-building examples inherited from the upstream material; they are
  not part of the syllabus.
