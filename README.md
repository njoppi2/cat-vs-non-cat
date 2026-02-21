# Cat vs Non-Cat

Image classification project that predicts whether an uploaded image is a cat or not.

This repository combines:

- model experiments in notebooks,
- a FastAPI prediction service,
- and a React frontend for interactive usage.

Live frontend: <https://njoppi2.github.io/cat-vs-non-cat/>

## Tech Stack

- Python, FastAPI, TensorFlow/Keras
- React + TypeScript
- Docker / Docker Compose
- GitHub Actions + GitHub Pages

## Repository Layout

- `deployment/`: FastAPI backend and model-serving files
- `front-end/`: React frontend
- `notebooks-and-models/`: model experiments and training artifacts
- `.github/workflows/`: CI/CD workflow for GitHub Pages

## Quickstart (Docker Compose)

From repository root:

```bash
docker compose up --build
```

Open:

- Frontend: `http://localhost:3000`
- API docs: `http://localhost:8000/docs`

Stop:

```bash
docker compose down
```

## Run Backend Only

```bash
cd deployment
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Then access `http://127.0.0.1:8000/docs`.

## Run Frontend Only

```bash
cd front-end
npm install
npm start
```

Then access `http://localhost:3000`.

## Model Notes

- The project includes logistic regression and neural network notebook baselines.
- The CNN notebook/model is the best-performing experiment in this repository.
- This project is intentionally educational and compact, with small datasets.

## Current Deployment Status

- GitHub Pages frontend is active.
- Heroku instructions remain in `deployment/`, but production API hosting is not currently guaranteed.

## Limitations / Next Improvements

- Replace large model binaries with GitHub Releases or Git LFS.
- Add reproducible training script(s) outside notebooks.
- Add backend unit tests and smoke tests in CI.
