# Data

The repository keeps small local teaching files with the relevant lecture folders. Larger or external datasets are downloaded into `data/raw/` by:

```bash
uv run python scripts/fetch_data.py
```

Downloaded source files in `data/raw/` are ignored by Git so the repository stays lightweight. The script also prepares the small lecture04 CSV described below. The lecture04 introduction reads that prepared CSV directly from GitHub; students do not need to run this script for that lesson.

| Local file | Source | Used by |
| --- | --- | --- |
| `data/raw/hotel_vienna_raw.csv` | <https://osf.io/yzntm/download> | lecture04 additional raw-data cleaning practice (`exercises/lecture04-pandas-munging-ii.ipynb`) |
| `data/raw/hotels_europe_price.csv` | <https://osf.io/p6tyr/download> | lecture04 quote-sample preparation; lecture05 plotnine |
| `data/raw/hotels_europe_features.csv` | <https://osf.io/utwjs/download> | lecture04 quote-sample preparation; lecture05 plotnine |
| `data/raw/sp500.csv` | <https://osf.io/4pgrf/download> | lecture05 matplotlib and function practice |
| `data/raw/billion_prices.csv` | <https://osf.io/yhbr5/download> | lecture07 data exploration |
| `data/raw/hotels_vienna.csv` | <https://osf.io/y6jvb/download> | lecture10 regression |

## Prepared GitHub-hosted sample for the pandas introduction

[`lectures/lecture04-pandas-basics/hotel_vienna_quotes.csv`](../lectures/lecture04-pandas-basics/hotel_vienna_quotes.csv) is the prepared CSV for the question-led DataFrame introduction, versioned and published together with the notebook on `main`. The notebook uses `pd.read_csv` with the [direct GitHub CSV URL](https://raw.githubusercontent.com/ulrichwohak/Coding-1-Introduction-to-Python/main/lectures/lecture04-pandas-basics/hotel_vienna_quotes.csv). Students need an internet connection, but no local combined CSV, manual data download, or repository update to obtain the data.

Merging and sample preparation happen in `scripts/fetch_data.py`, not in the lecture notebook. The detailed counts below document the prepared data for maintainers; the notebook asks students to discover these features by running code.

### Sources and reproducible preparation

For instructors maintaining the prepared CSV, run the standard data-preparation command from the repository root. This is not a student prerequisite for the GitHub-first lesson:

```bash
uv run python scripts/fetch_data.py
```

The script uses the existing OSF [price file](https://osf.io/p6tyr/download) and [feature file](https://osf.io/utwjs/download), downloaded to `data/raw/`. It joins prices to features on `hotel_id`, validating a many-to-one relationship: a hotel can have multiple price quotes but only one feature row. It retains records matching all of these source conditions:

- `city == "Vienna"` (the search area, not necessarily the actual municipality).
- `accommodation_type == "Hotel"`.
- `year == 2017` and `month == 12`.
- `holiday == 1` and `weekend == 0`.

The preparation retains all star categories and missing ratings within that sample. It renames `rating` to `ratings` and `rating_reviewcount` to `rating_count`, and writes these 14 columns:

`hotel_id`, `city`, `year`, `month`, `weekend`, `holiday`, `nnights`, `neighbourhood`, `stars`, `price`, `ratings`, `rating_count`, `distance`, `ratingta`.

`price` is the total quoted stay price in EUR, and `nnights` is the source's number of nights. The prepared CSV deliberately does **not** include `price_per_night`: students create it by dividing these columns. The stay lengths are genuine source values, not simulated or assigned for the exercise.

### Sample checks and interpretation

The prepared file contains 437 quotes for 250 distinct hotels: 239 one-night quotes and 198 four-night quotes. There is at most one row per `hotel_id` and `nnights` combination in this sample. Two quotes lack the primary guest rating, and ten lack the alternative Tripadvisor rating. No quotes are removed merely for having missing ratings.

Rows are quotes, not unique hotels. Some hotels therefore contribute more than once to descriptive statistics. In the optional star-category summary, each quote has equal weight, so a hotel with two quotes contributes twice. This is not a hotel-weighted summary.

The source identifies December 2017 holiday weekday stays but does not supply exact check-in dates. Converting a total quote into a nightly price makes the units comparable; it does not establish identical travel dates or otherwise equivalent stays. Nearby municipalities are included in the Vienna search area. This is a selected historical teaching sample, not a representative or current sample of hotels.

The notebook's default GitHub URL serves this prepared CSV, not an unprepared OSF source file. Updates to the prepared CSV and any notebook changes that depend on them should be committed and published together.

## Existing sample retained for exercises

[`lectures/lecture04-pandas-basics/hotel_vienna_restricted.csv`](../lectures/lecture04-pandas-basics/hotel_vienna_restricted.csv) remains unchanged for the existing lecture04 exercises that use it. It is not downloaded or regenerated by `fetch_data.py`.

The file contains 217 distinct hotels and 29 columns: one-night weekday quotes for the Vienna search area in November 2017, restricted to hotel star categories from 3 to 4 (including 3.5). Nearby municipalities are included. It is a prepared subset, not a representative or current sample of hotels. The primary guest ratings are complete; three alternative Tripadvisor ratings and their review counts are missing.

Original variable definitions and educational-use terms are in the [Hotels Europe dataset description](https://gabors-data-analysis.com/datasets/hotels-europe/); adapted-material attribution is in [NOTICE.md](../NOTICE.md).
