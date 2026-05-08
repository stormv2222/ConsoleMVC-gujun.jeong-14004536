from models.user import User


class UserView:
    def show_user(self, user: User) -> None:
        print(f"[User] id={user.id}, name={user.name}, email={user.email}")

    def show_user_list(self, users: list[User]) -> None:
        if not users:
            print("(유저 없음)")
            return
        for user in users:
            self.show_user(user)

    def show_message(self, message: str) -> None:
        print(f">> {message}")

    def get_input(self, prompt: str) -> str:
        return input(prompt).strip()
