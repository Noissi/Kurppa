from db import db
import json
from repositories.bird_repository import bird_repository as default_bird_repository


class BirdService:
    """ Class responsible for sight logic."""
    
    def __init__(self, bird_repository=default_bird_repository):
        """ Class constructor. Creates a new bird service.
		Args:"""

        self._bird_repository = bird_repository

    def get_birds(self):
        """ Get list of birds."""

        birds = self._bird_repository.get_birds()
        return birds

    def get_birdnames(self):
        """ Get list of bird names in Finnish."""

        result = self._bird_repository.get_birdnames()
        birdnames = [row[0] for row in result]
        return birdnames

    def get_orderrs(self):
        """ Get list of orders."""

        result = self._bird_repository.get_orderrs()
        orderrs = [row[0] for row in result]
        return orderrs

    def get_birdnums_in_orderrs(self):
        """ Get the amount of birds in every order."""

        orderrnum = self._bird_repository.get_birdnums_in_orderrs()
        orderrnum_dict = dict((x, y) for x, y in orderrnum)
        return orderrnum_dict

    def to_json(self, birdnames):
        """Converts birdnames to json."""

        json_str = json.dumps(birdnames)
        return json_str


bird_service = BirdService()
