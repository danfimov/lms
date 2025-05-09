from typing import Callable

import sqlalchemy as sa
from sqlalchemy import orm


convention: dict[str, str | Callable[[sa.Constraint, sa.Table], str]] = {
    'all_column_names':
        lambda constraint, table: '_'.join(
            [column.name for column in constraint.columns.values()]  # type: ignore
        ),
    'ix': 'ix__%(table_name)s__%(all_column_names)s',
    'uq': 'uq__%(table_name)s__%(all_column_names)s',
    'ck': 'ck__%(table_name)s__%(constraint_name)s',
    'fk': 'fk__%(table_name)s__%(all_column_names)s__' '%(referred_table_name)s',
    'pk': 'pk__%(table_name)s',
}

metadata = sa.MetaData(naming_convention=convention)
DeclarativeBase = orm.declarative_base(metadata=metadata)


__all__ = [
    'DeclarativeBase',
    'metadata',
]
