import pytest
from models.user import UserRepository
from views.user_view import UserView
from controllers.user_controller import UserController


@pytest.fixture
def ctx():
    repo = UserRepository()
    view = UserView()
    ctrl = UserController(repo, view)
    return ctrl, repo, view


def _set_inputs(view: UserView, *values: str):
    it = iter(values)
    view.get_input = lambda prompt: next(it)


# --- create_user ---

def test_create_user_adds_to_repository(ctx):
    ctrl, repo, view = ctx
    _set_inputs(view, "Alice", "alice@example.com")
    ctrl.create_user()
    assert len(repo.get_all()) == 1


def test_create_user_stores_correct_name(ctx):
    ctrl, repo, view = ctx
    _set_inputs(view, "Alice", "alice@example.com")
    ctrl.create_user()
    assert repo.get_all()[0].name == "Alice"


def test_create_user_stores_correct_email(ctx):
    ctrl, repo, view = ctx
    _set_inputs(view, "Alice", "alice@example.com")
    ctrl.create_user()
    assert repo.get_all()[0].email == "alice@example.com"


def test_create_user_assigns_id(ctx):
    ctrl, repo, view = ctx
    _set_inputs(view, "Alice", "alice@example.com")
    ctrl.create_user()
    assert repo.get_all()[0].id == 1


# --- list_users ---

def test_list_users_shows_created_user(ctx, capsys):
    ctrl, repo, view = ctx
    _set_inputs(view, "Alice", "alice@example.com")
    ctrl.create_user()
    ctrl.list_users()
    assert "Alice" in capsys.readouterr().out


def test_list_users_empty_shows_placeholder(ctx, capsys):
    ctrl, _, _ = ctx
    ctrl.list_users()
    assert "유저 없음" in capsys.readouterr().out


# --- update_user ---

def test_update_user_changes_name(ctx):
    ctrl, repo, view = ctx
    _set_inputs(view, "Alice", "alice@example.com")
    ctrl.create_user()

    _set_inputs(view, "1", "Alicia")
    ctrl.update_user()

    assert repo.get(1).name == "Alicia"


def test_update_user_unknown_id_shows_error(ctx, capsys):
    ctrl, _, view = ctx
    _set_inputs(view, "999", "Alicia")
    ctrl.update_user()
    assert "없음" in capsys.readouterr().out


# --- delete_user ---

def test_delete_user_removes_from_repository(ctx):
    ctrl, repo, view = ctx
    _set_inputs(view, "Alice", "alice@example.com")
    ctrl.create_user()

    _set_inputs(view, "1")
    ctrl.delete_user()

    assert repo.get(1) is None


def test_delete_user_unknown_id_shows_error(ctx, capsys):
    ctrl, _, view = ctx
    _set_inputs(view, "999")
    ctrl.delete_user()
    assert "없음" in capsys.readouterr().out
