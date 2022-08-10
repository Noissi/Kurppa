from db import db
import json
from werkzeug.security import check_password_hash, generate_password_hash
from repositories.user_repository import user_repository as default_user_repository
from entities.user import UserAccount


class UserService:
    """ Class responsible for user logic."""
    
    def __init__(self, user_repository=default_user_repository):
        """ Class constructor. Creates a new user service.
		Args:"""

        self._user_repository = user_repository

    def get_user(self, username):
        """ Get a user by username."""

        user = self._user_repository.get_user(username)
        return user

    def login(self, username, password):
        """ Log in user if valid combination."""
        
        if self.valid_username_and_password(username, password):
            return True, "Sisäänkirjautuminen onnistui"
        return False, "Käyttäjänimi tai salasana virheellinen"

    def valid_username_and_password(self, username, password):
        """ Check that the username and password are valid."""

        user = self._user_repository.get_user(username)
        if user:
            hash_value = user.password
            if check_password_hash(hash_value, password):
                return True
        return False

    def create_user(self, username, password):
    	""" Create a new user."""

    	if username == "" or len(username) < 3:
    	    return False, "Käyttäjätunnuksessa oltava vähintään 3 merkkiä"
    	if password == "" or len(password) < 5:
    	    return False, "Salasanassa oltava vähintään 5 merkkiä"

    	user = self._user_repository.get_user_lower(username)
    	if not user:
    	    hash_value = generate_password_hash(password)
    	    new_user = UserAccount(username, hash_value)
    	    self._user_repository.add_user(new_user)
    	    return True, "Käyttäjän luonti onnistui"
    	return False, "Käyttäjänimi on jo käytössä"

    def to_json(self, user):
        """Converts user to json."""

        json_str = json.dumps(user.__dict__)
        return json_str

    def from_json(self, json_str):
        """Converts json to user."""

        json_dict = json.loads(json_str)
        username = json_dict["_username"]
        password = json_dict["_password"]
        sights = json_dict["_sights"]
        score = json_dict["_score"]
        admin = json_dict["_admin"]
        user = UserAccount(username, password)
        user.set_sights(sights)
        user.set_admin(admin)
        user.set_score(score)
        return user


user_service = UserService()
