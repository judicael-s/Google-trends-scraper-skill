---
name: google-trends-scraper
description: Use the free standalone Playwright Google Trends scraper for slow SEO ideation, seasonality checks, region insights, related-query discovery, and cron-based query monitoring from Hermes, Open Claw Agent, Claude Code, Codex, or similar agent runners.
version: 0.2.0
author: Organic Agent / Judicael S
license: MIT
metadata:
  hermes:
    tags: [seo, google-trends, playwright, cron, keyword-research, windows, wsl]
---

# Google Trends Scraper Skill

## When to use

Use this skill when the user wants to:

- operate a **free** Google Trends scraper that leverages Playwright instead of a paid Trends scraper
- inspect seasonality for SEO/content ideas
- craft Trends-ready keyword candidates from article titles, sentences, campaign ideas, or rough concepts before scraping
- compare query demand timing across markets or regions
- run a slow radar cron over seed keywords
- turn raw Trends graph output into clear index numbers and result summaries
- troubleshoot Google Trends 429 / headless browser blocking
- use the standalone repo `judicael-s/Google-trends-scraper`
- equip Hermes, Open Claw Agent, Claude Code, Codex, or another agent runner with clear scraper workflows and cron procedures

Do **not** use Trends as search volume truth. In short: Trends is not search volume. It is an indexed signal for ideation, timing, and relative interest. Validate important opportunities later with GSC, DataForSEO, Google Ads, SERP evidence, or analytics.

## Query crafting from titles or sentences

When the user provides a full title, sentence, page title, or rough idea, do **not** search it literally by default. First use `references/query-crafting-workflow.md` and `templates/title-to-trends-query-candidates.md` to extract intent and generate short, natural Google Trends query candidates.

Recommended candidate buckets:

- broad anchor
- problem query
- action query
- audience/level query
- commercial query
- alternative wording
- time-sensitive query
- local/regional query

Then test only the strongest 1–3 candidates or add them to the slow rotating cron config.

For recurring radars, load `references/durable-radar-workflow.md`. Prefer 2–4-word human queries, preserve topic/source/intent provenance, exclude already-searched exact queries from state/JSONL, and rotate across website-specific topic buckets. Use `templates/google-trends-topic-buckets.json` as a generic shape—not as a fixed taxonomy.

## Clear result summaries

After each scrape, use `references/result-interpretation-workflow.md` and `templates/trends-result-summary.md` to present clear graph numbers before recommendations.

Always show, when available:

- status: `usable`, `weak_signal`, `unclear`, `rate_limited`, or `blocked_or_failed`
- data type: Google Trends index values, **not** absolute search volume
- timeline points
- non-zero periods and zero/low-display periods
- peak value and peak period
- latest value
- average value
- recent 4-period average when available
- trend delta
- region count and top regions
- related query count and top related queries

Explain that `100` is the peak inside the selected query/geo/timeframe and `0` means too low to display, not guaranteed zero searches.

## Source repo

Standalone scraper repo:

```text
https://github.com/judicael-s/Google-trends-scraper
```

Core files:

```text
trends_runner.js              # Windows-side Playwright collector
run-trends.ps1                # PowerShell wrapper for one scrape
open-trends-profile.ps1       # manual login/warmup helper
rotating_trends_cron.py       # one-query-per-tick cron wrapper
build_trends_radar_config.py  # evidence + topic buckets -> reusable client config
examples/client-trends-radar.config.json
```

## Preferred architecture

```text
Hermes / WSL / cron
  -> rotating_trends_cron.py
  -> powershell.exe run-trends.ps1
  -> Windows Playwright persistent Chrome/Edge profile
  -> Google Trends normalized JSON
  -> raw archive + durable Markdown/JSONL/optional Obsidian log
  -> alert-only concise cron summary
```

Reason: Google Trends often returns 429 to clean WSL/headless/fresh automation sessions. A persistent visible Windows browser profile is closer to the user’s normal browser and can be logged in/warmed once.

## Setup workflow

1. Clone and install:

```bash
git clone https://github.com/judicael-s/Google-trends-scraper.git
cd Google-trends-scraper
npm install
```

2. Validate offline:

