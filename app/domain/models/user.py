import enum
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column

from app.domain.models.abstract import AbstractModel


class UserRole(enum.Enum):
    """
    Enum representing user roles with integer values for ADMIN and USER.
    """
    ADMIN: int = 1
    USER: int = 2


class User(SQLAlchemyBaseUserTable[int], AbstractModel):
    """
    Database model for user data, extending the base SQLAlchemy user table
    with additional fields and a role property.
    """
    __tablename__ = 'user'
    hashed_password: Mapped[str] = mapped_column(String(length=1024), nullable=False)
    common_role: Mapped[int] = mapped_column(Integer, nullable=False)

    @property
    def role(self) -> UserRole:
        """
        Returns the user's role as a `UserRole` enum based on the `common_role` value.
        """
        return UserRole(self.common_role)

    @role.setter
    def role(self, role: UserRole):
        """
        Sets the user's role by assigning the corresponding `UserRole` value to `common_role`.
        """
        self.common_role = role.value
