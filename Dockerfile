FROM ghcr.io/astral-sh/uv:bookworm-slim AS base

COPY .python-version pyproject.toml uv.lock /app/
WORKDIR /app
RUN --mount=type=cache,target=/app/.cache \
    uv python install && \
    uv venv && \
    uv sync --no-install-project --no-dev --extra production

################################################################################
FROM base AS build

COPY . /app
WORKDIR /app

RUN --mount=type=cache,target=/app/.cache \
    uv sync --dev --no-install-project && \
    uv build

################################################################################
FROM base

COPY docker/entrypoint.sh /
COPY docker/django_init.d /django_init.d

RUN --mount=type=cache,target=/app/.cache \
    --mount=type=bind,from=build,source=/app/dist,target=/app/dist \
    uv pip install /app/dist/*.whl

ENV PATH="/app/.venv/bin:$PATH"

ARG DJANGO_SITE="myproject"
ENV DJANGO_SETTINGS_MODULE="$DJANGO_SITE.settings"

ARG WEB_CONCURRENCY=4
ENV WEB_CONCURRENCY=$WEB_CONCURRENCY

ENV DEBUG=off

ARG HOST=0.0.0.0
ENV HOST=$HOST
ARG PORT=8000
ENV PORT=$PORT

EXPOSE $PORT
ENTRYPOINT ["/entrypoint.sh"]
CMD []
