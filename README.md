# Chat

Small FastAPI service that answers questions using a fixed BEON.tech context.

## Requirements

- Python 3.14
- `HF_TOKEN` set in your environment or in a `.env` file

## Install

```bash
python -m venv env
source env/bin/activate
pip install -r requirements.txt
```

## Run

```bash
uvicorn app:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

## Endpoint

`POST /chat`

Example:

```bash
curl -X POST http://127.0.0.1:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"message":"What does BEON.tech offer?"}'
```

Response:

```json
{
  "message": "..."
}
```