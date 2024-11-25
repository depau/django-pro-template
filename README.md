# Django Professional Starter Template

Django is great for building reliable and well-architected web applications. However, setting up a modern project that
follows the current best practices can be time-consuming.

> [!NOTE]
> Developing a complex, multi-faceted product? Check out
> the [Django Professional Multi-Site Starter Template](https://github.com/depau/django-pro-multisite-template) for
> multi-site support.

Use this template to start your next Django project with a solid foundation. It includes:

- A simple, yet powerful setup that allows you to build a modern Django project with ease
  - Great for a single-site project with one configuration
- Follows the [Twelve-Factor App](https://12factor.net/) methodology
  - Configuration is done through environment variables
- Runs asynchronously in production with `asyncio`, [Uvicorn](https://www.uvicorn.org/)
  and [uvloop](https://uvloop.readthedocs.io/user/index.html)
- PEP-compliant: all project configuration happens in `pyproject.toml`
- Using [uv](https://docs.astral.sh/uv/) (in place of Poetry and similar tools),
  [ruff](https://docs.astral.sh/ruff/linter/) (replaces Black, isort, flake8) and [mypy](https://mypy-lang.org/) for the
  best possible Python development experience
- [Django REST Framework](https://www.django-rest-framework.org/) out of the box
  - [DRF Spectacular](https://drf-spectacular.readthedocs.io/en/latest/) is also included for modern OpenAPI support
  - [Django REST Auth](https://django-rest-auth.readthedocs.io/en/latest/introduction.html) for JWT authentication
  - [Django Filter](https://django-filter.readthedocs.io/en/stable/index.html) for filtering
- [Django Debug Toolbar](https://django-debug-toolbar.readthedocs.io/en/latest/installation.html) is ready to use
- [Django Health Check](https://django-health-check.readthedocs.io/en/latest/) is set up for monitoring
- [pre-commit](https://pre-commit.com/) hooks for code quality
- Dockerfile is included for easy deployment

To be added:

- Sample GitHub Actions workflow for CI/CD
- Sample `docker-compose.yml` for local development
- DevContainer support

## Make it yours

1. Clone this repository
2. Rename the `myproject` to your project name
3. Rename the apps (`core`, `mybusinesslogic`) to your app names
4. Make sure to find and replace all instances of `myproject`, `mybusinesslogic`, etc. in the codebase
5. Copy `.env.sample` to `.env` and adjust the environment variables to your needs (hint:
   try [direnv](https://direnv.net/))
6. Run `uv sync --dev --extra production`
7. Run `uv run python manage.py` to run management commands
8. Install the pre-commit hooks with `pre-commit install`

## Design Decisions

### Why `uv`?

`uv` is a new, PEP-compliant build tool that aims to replace Poetry and similar tools.

We chose `uv` because:

- It's incredibly fast
- It's convenient to use
- It's compliant with the latest Python packaging standards and uses `pyproject.toml` without non-standard custom
  sections

### Django project structure

For this project we adopted a peculiar structure that comes from years of experience in building Django projects.

- `project/`: The main code base package
  - `apps/`: All the apps of the project
    - `core/`: The core app of the project, where all common models and APIs are defined
    - Other apps that are specific to the project
  - `utils/`: Utility functions and classes that are shared across the project
  - Site modules (i.e. `urls.py`, `settings.py`, etc.)

The rationale behind this structure is the following:

Unless you're building a complex, multi-site project, there's no need to worry about Django sites. This template
provides an opinionated, yet simple and flexible structure that allows you to focus on building your application.

Some inspiration for this structure comes from the [Taiga](https://github.com/taigaio/taiga-back) backend.
