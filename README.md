# Google Trends Scraper Skill

A Hermes skill for operating the standalone [Google Trends Playwright Scraper](https://github.com/judicael-s/Google-trends-scraper).

This skill gives agents and users clear workflows for:

- installing the scraper
- warming a persistent Windows Chrome/Edge profile
- collecting one Google Trends query
- running a slow rotating cron radar
- interpreting errors like 429 and no-data cases
- using Trends as SEO ideation, not search-volume truth

## Repositories

| Repo | Purpose |
|---|---|
| [`Google-trends-scraper`](https://github.com/judicael-s/Google-trends-scraper) | Standalone scraper code |
| [`Google-trends-scraper-skill`](https://github.com/judicael-s/Google-trends-scraper-skill) | Hermes skill/workflows for using the scraper |

## Install as a Hermes skill

Copy or symlink this repo into a Hermes profile's skills directory, for example:

```bash
mkdir -p ~/.hermes/profiles/organicagent/skills/seo
cd ~/.hermes/profiles/organicagent/skills/seo
git clone https://github.com/judicael-s/Google-trends-scraper-skill.git google-trends-scraper
```

Then the skill can be loaded by name:

```text
google-trends-scraper
```

## What the skill teaches

The skill is intentionally practical. It includes:

```text
SKILL.md
references/workflows.md
references/troubleshooting.md
templates/client-trends-radar.config.json
templates/hermes-cron-script.sh
```

## Recommended usage pattern

```text
1. Clone standalone scraper.
2. Run fixture tests.
3. Warm/login a dedicated Windows browser profile if needed.
4. Run one live scrape.
5. Configure a client seed list.
6. Schedule one-query-per-tick cron every ~8h.
7. Save raw JSON and report concise summaries.
8. Validate promising ideas with SEO data before action.
```

## Strong guardrails

- Google Trends is not search volume.
- Rate-limit errors are not zero demand.
- Keep scraping slow.
- Keep browser profiles local/private.
- Do not copy cookies or profiles between clients.
- Validate SEO decisions with GSC, DataForSEO, Ads, SERP, or analytics.

## License

MIT
