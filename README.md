# 🎧 Clips API Backend

A lightweight audio library API built with FastAPI, Docker, PostgreSQL, Prometheus, and Grafana.

## 🚀 Features

- Fetch and stream audio previews
- Track play counts per clip
- Built-in monitoring (Prometheus + Grafana)

## 🛠️ Stack

- FastAPI + SQLAlchemy
- PostgreSQL
- Prometheus (via starlette_exporter)
- Grafana
- Docker Compose

## 🧪 Run Locally
Set your environment variables using the sample below:
* **.env.app**: `DATABASE_URL=postgresql://<user>:<password>@db:5432/clips_db`
* **.env.db**:
  `POSTGRES_USER=<user>
  POSTGRES_PASSWORD=<password>
  POSTGRES_DB=clips_db`

In bash:
```bash
docker-compose up --build