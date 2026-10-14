# OpenAI Agents Sample Service

A controlled order-pricing Python target for coding/review tasks. Its canonical checkout contains an intentional discount defect: a 100-unit order with ten-percent discount still totals 100. This is a benchmark fixture, not a production service.

WSL2: `uv sync --locked`; `uv run --offline --locked python -m unittest discover -s tests -v`. One ordinary assertion passes and the explicitly marked known-defect assertion is an expected failure. This result does not prove the defect is fixed.

The independent repair acceptance command is `uv run --offline --locked python tasks/verify_discount.py`: it unconditionally fails on the canonical defect and must pass after a repair in a disposable workspace. It avoids treating an unexpected-success marker as repair acceptance. Fixture metadata is tasks/sample.discount.json.

Automated tasks must use temporary copies or explicitly approved branches. Preserve canonical contents/history, retain source revision/hash, patch/test logs and approval decisions. No remote URL or live-model result is assumed.
