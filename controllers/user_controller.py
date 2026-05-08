from models.user import User, UserRepository
from views.user_view import UserView


class UserController:
    def __init__(self, repository: UserRepository, view: UserView) -> None:
        self._repo = repository
        self._view = view

    def create_user(self) -> None:
        name = self._view.get_input("이름: ")
        email = self._view.get_input("이메일: ")
        user = self._repo.add(User(name=name, email=email))
        self._view.show_message(f"생성 완료 (id={user.id})")

    def list_users(self) -> None:
        users = self._repo.get_all()
        self._view.show_user_list(users)

    def update_user(self) -> None:
        user_id = int(self._view.get_input("수정할 id: "))
        name = self._view.get_input("새 이름: ")
        user = self._repo.update(user_id, name=name)
        if user:
            self._view.show_message("수정 완료")
        else:
            self._view.show_message("해당 id 없음")

    def delete_user(self) -> None:
        user_id = int(self._view.get_input("삭제할 id: "))
        success = self._repo.delete(user_id)
        self._view.show_message("삭제 완료" if success else "해당 id 없음")

    def run(self) -> None:
        menu = {
            "1": ("유저 생성", self.create_user),
            "2": ("유저 목록", self.list_users),
            "3": ("유저 수정", self.update_user),
            "4": ("유저 삭제", self.delete_user),
        }
        while True:
            print("\n--- MVC POC ---")
            for key, (label, _) in menu.items():
                print(f"  {key}. {label}")
            print("  0. 종료")

            choice = self._view.get_input("선택: ")
            if choice == "0":
                break
            if choice in menu:
                menu[choice][1]()
            else:
                self._view.show_message("잘못된 입력")
