# Deployment Backend

FastAPI backend for the cat classifier project.

## Local Run

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open:

- API root: `http://127.0.0.1:8000/`
- API docs: `http://127.0.0.1:8000/docs`

## Docker Run

```bash
docker build -t cat-api .
docker run --rm -p 8000:80 cat-api
```

## Notes

- `heroku.yml` is kept only as legacy deployment metadata.
- The recommended local orchestration path for this repository is `docker compose up --build` from the project root.
