#!/bin/bash
set -euo pipefail

echo "[+] Applying migrations"
django-admin migrate
echo