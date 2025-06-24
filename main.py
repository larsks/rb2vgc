import argparse
import sys

from pydantic import BaseModel

import models
import repeaterbook


class Options(BaseModel):
    query: list[str]
    output: str | None


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--output", "-o")
    p.add_argument("query", nargs="+")
    return Options.model_validate(vars(p.parse_args()))


def main():
    args = parse_args()
    rb = repeaterbook.RepeaterBook()
    terms = repeaterbook.QueryTerms.model_validate(
        dict(item.split("=") for item in args.query)
    )
    repeaters = rb.query(terms)

    with open(args.output, "w") if args.output else sys.stdout as fd:
        fd.write(repeaters.model_dump_json(indent=2))


if __name__ == "__main__":
    main()
