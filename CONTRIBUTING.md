# Contributing

## Setup

Run full stack:

```bash
docker compose up --build
```

## Before Opening a PR

Run:

```bash
python -m compileall deployment/app
PYTHONPATH=deployment python -m unittest discover -s deployment/tests -p "test_*.py"
cd front-end && npm ci && npm run build
```

## Pull Request Guidelines

- Keep PRs scoped and document behavior changes.
- Update `README.md` when commands, deployment, or structure changes.
- Include validation output or CI run link.
- Never commit credentials, `.env` files, or large generated artifacts.
