# Lecture 04: Exploring DataFrames with pandas

## Start with a question

Can we find a hotel quote below EUR 100 per night with a guest rating of at least 4 out of 5? We use this question to learn how to explore a table, check the information available, and build a shortlist using pandas. First, we need to work out a nightly price from each quote's total price and length of stay.

Start with [`02_pandas_data_munging.ipynb`](02_pandas_data_munging.ipynb). Despite its retained filename, it is a self-contained introduction to DataFrames: it loads the prepared CSV directly from GitHub and does not require completing part one or generating any data first.

[`01_pandas_basics.ipynb`](01_pandas_basics.ipynb) remains available as an optional reference for constructing Series and DataFrames and working with indexes. It is not a prerequisite for the question-led lesson.

## Questions and operations

| Question | pandas operations |
| --- | --- |
| What quotes and information do we actually have? | `read_csv`, column selection, `head`, `shape`, `info`, `value_counts` |
| How can we compare quoted prices for different lengths of stay? | Column arithmetic and assignment to create `price_per_night` |
| What does a typical night cost, and how much do nightly prices vary? | `describe` on selected measurements |
| Does every quote have a rating from both sources? | `isna` and counts of missing values |
| Which quotes meet our nightly budget and guest-rating requirements? | Boolean conditions and `.loc` |
| Which qualifying quotes are cheapest per night? | `sort_values` and `head` |

Each section introduces a concrete question, shows a short code example with explanatory comments, and asks students to read the answer from its output. Dataset sizes, star categories, stay lengths, missing values, and summary results are discoveries to make with code, not answers supplied in advance. The focus is on reading and using a DataFrame, not memorising methods or calculating statistics.

The core lesson ends with a variation: a visitor has a different nightly budget and wants the closest qualifying quotes rather than the cheapest. The three optional extensions cover converting distances into a new column, comparing median nightly prices by star category, and saving a shortlist as a new CSV. The grouped summary is per quote: hotels with more quotes contribute more observations. Stop before these extensions if time is short.

## Learning outcomes

After the core lesson, students should be able to:

- Explain what a DataFrame's rows, columns, and index represent.
- Distinguish a hotel identifier from a quote: the same hotel can appear in more than one row.
- Load a CSV directly from a URL and distinguish the source file from the table in memory.
- Inspect dimensions, column types, categories, and numerical summaries.
- Create `price_per_night` by dividing total `price` by `nnights`, and use it for price comparisons.
- Distinguish a missing rating from a rating of zero.
- Select columns and filter rows with one or two conditions.
- Sort a filtered result and explain the limits of the resulting shortlist.
- Find the relevant method in the linked pandas documentation.

## Data and setup

Use the course Python environment and run the notebook from top to bottom with an internet connection. The loading cell reads the [prepared CSV directly from GitHub](https://raw.githubusercontent.com/ulrichwohak/Coding-1-Introduction-to-Python/main/lectures/lecture04-pandas-basics/hotel_vienna_quotes.csv), independently of the notebook's working directory. Students do not need a local copy of the combined CSV, a manual data download, or a repository update just to obtain the data.

[`hotel_vienna_quotes.csv`](hotel_vienna_quotes.csv) is versioned and published together with the notebook on the repository's `main` branch. It contains historical hotel quotes for the Vienna search area, including nearby municipalities, from December 2017. It is not a representative sample of all hotels or a source of current prices. Exact check-in dates are not available, so normalising prices by stay length does not establish that the stays are otherwise identical.

The supplied CSV contains total `price` and `nnights`, but no `price_per_night` column: students construct that column themselves. Each row is a quote, and the same hotel may have multiple quotes. The notebook does not ask students to merge or clean the source files.

For instructors maintaining the prepared CSV, reproduce it from the source files by running this command from the repository root. Students do not need to run it for this lesson:

```bash
uv run python scripts/fetch_data.py
```

Optional export writes a separate file inside a `scratch` folder in the current working directory. That folder is ignored by Git when working inside the course repository.

For data definitions, including prices in EUR, and educational-use terms, see the [Hotels Europe dataset description](https://gabors-data-analysis.com/datasets/hotels-europe/). See also the repository's [data inventory](../../data/README.md) and [attribution notice](../../NOTICE.md).

## Further practice

The existing notebooks under `exercises/lecture04-pandas-*` remain available. The older [`hotel_vienna_restricted.csv`](hotel_vienna_restricted.csv) is retained unchanged for exercises that use it. Some exercises contain material beyond this shorter introduction, such as raw-data cleaning; they are not prerequisites for the core lesson. In particular, `lecture04-pandas-munging-ii.ipynb` uses the downloaded raw data and still requires the repository's data-preparation step.

Official pandas documentation linked in the main notebook covers loading, summaries, selection, and sorting. The broader [hotel case studies](https://gabors-data-analysis.com/casestudies/) provide context for later data preparation and analysis.
