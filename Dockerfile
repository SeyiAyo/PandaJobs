FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

COPY requirements.txt .

# requirements.txt is currently UTF-16 LE, so normalize it before pip reads it.
RUN iconv -f UTF-16 -t UTF-8 requirements.txt > requirements.utf8.txt \
    && pip install --upgrade pip \
    && pip install -r requirements.utf8.txt

COPY . .

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
  CMD python -c "import sys, urllib.request; urllib.request.urlopen('http://127.0.0.1:8000/health/', timeout=3); sys.exit(0)"

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
