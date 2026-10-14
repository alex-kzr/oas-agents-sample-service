# agents-sample-service

Controlled Python coding/review target with defects, tests and task fixtures.

Status: independent Git repository scaffold only. No runnable application, dependency lock or completed test exists. Proposed GitHub name: `openai-agents-sample-service`; no remote configured or assumed.

Ownership and future interfaces: see the umbrella docs/component-contracts.md and SPEC §§3,5,10. Those are documentation paths in the parent checkout, not imports or independently packaged dependencies. This repository must gain its own contracts/configuration/test instructions before runtime implementation.

Python import package target: `sample_service`. Python 3.11+ pending the verified SDK pin; uv pyproject.toml and uv.lock will be created after dependency verification. Component tests will use unittest.

Current inspection: `git status --short` and `git log -1`. Test command is not available yet; empty test directories do not establish passing tests. Future implementation keeps code/tests and version history here. No model/API calls or Docker launch in this milestone.
