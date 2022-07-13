class Sight():
    """ Class that represents a single user. """

    def __init__(self, name, date, place, amount, username):
        """ Class constructor. Creates a new user.
        Attributes:
            _name: [String] Unique identifier of the user.
            _time: [String] Password of the user profile.
        """

        self._name = name
        self._date = date
        self._place = place
        self._amount = amount
        self._username = username

    def get_name(self):
        """ Gets the name of the sight."""

        return self._name

    def get_date(self):
        """ Gets the date of the sight."""

        return self._date

    def get_place(self):
        """ Gets the place of the sight."""

        return self._place

    def get_amount(self):
        """ Gets the amount of the sight."""

        return self._amount

    def get_username(self):
        """ Gets the username of the sight."""

        return self._username

    def set_name(self, name):
        """ Sets name.
        Args:
            name: [String] The name to be set.
        """

        self._name = name

    def set_date(self, date):
        """ Sets the date of the sight.
        Args:
            date: [String] The date to be set.
        """

        self._date = date

    def set_username(self, username):
        """ Sets username for the sight.
        Args:
            username: [String] The username to be set.
        """

        self._username = username
