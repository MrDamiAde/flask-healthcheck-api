# Flask Healthcheck API (Dockerised)

This is a lightweight Flask API that returns JSON character data — containerised using Docker with a proper **Docker health check**.

I built this to practise using Alpine-based Docker images and to explore how Docker uses health checks to detect app failures in production (e.g. ECS, Kubernetes, etc.).

---

## 🧱 What It Does

- Serves a simple JSON API at `/api/characters`
- Uses an Alpine-based Python image (`python:3.11-alpine`)
- Includes a `HEALTHCHECK` instruction in the Dockerfile
- Docker marks the container as `(healthy)` after successful checks

---

## 🔍 Health Check Example

```dockerfile
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
  CMD curl --fail http://localhost:5000/api/characters || exit 1

##📦 How to Run

```bash
docker-compose up --build
```

Visit: http://localhost:5000/api/characters

Check health:

```bash
docker ps
```

## 💡 Why It Matters

Health checks are essential in real-world deployments as they allow Docker and orchestration tools like ECS or Kubernetes to detect unhealthy containers and recover automatically.t

