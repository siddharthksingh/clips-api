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

```bash
cp .env.db .env.app
docker-compose up --build