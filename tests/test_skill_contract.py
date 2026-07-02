import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_skill_files_exist():
    for rel in [
        'SKILL.md',
        'README.md',
        'references/workflows.md',
        'references/troubleshooting.md',
        'templates/client-trends-radar.config.json',
        'templates/hermes-cron-script.sh',
    ]:
        assert (ROOT / rel).exists(), rel


def test_template_config_is_valid_json():
    data = json.loads((ROOT / 'templates/client-trends-radar.config.json').read_text(encoding='utf-8'))
    assert data['client_id'] == 'client-slug'
    assert data['min_hours_between_same_query'] >= 8
    assert len(data['queries']) >= 2


def test_skill_contains_cron_and_guardrails():
    text = (ROOT / 'SKILL.md').read_text(encoding='utf-8')
    assert 'every 8 hours' in text or 'every 8h' in text
    assert 'not search volume' in text.lower()
    assert 'GOOGLE_TRENDS_RATE_LIMITED' in text
