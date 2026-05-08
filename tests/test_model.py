from models.user import User, UserRepository


def test_add_assigns_id():
    repo = UserRepository()
    user = repo.add(User(name="Alice", email="alice@example.com"))
    assert user.id == 1


def test_add_increments_id():
    repo = UserRepository()
    u1 = repo.add(User(name="Alice", email="a@a.com"))
    u2 = repo.add(User(name="Bob", email="b@b.com"))
    assert u1.id == 1
    assert u2.id == 2


def test_get_returns_stored_user():
    repo = UserRepository()
    added = repo.add(User(name="Alice", email="alice@example.com"))
    assert repo.get(added.id) is added


def test_get_returns_none_for_unknown_id():
    repo = UserRepository()
    assert repo.get(999) is None


def test_get_all_returns_all_users():
    repo = UserRepository()
    repo.add(User(name="Alice", email="a@a.com"))
    repo.add(User(name="Bob", email="b@b.com"))
    assert len(repo.get_all()) == 2


def test_get_all_empty_repository():
    repo = UserRepository()
    assert repo.get_all() == []


def test_update_changes_name():
    repo = UserRepository()
    user = repo.add(User(name="Alice", email="a@a.com"))
    updated = repo.update(user.id, name="Alicia")
    assert updated.name == "Alicia"


def test_update_preserves_unchanged_fields():
    repo = UserRepository()
    user = repo.add(User(name="Alice", email="a@a.com"))
    repo.update(user.id, name="Alicia")
    assert user.email == "a@a.com"


def test_update_ignores_id_field():
    repo = UserRepository()
    user = repo.add(User(name="Alice", email="a@a.com"))
    original_id = user.id
    repo.update(user.id, id=999)
    assert user.id == original_id


def test_update_returns_none_for_unknown_id():
    repo = UserRepository()
    assert repo.update(999, name="Ghost") is None


def test_delete_removes_user():
    repo = UserRepository()
    user = repo.add(User(name="Alice", email="a@a.com"))
    result = repo.delete(user.id)
    assert result is True
    assert repo.get(user.id) is None


def test_delete_returns_false_for_unknown_id():
    repo = UserRepository()
    assert repo.delete(999) is False


def test_delete_does_not_affect_other_users():
    repo = UserRepository()
    u1 = repo.add(User(name="Alice", email="a@a.com"))
    u2 = repo.add(User(name="Bob", email="b@b.com"))
    repo.delete(u1.id)
    assert repo.get(u2.id) is u2
