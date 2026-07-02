# Workflows

## 1. Offline validation workflow

Use before any live Google request.

```bash
cd /path/to/Google-trends-scraper
npm install
node trends_runner.js --fixture fixtures/google_trends_sample.json >/tmp/trends.json
python -m json.tool /tmp/trends.json >/dev/null
python -m pytest tests -q
```

Pass criteria:

- JSON parses.
- `rows` exists.
- A row has `interest_over_time`, `interest_by_region`, `related_queries`, and `validation_status`.

## 2. Browser warmup workflow

Use when manual Chrome works but automation gets 429.

```bash
powershell.exe -NoProfile -ExecutionPolicy Bypass \
  -File "$(wslpath -w ./open-trends-profile.ps1)" \
  -Query "cahier de vacances maths" \
  -Geo FR \
  -Hl fr-FR \
  -Timeframe "today 12-m"
```

In the opened browser:

1. Log in if Google asks.
2. Load Google Trends manually.
3. Check the query once.
4. Close the browser.

Then retry the automated run.

## 3. One live query workflow

```bash
powershell.exe -NoProfile -ExecutionPolicy Bypass \
  -File "$(wslpath -w ./run-trends.ps1)" \
  -Query "cahier de vacances maths" \
  -Geo FR \
  -Hl fr-FR \
  -Timeframe "today 12-m" \
  -RegionResolution REGION
```

Use one broad anchor first. Avoid testing many long-tail queries repeatedly.

## 4. Client cron workflow

Create a config:

```bash
cp examples/client-trends-radar.config.json /client/google-trends-radar.config.json
```

Edit:

- `client_id`
- `site_url`
- `geo`
- `hl`
- `timeframe`
- `queries`
- `min_hours_between_same_query`

Create script:

```bash
#!/usr/bin/env bash
set -euo pipefail
cd /path/to/Google-trends-scraper
python rotating_trends_cron.py \
  --config /client/google-trends-radar.config.json \
  --state /client/google-trends-radar-state.json \
  --output-dir /client/google-trends-raw
```

Schedule every 8h as a no-agent script cron.

## 5. Interpreting cron summaries

Example success:

```text
Google Trends radar: client
Query: cahier de vacances maths
Status: ok
Timeline points: 53
Latest/mean/max/delta: 97 / 10.98 / 100 / -3
Regions: 22
Related queries: 6
Validation: trends_ideation_only
```

Example low/no-data warning:

```text
Warnings: NO_TIMELINE_DATA
Timeline points: 0
Regions: 22
```

Do not immediately reject the keyword. Compare with a broader anchor and validate elsewhere.

## 6. SEO decision workflow

1. Use Trends to discover timing, seasonality, and regional/related-query signals.
2. Generate content hypotheses.
3. Validate with GSC/DataForSEO/Google Ads/SERP.
4. Score opportunity by business fit, feasibility, and conversion value.
5. Only then create briefs, update pages, or publish content.
