class UserAccount():
    """ Class that represents a single user. """

    def __init__(self, username, password):
        """ Class constructor. Creates a new user.
        Attributes:
            _username: [String] Unique identifier of the user.
            _password: [String] Password of the user profile.
        """

        self._username = username
        self._password = password
        self._sights = []
        self._score = 0
        self._admin = False

    def get_username(self):
        """ Gets the name of the user."""

        return self._username

    def get_password(self):
        """ Gets the password of the user."""

        return self._password

    def get_sights(self):
        """ Gets the sights of the user."""

        return self._sights

    def get_score(self):
        """ Gets the score of the user."""

        return self._score

    def get_admin(self):
        """ Gets the admin status of the user."""

        return self._admin

    def set_username(self, username):
        """ Sets username.
        Args:
            username: [String] The username to be set.
        """

        self._username = username

    def set_password(self, password):
        """ Sets user's password.
        Args:
            password: [String] The password to be set.
        """

        self._password = password

    def set_sights(self, sights):
        """ Sets user's sights.
        Args:
            sights: [List String] The sights to be set.
        """

        self._sights = sights

    def set_score(self, score):
        """ Sets user's score.
        Args:
            score: [Integer] The score to be set.
        """

        self._score = score

    def set_admin(self, boolean):
        """ Sets user's admin status.
        Args:
            admin: [boolean] The admin status to be set.
        """

        self._admin = boolean

    def add_sight(self, sight):
        """ Adds a sight to the user."""

        self._sights.append(sight)

    def remove_sight(self, sight):
        """ Removes a sight from the user."""

        if sight in self._sights:
            self._sights.remove(sight)

    def increase_score(self):
        """ Increases user's score."""

        self._score += 1

    def is_admin(self):
        return self._admin
