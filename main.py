from models.user import UserRepository
from views.user_view import UserView
from controllers.user_controller import UserController

if __name__ == "__main__":
    repo = UserRepository()
    view = UserView()
    controller = UserController(repo, view)
    controller.run()
