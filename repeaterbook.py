# pyright: reportUnusedCallResult=false

import os
import requests

import urllib.parse as urlparse

from pydantic import BaseModel
from pydantic import model_validator
from pathlib import Path
from diskcache import Cache
from typing import TypeVar
from typing import cast

from models import RepeaterBookResults
from constants import RepeaterMode
from constants import StateCodes

xdg_cache_home = Path(os.environ.get("XDG_CACHE_HOME", os.path.expanduser("~/.cache")))
cache = Cache(str(xdg_cache_home / "repeaterbook"))

T = TypeVar("T")
multivalue = T | list[T] | None


class QueryTerms(BaseModel):
    country: multivalue[str] = None
    county: multivalue[str] = None
    city: multivalue[str] = None
    callsign: multivalue[str] = None
    state_id: multivalue[StateCodes] = None
    frequency: multivalue[float] = None
    mode: multivalue[RepeaterMode] = None

    @model_validator(mode="before")
    @classmethod
    def validate_model(cls, data):
        if "state" in data:
            try:
                data["state_id"] = StateCodes[data["state"]]
            except KeyError:
                raise ValueError("unknown state abbreviation")

        return data

    def make_query_term(self, k: str, v) -> str:
        return f"{k}={v}"

    def to_query(self) -> str:
        terms: list[str] = []
        for k, v in self.model_dump().items():
            if v is None:
                continue

            if isinstance(v, list):
                for x in v:
                    terms.append(self.make_query_term(k, x))
            else:
                terms.append(self.make_query_term(k, v))

        return "&".join(urlparse.quote(term, "/=") for term in terms)


class RepeaterBook(requests.Session):
    baseurl: str = "https://www.repeaterbook.com/api/export.php"
    user_agent: str = "repeaterbook.py; repeaterbook@mailinator.com"
    cache_lifetime: int = 1800

    def __init__(self, user_agent: str | None = None):
        super().__init__()

        if user_agent is not None:
            self.user_agent = user_agent

        self.headers["user-agent"] = self.user_agent

    def query(self, terms: QueryTerms) -> RepeaterBookResults:
        content: bytes = cast(bytes, cache.get(terms))

        if not content:
            query = terms.to_query()
            url = f"{self.baseurl}?{query}"
            res = self.get(url)
            res.raise_for_status()
            content = res.content
            cache.set(terms, content, expire=self.cache_lifetime)

        return RepeaterBookResults.model_validate_json(content)
