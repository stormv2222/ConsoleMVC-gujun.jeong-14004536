from models.user import User, UserRepository
from views.user_view import UserView


class UserController:
    def __init__(self, repository: UserRepository, view: UserView) -> None:
        self._repo = repository
        self._view = view

    def create_user(self) -> None:
        pass

    def list_users(self) -> None:
        pass

    def update_user(self) -> None:
        pass

    def delete_user(self) -> None:
        pass

    def run(self) -> None:
        pass
