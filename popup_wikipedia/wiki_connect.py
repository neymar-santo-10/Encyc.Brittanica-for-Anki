# -*- coding: utf-8 -*-

import json
from os import PathLike
from pathlib import Path

# We still load config because other parts of the addon import WikiConnect
from .config import config


class WikiConnect(object):
    """
    Replaces Wikipedia API calls with simple Britannica page loading.
    We no longer fetch JSON or mobile HTML.
    We just return a URL for the popup to load in a WebView.
    """

    def __init__(self, cache_expiry_hrs: int):
        pass  # no need for caching

    def get_britannica_url(self, term: str) -> str:
        """
        Returns the Britannica search page for a term.
        Britannica does not provide a free REST API.
        """
        safe = term.strip().replace(" ", "%20")
        return f"https://www.britannica.com/search?query={safe}"

    # Legacy API functions replaced with Britannica redirect
    def get_summary(self, title: str):
        return {"url": self.get_britannica_url(title)}

    def get_mobile_html(self, title: str) -> str:
        # Instead of returning HTML, return a URL string
        return self.get_britannica_url(title)

    def get_extract(self, title: str) -> str:
        # Same: return URL instead of HTML
        return self.get_britannica_url(title)

    def summary_parser(self, summary_resp: {}):
        return summary_resp

    @staticmethod
    def _parse_title(title: str) -> str:
        return title.strip().replace(" ", "_")

    @staticmethod
    def _write_htmlfile(html, pth: PathLike) -> int:
        return Path(pth).write_text(html, encoding="utf-8")
