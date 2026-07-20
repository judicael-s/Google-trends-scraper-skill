# Durable Google Trends Radar Workflow

Use this when turning a one-off Google Trends check into a reusable slow radar for any website, market, language, or query family.

## Product rules

1. **Write human-style queries.** Prefer 2–4 words in the target market's natural language. Do not send article titles or copy a client-specific vocabulary into a reusable template. A one-word broad anchor or a justified 5–6-word phrase is allowed when the market requires it.
2. **Mix topical buckets.** Derive buckets from the site's business model and customer journey. Start with reusable dimensions such as core offers, audience needs, problems/outcomes, commercial comparisons, seasonal/events, and adjacent opportunities. Rename or replace them for the client.
3. **Use evidence.** Bootstrap from public audit/site copy, onboarding, titles, and competitors; enrich with GSC after access is available. Preserve `source`, `intent`, `topic`, and `selection_score`.
4. **Avoid duplicate checks.** Read state and cumulative JSONL history before generating a new set. Use normalized exact query + geo + timeframe as the runtime identity.
5. **One query per tick.** Rotate across topic buckets and respect a cooldown. Do not exhaust one cluster first.
6. **Log every check.** No-data, weak, normal, error, and alert-worthy runs all belong in durable history. Alerting and logging are separate decisions.
7. **Keep raw evidence.** Store the raw JSON path in every log record.
8. **Alert selectively.** `opportunities_only` should leave stdout empty for ordinary checks while still writing durable records. Errors may remain alertable.

## Adaptable storage

Do not require Obsidian. Configure one or more destinations:

- `markdown` for a local, shared, Git-based, or synced note;
- `jsonl` for machine-readable cumulative state and later analysis;
- `obsidian_markdown` when the user has an Obsidian vault;
- optional downstream ingestion into GBrain or another knowledge layer from the Markdown/JSONL files.

For Obsidian, use either a destination `vault_path` or `OBSIDIAN_VAULT_PATH`. If Obsidian is unavailable, local Markdown and JSONL remain the default safe storage.

## Required result fields

Each record should contain:

- time UTC;
- query, topic, intent, source, selection score;
- status and error codes;
- geo, language, timeframe;
- timeline points;
- latest, mean, max, and delta;
- active weeks/share;
- peak weeks and peak months;
- seasonality class and plain-language interpretation;
- region and related-query counts;
- raw JSON path;
- `validation_status: trends_ideation_only`.

## Seasonality classes

- `no timeline data`: no weekly points captured; do not call this zero demand.
- `no visible Trends demand`: timeline exists but all normalized values are zero.
- `sparse / low Trends signal`: few active weeks and no strong peak.
- `seasonal peak`: demand concentrates in a short window.
- `sparse multi-peak`: few active weeks with separated strong peaks.
- `recurring / broad-season`: demand is active across a meaningful part of the period.
- `evergreen / all-year`: many active weeks with repeated strong values.

These labels are heuristics, not search volume or business truth.

## Validation ladder

Before turning a Trends signal into an SEO action, validate with the least expensive relevant evidence:

1. GSC query/page evidence;
2. SERP intent and ranking landscape;
3. GA4 or BigQuery journey/conversion relevance;
4. DataForSEO or Google Ads only when paid validation is justified.

Google Trends is an ideation, timing, and prioritisation signal—not absolute demand.
