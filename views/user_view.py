from models.user import User


class UserView:
    def show_user(self, user: User) -> None:
        pass

    def show_user_list(self, users: list[User]) -> None:
        pass

    def show_message(self, message: str) -> None:
        pass

    def get_input(self, prompt: str) -> str:
        pass
