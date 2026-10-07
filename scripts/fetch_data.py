"""Download external datasets used by the course notebooks."""

from __future__ import annotations

import argparse
import sys
import urllib.error
import urllib.request
from dataclasses import dataclass
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data" / "raw"


@dataclass(frozen=True)
class Dataset:
    filename: str
    url: str
    description: str


DATASETS = (
    Dataset("hotel_vienna_raw.csv", "https://osf.io/yzntm/download", "Hotels Europe raw data (legacy local filename)"),
    Dataset("hotels_europe_price.csv", "https://osf.io/p6tyr/download", "Hotels Europe prices"),
    Dataset("hotels_europe_features.csv", "https://osf.io/utwjs/download", "Hotels Europe features"),
    Dataset("sp500.csv", "https://osf.io/4pgrf/download", "S&P 500 data"),
    Dataset("billion_prices.csv", "https://osf.io/yhbr5/download", "Billion Prices data"),
    Dataset("hotels_vienna.csv", "https://osf.io/y6jvb/download", "Hotels Vienna regression data"),
)


def download(dataset: Dataset, force: bool) -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    target = DATA_DIR / dataset.filename
    if target.exists() and target.stat().st_size > 0 and not force:
        print(f"exists: {target.relative_to(ROOT)}")
        return

    temp = target.with_suffix(target.suffix + ".tmp")
    print(f"download: {dataset.description} -> {target.relative_to(ROOT)}")
    request = urllib.request.Request(dataset.url, headers={"User-Agent": "coding-1-course/2026"})
    try:
        with urllib.request.urlopen(request, timeout=60) as response, temp.open("wb") as output:
            while True:
                chunk = response.read(1024 * 1024)
                if not chunk:
                    break
                output.write(chunk)
    except (urllib.error.URLError, TimeoutError) as exc:
        if temp.exists():
            temp.unlink()
        raise RuntimeError(f"failed to download {dataset.url}: {exc}") from exc

    if temp.stat().st_size == 0:
        temp.unlink()
        raise RuntimeError(f"downloaded empty file for {dataset.url}")
    temp.replace(target)


def prepare_pandas_quotes() -> None:
    """Supply a small joined table; students calculate nightly prices in class."""
    prices = pd.read_csv(DATA_DIR / "hotels_europe_price.csv")
    features = pd.read_csv(DATA_DIR / "hotels_europe_features.csv")

    # A single source period has both one- and four-night quotes. Exact check-in
    # dates are not supplied, so this is not an identical-date price comparison.
    period = prices.loc[
        (prices["year"] == 2017)
        & (prices["month"] == 12)
        & (prices["holiday"] == 1)
        & (prices["weekend"] == 0)
    ]
    joined = period.merge(
        features, on="hotel_id", how="left", validate="many_to_one", indicator=True
    )
    if not joined["_merge"].eq("both").all():
        raise ValueError("Some hotel quotes have no matching hotel characteristics")

    quotes = joined.loc[
        (joined["city"] == "Vienna") & (joined["accommodation_type"] == "Hotel")
    ].copy()
    quotes = quotes.rename(
        columns={"rating": "ratings", "rating_reviewcount": "rating_count"}
    )
    columns = [
        "hotel_id", "city", "year", "month", "weekend", "holiday", "nnights",
        "neighbourhood", "stars", "price", "ratings", "rating_count", "distance",
        "ratingta",
    ]
    quotes = quotes[columns].sort_values(["hotel_id", "nnights"])
    if quotes.empty or quotes["nnights"].isna().any() or not quotes["nnights"].gt(0).all():
        raise ValueError("Teaching quotes must have observed, positive stay lengths")
    if quotes.duplicated(["hotel_id", "nnights"]).any():
        raise ValueError("Expected one quote per hotel and stay length in this period")

    # Do not precompute price_per_night or remove missing ratings/star categories.
    target = ROOT / "lectures" / "lecture04-pandas-basics" / "hotel_vienna_quotes.csv"
    target.parent.mkdir(parents=True, exist_ok=True)
    quotes.to_csv(target, index=False, lineterminator="\n")
    print(f"prepared: {target.relative_to(ROOT)} ({len(quotes)} quotes)")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--force", action="store_true", help="re-download files that already exist")
    args = parser.parse_args()

    try:
        for dataset in DATASETS:
            download(dataset, force=args.force)
        prepare_pandas_quotes()
    except (RuntimeError, ValueError) as exc:
        print(exc, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
