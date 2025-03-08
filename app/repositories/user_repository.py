from app.models.user import User


def get_user_by_username(username: str) -> User:
    return User.query.filter_by(username=username).first()


def get_user_by_id(id: int) -> User:
    return User.query.get(id)
