# Title/Sentence to Google Trends Query Crafting Workflow

Use this workflow when the user gives an article title, content idea, sentence, campaign tagline, product description, or rough topic. Do **not** send the full sentence to Google Trends by default. First transform it into short, natural search queries that real people are likely to type.

## Why this matters

Google Trends is sensitive to wording and query volume. Editorial titles often produce no data even when the underlying topic has demand.

Bad direct query:

```text
Sauver l’été préparer la rentrée éviter les lacunes en maths
```

Better query candidates:

```text
cahier de vacances maths
réviser les maths pendant les vacances
lacunes en maths
stage maths vacances
préparer sa rentrée en seconde
remise à niveau maths
```

## Workflow

### 1. Parse the input

Extract:

- **Core topic** — what the idea is about
- **Audience** — who searches: parents, students, buyers, founders, developers, etc.
- **Pain/problem** — what they want to solve
- **Desired outcome** — what success looks like
- **Timing/seasonality** — summer, rentrée, Black Friday, tax season, daily news, etc.
- **Commercial angle** — course, product, service, tool, template, consultant, local provider
- **Market/language** — country, region, language, slang

### 2. Generate query candidates

Generate 5–12 short queries across these buckets:

| Bucket | Purpose | Example |
|---|---|---|
| Broad anchor | Higher-volume market signal | `cahier de vacances maths` |
| Problem query | Pain language | `lacunes en maths` |
| Action query | What user wants to do | `réviser les maths pendant les vacances` |
| Audience/level query | Segment-specific demand | `préparer sa rentrée en seconde` |
| Commercial query | Buyer intent | `stage maths vacances` |
| Alternative wording | Synonyms/slang | `remise à niveau maths` |
| Time-sensitive query | Short-term trend | `bac maths sujet 2026` |
| Local/regional query | Region/country-specific | `cours de maths Paris été` |

### 3. Score before scraping

Score each candidate 1–5 on:

- likely search phrasing
- topic relevance
- business relevance
- specificity
- expected Trends volume
- seasonality fit
- too-literal risk, reversed so lower risk scores higher

Prioritize:

1. one broad anchor
2. two to four mid-tail candidates
3. one or two commercial/action queries
4. optional local/region variants

### 4. Choose timeframe and geo

| Question | Suggested timeframe |
|---|---|
| Is this currently spiking? | `now 1-d` or `now 7-d` |
| Is this a short campaign/topic? | `today 1-m` or `today 3-m` |
| Is this seasonal? | `today 12-m` |
| Is this evergreen/growing? | `today 5-y` or `all` |

Choose `geo` and `hl` from the target market. If the user asks “worldwide”, leave `geo` empty or use worldwide settings supported by the runner.

### 5. Run Trends slowly

Do not scrape every candidate immediately. Recommended:

- manually test 1–3 strongest candidates, or
- add candidates to rotating cron config and let one query run per tick

### 6. Use related queries as feedback

When Trends returns related/rising queries:

1. keep the ones that match the intent
2. discard irrelevant school level/product/person/location mismatches
3. add strong related queries to the candidate list
4. validate promising ideas later with GSC, DataForSEO, Google Ads, or SERP data

## Output format

```markdown
## Trends Query Candidates

Input: [original title/sentence]
Market: [geo/hl]

### Extracted intent
- Topic:
- Audience:
- Pain/problem:
- Desired outcome:
- Timing:
- Commercial angle:

### Candidate queries
| Priority | Query | Bucket | Timeframe | Geo | Why | Risk |
|---:|---|---|---|---|---|---|
| 1 |  | Broad anchor | today 12-m | FR |  | low |

### Recommended first scrape
1. [query] — [timeframe] — [geo]
2. [query] — [timeframe] — [geo]

### Do not search literally
- [full sentence/title if too editorial]
```

## Guardrails

- Do not search full article titles literally unless the title itself is a known query pattern.
- Avoid very long queries; 2–5 words is often better for Trends.
- Avoid brand names unless the user specifically wants brand demand.
- For low-volume niches, use broader anchors first, then spokes.
- Trends is not volume. Treat this as ideation and validate elsewhere.
