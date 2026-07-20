# Google Trends Scraper Skill

A skill/workflow pack for operating the standalone [Google Trends Playwright Scraper](https://github.com/judicael-s/Google-trends-scraper): a **free**, Playwright-powered Google Trends scraper.

It can be used by **Hermes**, **Open Claw Agent**, **Claude Code**, **Codex**, or any agent/workflow runner that can follow markdown procedures and execute shell/PowerShell commands.

This skill gives agents and users clear workflows for practical use cases such as:

- testing and comparing SEO/content ideas
- transforming article titles, sentences, and rough ideas into Trends-ready keyword candidates before scraping
- estimating market interest directionally with Google Trends index data
- discovering rising trends and related queries
- finding promising keywords worldwide or regionally
- comparing which countries or regions search for which keywords
- inspecting short-term and long-term demand windows: daily, weekly/hebdo, monthly, yearly, or multi-year
- timing seasonal campaigns and content refreshes
- running cron-based keyword radars
- generating short human-style query sets across website-specific topic buckets
- logging every check to portable Markdown/JSONL and optional Obsidian/GBrain inputs
- classifying active weeks, peak weeks/months, and seasonality

It also covers operational workflows for:

- installing the scraper
- warming a persistent Windows Chrome/Edge profile
- collecting one Google Trends query
- summarizing clear Trends index numbers from the graph
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
references/query-crafting-workflow.md
references/result-interpretation-workflow.md
references/durable-radar-workflow.md
references/troubleshooting.md
templates/title-to-trends-query-candidates.md
templates/trends-result-summary.md
templates/client-trends-radar.config.json
templates/google-trends-topic-buckets.json
templates/hermes-cron-script.sh
```

## Recommended usage pattern

```text
1. Clone standalone scraper.
2. Craft Trends-ready query candidates if the input is a title/sentence, not a literal query.
3. Run fixture tests.
4. Warm/login a dedicated Windows browser profile if needed.
5. Run one live scrape.
6. Summarize clear Trends index numbers and plain-language interpretation.
7. Generate a 2–4-word query set across website-specific topic buckets and exclude prior exact checks.
8. Configure portable Markdown + JSONL storage; add Obsidian only if available.
9. Schedule one-query-per-tick cron every ~8h with cross-topic rotation.
10. Save every check and raw JSON, but alert only on errors/opportunities.
11. Validate promising ideas with SEO data before action.
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
