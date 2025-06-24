# pyright: reportUnusedCallResult=false

import argparse
import csv
import json
import sys

from pydantic import BaseModel
from enum import StrEnum

import models
import repeaterbook


class FrequencyBand(StrEnum):
    BAND_10M = "10m"
    BAND_6M = "6m"
    BAND_2M = "2m"
    BAND_70CM = "70cm"


class OutputFormat(StrEnum):
    JSON = "json"
    CSV = "csv"


FrequencyBandLimits: dict[FrequencyBand, tuple[float, float]] = {
    FrequencyBand.BAND_10M: (28, 29.7),
    FrequencyBand.BAND_6M: (50, 54),
    FrequencyBand.BAND_2M: (144, 148),
    FrequencyBand.BAND_70CM: (420, 450),
}


class Options(BaseModel):
    query: list[str]
    band: list[FrequencyBand]
    format: OutputFormat
    output: str | None


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--format", "-f", choices=OutputFormat, default=OutputFormat.JSON)
    p.add_argument("--output", "-o")
    p.add_argument(
        "-b", "--band", choices=FrequencyBandLimits, action="append", default=[]
    )
    p.add_argument("query", nargs="+")
    return Options.model_validate(vars(p.parse_args()))


def filter_band(repeaters: list[models.Repeater], bands: list[FrequencyBand]):
    bandlimits = tuple(FrequencyBandLimits[band] for band in bands)
    return [
        repeater.model_dump()
        for repeater in repeaters
        if not bandlimits
        or any(limit[0] <= repeater.tx_freq <= limit[1] for limit in bandlimits)
    ]


def main():
    args = parse_args()
    rb = repeaterbook.RepeaterBook()
    terms = repeaterbook.QueryTerms.model_validate(
        dict(item.split("=") for item in args.query)
    )
    repeaters = rb.query(terms)
    filtered_repeaters = filter_band(repeaters.results, bands=args.band)

    with open(args.output, "w") if args.output else sys.stdout as fd:
        if args.format == OutputFormat.JSON:
            json.dump(filtered_repeaters, fd, indent=2)
        elif args.format == OutputFormat.CSV:
            writer = csv.DictWriter(fd, models.Repeater.model_fields)
            writer.writeheader()
            writer.writerows(filtered_repeaters)
        else:
            raise ValueError("unknown output format")


if __name__ == "__main__":
    main()
