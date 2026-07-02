#!/usr/bin/env bash
set -euo pipefail

# Edit these paths for each client/profile.
SCRAPER_DIR="/path/to/Google-trends-scraper"
CONFIG_PATH="/path/to/client-trends-radar.config.json"
STATE_PATH="/path/to/client-trends-radar-state.json"
OUTPUT_DIR="/path/to/google-trends-raw"

cd "$SCRAPER_DIR"
python rotating_trends_cron.py \
  --config "$CONFIG_PATH" \
  --state "$STATE_PATH" \
  --output-dir "$OUTPUT_DIR"
