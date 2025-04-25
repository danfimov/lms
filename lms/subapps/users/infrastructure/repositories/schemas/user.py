from sqlalchemy.dialects.postgresql import VARCHAR
from sqlalchemy.orm import Mapped, mapped_column

from lms.core.infrastructure.repository.schemas.base import DeclarativeBase
from lms.core.infrastructure.repository.schemas.mixins import TimestampMixin, UUIdMixin


class User(DeclarativeBase, UUIdMixin, TimestampMixin):
    username: Mapped[str] = mapped_column(
        VARCHAR(128),
        nullable=False,
        doc='Username of user',
    )
    email: Mapped[str] = mapped_column(
        VARCHAR(256),
        nullable=False,
        doc='Email address of user',
    )
    password: Mapped[str] = mapped_column(
        VARCHAR(256),
        doc='Hashed password of user',
    )
    full_name: Mapped[str] = mapped_column(
        VARCHAR(256),
        nullable=False,
        doc='Username of user',
    )
