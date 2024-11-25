#!/usr/bin/env bash
set -euo pipefail

if [[ "${1:-}" == "django-admin" ]]; then
    # Allow the user to run custom management commands
    exec "$@"
fi 

if [[ "${DJANGO_NO_PINGDB:-}" != 1 ]]; then
    django-admin pingdb || {
        echo "[!] Database is not ready yet, will retry later" >&2
        exit 10
    }
fi

run-parts --verbose /django_init.d

# Fetch ASGI application from Django settings
ASGI_APPLICATION="$(python3 -c 'import django; django.setup(); from django.conf import settings; print(settings.ASGI_APPLICATION)')"

echo "[+] Running ASGI application '${ASGI_APPLICATION}' with uvicorn"
exec uvicorn \
    "${ASGI_APPLICATION}" \
    --loop uvloop \
    --lifespan off \
    --host "$HOST" \
    --port "$PORT"
