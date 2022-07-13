from db import db


class UserRepository:
    """Class that handles database queries for users."""

    def __init__(self):
        """Class constructor"""

    def add_user(self, user):
        """Adds a new user to database."""

        try:
            sql = "INSERT INTO accounts (username, password) VALUES (:username, :password)"
            db.session.execute(sql, {"username": user.get_username(), "password": user.get_password()})
            db.session.commit()
            return True
        except Exception as exception:
            print(exception)
            return False

    def get_user(self, username):
        """Returns a user with given username."""
        
        sql = "SELECT * FROM accounts WHERE username=:username"
        result = db.session.execute(sql, {"username":username})
        user = result.fetchone()
        return user

    def get_user_by_id(self, user_id):
        """Returns user with given user_id."""

        sql = "SELECT * FROM accounts WHERE user_id=:user_id"
        result = db.session.execute(sql, {"user_id": user_id})
        user = result.fetchone()
        if not user:
            return False
        return user

    def delete_all(self):
        sql = """DELETE FROM users"""
        db.session.execute(sql)
        db.session.commit()


user_repository = UserRepository()
