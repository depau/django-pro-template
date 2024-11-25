import uuid

from django.db import models


# noinspection PyPep8Naming
def UUID4PrimaryKey(**kwargs):  # noqa: N802
    return models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, **kwargs)
