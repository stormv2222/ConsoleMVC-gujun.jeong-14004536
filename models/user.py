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
        user.id = self._next_id
        self._store[self._next_id] = user
        self._next_id += 1
        return user

    def get(self, user_id: int) -> Optional[User]:
        return self._store.get(user_id)

    def get_all(self) -> list[User]:
        return list(self._store.values())

    def update(self, user_id: int, **kwargs) -> Optional[User]:
        user = self._store.get(user_id)
        if user is None:
            return None
        for key, value in kwargs.items():
            if hasattr(user, key) and key != "id":
                setattr(user, key, value)
        return user

    def delete(self, user_id: int) -> bool:
        if user_id not in self._store:
            return False
        del self._store[user_id]
        return True
