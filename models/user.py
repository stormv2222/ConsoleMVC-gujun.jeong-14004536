from dataclasses import dataclass, field
from typing import Optional


@dataclass
class User:
    name: str
    email: str
    id: int = field(default=0, init=False)


class UserRepository:
    def __init__(self):
        self._store: dict[int, User] = {}
        self._next_id: int = 1

    def add(self, user: User) -> User:
        pass

    def get(self, user_id: int) -> Optional[User]:
        pass

    def get_all(self) -> list[User]:
        pass

    def update(self, user_id: int, **kwargs) -> Optional[User]:
        pass

    def delete(self, user_id: int) -> bool:
        pass
