# Lecture 04: Exploring DataFrames with pandas

## Start with a question

Can we find a hotel below EUR 100 per night with a guest rating of at least 4 out of 5? We use this question to learn how to explore a table, check the information available, and build a shortlist using pandas.

Start with [`02_pandas_data_munging.ipynb`](02_pandas_data_munging.ipynb). Despite its retained filename, it is a self-contained introduction to DataFrames: it loads a supplied CSV and does not require completing part one or generating any data first.

[`01_pandas_basics.ipynb`](01_pandas_basics.ipynb) remains available as an optional reference for constructing Series and DataFrames and working with indexes. It is not a prerequisite for the question-led lesson.

## Questions and operations

| Question | pandas operations |
| --- | --- |
| What hotels and information do we actually have? | `read_csv`, column selection, `head`, `shape`, `info`, `value_counts` |
| What does a typical night cost, and how much do prices vary? | `describe` on selected measurements |
| Does every hotel have a rating from both sources? | `isna` and counts of missing values |
| Which hotels meet our budget and guest-rating requirements? | Boolean conditions and `.loc` |
| Which qualifying hotels are cheapest? | `sort_values` and `head` |

Each section introduces a concrete question, shows a short code example with explanatory comments, and interprets the result. The focus is on reading and using a DataFrame, not memorising methods or calculating statistics.

The core lesson ends with a variation: a visitor has a different budget and wants the closest qualifying hotels rather than the cheapest. The three optional extensions cover converting distances into a new column, comparing median prices by star category, and saving a shortlist as a new CSV. Stop before these extensions if time is short.

## Learning outcomes

After the core lesson, students should be able to:

- Explain what a DataFrame's rows, columns, and index represent.
- Load a local CSV and distinguish the file on disk from the table in memory.
- Inspect dimensions, column types, categories, and numerical summaries.
- Distinguish a missing rating from a rating of zero.
- Select columns and filter rows with one or two conditions.
- Sort a filtered result and explain the limits of the resulting shortlist.
- Find the relevant method in the linked pandas documentation.

## Data and setup

Use the course Python environment and run the notebook from top to bottom. Its setup supports working from either the repository root or this lecture folder.

[`hotel_vienna_restricted.csv`](hotel_vienna_restricted.csv) is already included in the repository. No download is needed for this lesson. This existing prepared sample contains 217 distinct hotels, with one-night weekday quotes for the Vienna search area in November 2017. It includes nearby municipalities and star categories 3, 3.5, and 4; it is not a representative sample of all hotels or a source of current prices.

The CSV has 29 columns; the lesson selects eight. All primary guest ratings are present, while three alternative Tripadvisor ratings are missing. The data are unchanged by this lesson revision. Optional export writes a separate file inside a Git-ignored `scratch` folder.

For data definitions, including prices in EUR, and educational-use terms, see the [Hotels Europe dataset description](https://gabors-data-analysis.com/datasets/hotels-europe/). See also the repository's [data inventory](../../data/README.md) and [attribution notice](../../NOTICE.md).

## Further practice

The existing notebooks under `exercises/lecture04-pandas-*` remain available. Some contain material beyond this shorter introduction, such as raw-data cleaning; they are not prerequisites for the core lesson. In particular, `lecture04-pandas-munging-ii.ipynb` uses the downloaded raw data and still requires the repository's data-preparation step.

Official pandas documentation linked in the main notebook covers loading, summaries, selection, and sorting. The broader [hotel case studies](https://gabors-data-analysis.com/casestudies/) provide context for later data preparation and analysis.
