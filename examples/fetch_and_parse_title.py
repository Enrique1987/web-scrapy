"""Fetch a public HTML page and print its title.

Usage:
    python examples/fetch_and_parse_title.py https://example.com
"""

from __future__ import annotations

import argparse

import requests
from bs4 import BeautifulSoup


def fetch_html(url: str) -> str:
    """Return the HTML at *url* with a bounded request."""
    response = requests.get(
        url,
        headers={"User-Agent": "learning-web-scraping-example/1.0"},
        timeout=15,
    )
    response.raise_for_status()
    return response.text


def extract_title(html: str) -> str:
    """Extract a document title, returning a useful fallback when absent."""
    soup = BeautifulSoup(html, "html.parser")
    return soup.title.get_text(strip=True) if soup.title else "No title found"


def main() -> None:
    parser = argparse.ArgumentParser(description="Fetch a page and print its title.")
    parser.add_argument("url", help="Public URL to fetch, for example https://example.com")
    args = parser.parse_args()

    print(extract_title(fetch_html(args.url)))


if __name__ == "__main__":
    main()
