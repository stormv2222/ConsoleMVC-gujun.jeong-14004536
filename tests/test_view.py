from models.user import User
from views.user_view import UserView


def _make_user(user_id: int, name: str, email: str) -> User:
    user = User(name=name, email=email)
    user.id = user_id
    return user


def test_show_user_contains_id(capsys):
    view = UserView()
    view.show_user(_make_user(1, "Alice", "alice@example.com"))
    assert "id=1" in capsys.readouterr().out


def test_show_user_contains_name(capsys):
    view = UserView()
    view.show_user(_make_user(1, "Alice", "alice@example.com"))
    assert "Alice" in capsys.readouterr().out


def test_show_user_contains_email(capsys):
    view = UserView()
    view.show_user(_make_user(1, "Alice", "alice@example.com"))
    assert "alice@example.com" in capsys.readouterr().out


def test_show_user_list_prints_all_users(capsys):
    view = UserView()
    view.show_user_list([
        _make_user(1, "Alice", "a@a.com"),
        _make_user(2, "Bob", "b@b.com"),
    ])
    output = capsys.readouterr().out
    assert "Alice" in output
    assert "Bob" in output


def test_show_user_list_empty_shows_placeholder(capsys):
    view = UserView()
    view.show_user_list([])
    assert "유저 없음" in capsys.readouterr().out


def test_show_message_includes_content(capsys):
    view = UserView()
    view.show_message("저장 완료")
    assert "저장 완료" in capsys.readouterr().out


def test_show_message_includes_prefix(capsys):
    view = UserView()
    view.show_message("저장 완료")
    assert ">>" in capsys.readouterr().out
