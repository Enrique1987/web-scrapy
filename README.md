# Web Scraping with Python

A personal learning repository for practical web-scraping techniques with Python.

The goal is to keep examples small, readable, and responsible: each notebook or script should explain one technique, use clear names, and avoid collecting more data than necessary.

## Start here

1. Create and activate a virtual environment.
2. Install the dependencies with `python -m pip install -r requirements.txt`.
3. Run the first standalone example:

   ```bash
   python examples/fetch_and_parse_title.py https://example.com
   ```

## Repository map

| Area | Purpose |
| --- | --- |
| `01_Beautiful_Soup/` | HTML parsing and data extraction exercises. |
| `02_Selenium/` | Browser automation and dynamic-page examples. |
| `05_Single_Notes/` | Focused one-topic notebooks, including pandas HTML tables. |
| `examples/` | Short, runnable scripts that demonstrate a single pattern. |
| `docs/` | Working conventions for keeping notebooks and examples readable. |

## Responsible scraping

- Read a site's terms of service and robots policy before collecting data.
- Use rate limits, identify your client when appropriate, and set timeouts.
- Do not bypass authentication, access controls, CAPTCHAs, or rate limits.
- Prefer an official API when one is available.

## Learning path

1. Parse static HTML with `requests` and Beautiful Soup.
2. Extract and clean tabular data with pandas.
3. Work with JSON and XML responses.
4. Use Selenium only when browser rendering is genuinely required.
5. Turn a stable example into a small, documented project.

See [docs/notebook-style.md](docs/notebook-style.md) for the standard used by new material.

