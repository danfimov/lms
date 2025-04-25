from datetime import datetime

from pydantic import UUID4
from sqlalchemy import func
from sqlalchemy.dialects.postgresql import TIMESTAMP, UUID
from sqlalchemy.orm import Mapped, mapped_column


class UUIdMixin:
    id: Mapped[UUID4] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=func.gen_random_uuid(),
        doc='Unique index of element (type UUID)',
    )


class CreatedAtMixin:
    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True),
        server_default=func.current_timestamp(),
        nullable=False,
        doc='Date and time of create (type TIMESTAMP)',
    )


class UpdatedAtMixin:
    updated_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True),
        server_default=func.current_timestamp(),
        onupdate=func.current_timestamp(),
        nullable=False,
        doc='Date and time of last update (type TIMESTAMP)',
    )


class TimestampMixin(CreatedAtMixin, UpdatedAtMixin):
    pass
