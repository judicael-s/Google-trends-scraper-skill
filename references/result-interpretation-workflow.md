# Google Trends Result Interpretation Workflow

Use this workflow after the scraper returns JSON or a cron summary. The goal is to turn raw Google Trends output into clear numbers and a plain-language result summary.

## Core rule

Google Trends numbers are **index values**, not absolute search volume.

```text
100 = highest relative interest point in the selected query/geo/timeframe
50 = about half the relative interest of that peak
0 = too low to display for that period, not necessarily zero searches
```

Never present Trends index values as monthly searches. If the user needs real search-volume estimates, recommend DataForSEO, Google Ads Keyword Planner, Search Console impressions, or a calibration workflow.

## Status labels

Classify every result before interpreting it:

| Status | When to use | Meaning |
|---|---|---|
| `usable` | timeline has multiple points and at least one non-zero value | Useful Trends signal |
| `weak_signal` | few non-zero points or only regional/related data | Query may be low-volume or too specific |
| `unclear` | no timeline and no related/region signal | Try broader query or warm profile |
| `rate_limited` | error code is `GOOGLE_TRENDS_RATE_LIMITED` | Cooldown; not a demand signal |
| `blocked_or_failed` | browser/parser/launch errors | Fix setup before interpreting demand |

## Clear numbers to extract

From `interest_over_time` and `summary`, compute or display:

| Number | Definition |
|---|---|
| Timeline points | count of graph points |
| Non-zero periods | count of points with value > 0 |
| Zero/low-display periods | count of points with value == 0 |
| Peak value | max graph value, usually 100 when data exists |
| Peak period | formatted time/date where max occurs |
| Latest value | last graph value |
| Average value | mean graph value |
| Trend delta | latest value minus first value |
| First value | first graph value |
| Recent 4-period average | average of last 4 points when available |
| Non-zero share | non-zero periods / timeline points |
| Region count | count of regions returned |
| Top regions | top 3–5 regions with values |
| Related query count | count of related queries returned |
| Top related queries | first 3–5 related queries |

## Plain-language interpretation rules

Use the numbers to explain what happened:

- **Strong seasonal query**: long low baseline + sharp recurring peaks around a season.
- **Evergreen query**: many non-zero periods and moderate average value.
- **Currently rising**: latest value is high vs recent average or trend delta is strongly positive.
- **Declining**: latest value is much lower than peak/recent average.
- **Low-volume/too-specific**: timeline has mostly zero values but some regions/related queries exist.
- **Possibly wrong query phrasing**: no timeline + no related queries + query is long/editorial.

## Output template

```markdown
## Google Trends Result Summary — [query]

Status: usable / weak_signal / unclear / rate_limited / blocked_or_failed
Data type: Google Trends index values, not absolute search volume
Geo/language: [geo] / [hl]
Timeframe: [timeframe]

### Clear graph numbers
| Metric | Value |
|---|---:|
| Timeline points |  |
| Non-zero periods |  |
| Zero/low-display periods |  |
| Peak value |  |
| Peak period |  |
| Latest value |  |
| Average value |  |
| Trend delta |  |
| Recent 4-period average |  |
| Region count |  |
| Related query count |  |

### Top regions
| Region | Index value |
|---|---:|

### Top related queries
| Query | Type | Value |
|---|---|---:|

### Interpretation
- [plain-language explanation]

### What this does / does not mean
- This shows relative search interest inside the selected Trends context.
- This does not show monthly search volume.
- A zero period means too low to display, not guaranteed zero searches.

### Recommended next step
- [broader query / comparison query / validation source / cron monitoring]
```

## Recommendation logic

If status is `usable`:

- summarize seasonality/current trend
- recommend comparison with 1–3 crafted candidates
- suggest validation source if SEO action is being considered

If status is `weak_signal`:

- say the query may be too narrow
- suggest a broader anchor and related wording
- keep useful region/related clues

If status is `unclear`:

- do not conclude there is no demand
- run the query-crafting workflow and try broader anchors

If status is `rate_limited`:

- stop testing repeatedly
- wait/cooldown
- warm/login browser profile if needed

If status is `blocked_or_failed`:

- fix browser/profile/parser before interpreting demand

## Example interpretation

```text
This is a usable seasonal query. The peak value is 100 in late June / early July, the latest value is 97, and the average over the year is only 10.98. That means demand is concentrated around the summer/rentrée window. It is a good broad anchor for content planning, but it is not a search-volume estimate. Validate with DataForSEO, Google Ads, or GSC before prioritizing production.
```
