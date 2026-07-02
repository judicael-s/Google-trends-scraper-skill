# Troubleshooting

## Google returns 429 / Too Many Requests

Meaning: Google is rate-limiting the browser/session/IP.

Actions:

1. Stop repeated tests.
2. Wait 30–60 minutes.
3. Warm the dedicated browser profile with `open-trends-profile.ps1`.
4. Log in if Google asks.
5. Reduce cadence to one query every 8h or slower.
6. Prefer broad anchor queries.

Never treat 429 as zero demand.

## Browser opens then closes too quickly

`run-trends.ps1` is the automated collector and closes the browser after collection. Use `open-trends-profile.ps1` when you need a browser to remain open for login/warmup.

## Browser profile already in use

Error often contains:

```text
Opening in existing browser session
profile is already in use
```

Close the Chrome/Edge window using that profile, then retry.

## No timeline data

`NO_TIMELINE_DATA` can mean:

- query is very low volume
- Google UI/API changed
- partial capture
- temporary friction not detected as 429

Compare a broader anchor query before deciding demand is weak.

## WSL cannot open visible browser

Expected. WSL has no Windows desktop display. Use the PowerShell wrappers so Windows Chrome/Edge opens on the Windows host.

## Node/Playwright missing

Run:

```bash
npm install
npx playwright install chromium
```

If system dependencies are missing in WSL, prefer the Windows-side runner rather than WSL headless.

## PowerShell multiline command errors

Use one-line commands when giving instructions to non-technical users. Backticks in PowerShell are fragile if there are trailing spaces or blank lines.

## Security reminders

- Do not commit `UserDataDir` browser profiles.
- Do not copy cookies between clients.
- Do not paste tokens/API keys into configs.
- Keep raw client outputs in client-private folders.
