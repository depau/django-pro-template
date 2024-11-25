#!/bin/bash
set -euo pipefail

if [[ -n "${DJANGO_ADMIN_USERNAME:-}" ]]; then
    echo "[+] Ensuring superuser account exists"
    django-admin ensureadmin --username "$DJANGO_ADMIN_USERNAME" --password "$DJANGO_ADMIN_PASSWORD"
    echo
fi
