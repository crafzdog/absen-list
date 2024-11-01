from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import VARCHAR

from .. import db


class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(VARCHAR(50), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(VARCHAR(50), unique=True, nullable=False)