```bash
node trends_runner.js --fixture fixtures/google_trends_sample.json >/tmp/trends.json
python -m json.tool /tmp/trends.json >/dev/null
python -m pytest tests -q
```

3. Warm the browser profile if live automation gets 429:

```bash
powershell.exe -NoProfile -ExecutionPolicy Bypass \
  -File "$(wslpath -w ./open-trends-profile.ps1)" \
  -Query "cahier de vacances maths" \
  -Geo FR \
  -Hl fr-FR \
  -Timeframe "today 12-m"
```

In the opened Windows Chrome window: log in if requested, load Trends manually once, then close the window.

4. Run a live scrape:

```bash
powershell.exe -NoProfile -ExecutionPolicy Bypass \
  -File "$(wslpath -w ./run-trends.ps1)" \
  -Query "cahier de vacances maths" \
  -Geo FR \
  -Hl fr-FR \
  -Timeframe "today 12-m" \
  -RegionResolution REGION
```

## Cron workflow

Use one query per tick. Recommended starting cadence: every 8 hours.

1. Create a client config from `templates/client-trends-radar.config.json` or the repo example.
2. Create a script like `client_google_trends_radar.sh`:

```bash
#!/usr/bin/env bash
set -euo pipefail
cd /path/to/Google-trends-scraper
python rotating_trends_cron.py \
  --config /path/to/client-trends-radar.config.json \
  --state /path/to/client-trends-radar-state.json \
  --output-dir /path/to/google-trends-raw
```

3. In Hermes, schedule it as a no-agent cron:

```text
schedule: every 8h
script: client_google_trends_radar.sh
no_agent: true
```

The runner logs every due check before deciding whether to print. With `alert_policy.mode: opportunities_only`, ordinary checks produce empty stdout while durable Markdown/JSONL/optional Obsidian history still grows.

Storage must adapt to the user's setup. Local Markdown plus JSONL is the portable default. Add `obsidian_markdown` only when a vault exists (via `vault_path` or `OBSIDIAN_VAULT_PATH`). Multiple destinations may be enabled together.

## Query selection rules

- Start with broad anchors before long article titles.
- When input is an article title, page title, sentence, or rough idea, craft short Trends-ready query candidates before scraping; do not search the full title literally by default.
- Use cluster terms as spokes after a broad anchor validates seasonal interest.
- Rotate seed terms slowly.
- Rotate across topical buckets rather than exhausting one cluster.
- Do not repeat identical query/geo/timeframe combinations too often.
- Use market-specific `geo` and `hl` values.
- Keep per-client browser profiles separate.

## Output interpretation

For any non-empty scraper result, first provide a clear result summary using `templates/trends-result-summary.md`.

| Signal | Meaning |
|---|---|
| `interest_over_time` | normalized 0–100 time series |
| `interest_by_region` | relative regional interest |
| `related_queries` | top/rising query ideas |
| `summary.latest_value` | most recent indexed value |
| `summary.trend_delta` | latest minus first point |
| `NO_TIMELINE_DATA` | possible low volume, UI change, or partial capture |
| `GOOGLE_TRENDS_RATE_LIMITED` | cooldown/warm profile; not zero demand |

## Troubleshooting

### 429 / Too Many Requests

- Stop testing repeatedly.
- Wait 30–60 minutes.
- Use `open-trends-profile.ps1` and log in/warm the profile manually.
- Reduce cadence.
- Prefer broad anchor queries.

### Browser profile in use

Close Chrome/Edge windows using the same `UserDataDir`, then retry.

### WSL cannot display a visible browser

That is expected. The runner launches Windows Chrome via PowerShell instead.

## Safety guardrails

- Do not commit cookies, browser profiles, credentials, API keys, or raw private client data.
- Do not copy a logged-in browser profile between clients or machines.
- Treat all Trends data as ideation only.
- Validate SEO actions before execution.
- Keep scraping slow and human-scale.

## Linked files

- `templates/client-trends-radar.config.json` — starting config
- `templates/google-trends-topic-buckets.json` — generic multi-topic query strategy starter
- `templates/hermes-cron-script.sh` — cron script template
- `references/durable-radar-workflow.md` — logging, storage, seasonality, alerting, and validation contract
- `references/workflows.md` — detailed workflows and examples
- `references/troubleshooting.md` — common failures and fixes
