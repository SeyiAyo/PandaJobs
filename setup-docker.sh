#!/usr/bin/env bash
set -euo pipefail

MODE="${1:-dev}"

case "$MODE" in
  default)
    COMPOSE_FILE="docker-compose.yml"
    ;;
  dev)
    COMPOSE_FILE="docker-compose-dev.yml"
    ;;
  prod)
    COMPOSE_FILE="docker-compose-prod.yml"
    ;;
  help|-h|--help)
    echo "Usage: ./setup-docker.sh [default|dev|prod]"
    echo
    echo "default  Build and run docker-compose.yml"
    echo "dev      Build and run docker-compose-dev.yml"
    echo "prod     Build and run docker-compose-prod.yml"
    exit 0
    ;;
  *)
    echo "Unknown mode: $MODE"
    echo "Usage: ./setup-docker.sh [default|dev|prod]"
    exit 1
    ;;
esac

if ! command -v docker >/dev/null 2>&1; then
  echo "Docker is not installed or not available on PATH."
  exit 1
fi

if ! docker compose version >/dev/null 2>&1; then
  echo "Docker Compose v2 is not available. Install Docker Compose or update Docker."
  exit 1
fi

if [ ! -f "$COMPOSE_FILE" ]; then
  echo "Compose file not found: $COMPOSE_FILE"
  exit 1
fi

echo "Starting PandaJobs in $MODE mode using $COMPOSE_FILE..."
docker compose -f "$COMPOSE_FILE" up --build -d

echo
echo "PandaJobs is starting on http://localhost:8000"
echo "View logs with: docker compose -f $COMPOSE_FILE logs -f"
echo "Stop with:      docker compose -f $COMPOSE_FILE down"
