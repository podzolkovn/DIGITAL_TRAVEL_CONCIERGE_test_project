import enum
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column

from app.domain.models.abstract import AbstractModel


class UserRole(enum.Enum):
    ADMIN: int = 1
    USER: int = 2


class User(SQLAlchemyBaseUserTable[int], AbstractModel):
    __tablename__ = 'user'
    hashed_password: Mapped[str] = mapped_column(String(length=1024), nullable=False)
    common_role: Mapped[int] = mapped_column(Integer, nullable=False)

    @property
    def role(self) -> UserRole:
        return UserRole(self.common_role)

    @role.setter
    def role(self, role: UserRole):
        self.common_role = role.value
