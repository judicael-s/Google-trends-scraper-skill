# Title/Sentence to Trends Query Candidates

Use this template before running the scraper when the user provides a full sentence, article title, page title, campaign idea, or rough concept.

## Input

```text
[Paste user title/sentence/idea here]
```

Market:

```text
geo: [FR / US / worldwide / region]
hl: [fr-FR / en-US / etc.]
```

## Extracted intent

- Topic:
- Audience:
- Pain/problem:
- Desired outcome:
- Timing/seasonality:
- Commercial angle:
- Language/market notes:

## Candidate queries

| Priority | Query | Bucket | Suggested timeframe | Geo | Why this is better than the literal title | Risk |
|---:|---|---|---|---|---|---|
| 1 |  | Broad anchor | today 12-m |  |  | low |
| 2 |  | Problem query | today 12-m |  |  | medium |
| 3 |  | Action query | today 3-m / today 12-m |  |  | medium |
| 4 |  | Commercial query | today 12-m |  |  | medium |
| 5 |  | Audience/level query | today 12-m |  |  | medium |

## Recommended first scrape

Run only the strongest 1–3 candidates first:

```text
1. [query] — [timeframe] — [geo]
2. [query] — [timeframe] — [geo]
3. [query] — [timeframe] — [geo]
```

## Cron candidates

Add these to the rotating config if the user wants slow monitoring:

```json
{
  "queries": [
    {
      "query": "primary broad anchor",
      "intent": "broad anchor derived from title"
    },
    {
      "query": "mid-tail query",
      "intent": "specific user pain/action"
    }
  ]
}
```

## Literal query warning

Do not search this literally unless it is already a natural search phrase:

```text
[original title/sentence]
```
