from db import db
from repositories.sight_repository import sight_repository as default_sight_repository
from entities.sight import Sight


class SightService:
    """ Class responsible for sight logic."""
    
    def __init__(self, sight_repository=default_sight_repository):
        """ Class constructor. Creates a new sight service.
		Args:"""

        self._sight_repository = sight_repository

    def add_sight(self, birdnames, birdname, date, user, place="", amount=1):
        """ Add a new sight to the user."""
        if birdname in birdnames:
            username = user.get_username()
            sight = Sight(birdname, date, place, amount, username)
            exists = self.get_sight_by_name(birdname, user)
            self._sight_repository.add_sight(sight)
            #user.add_sight(sight)
            if not exists:
                user.increase_score()

    def get_sights(self, user):
        """ Get list of sights from user."""

        sights = self._sight_repository.get_sights(user.get_username())
        sights_list = [list(x) for x in sights]
        return sights_list

    def get_sight_by_name(self, birdname, user):
        """ Get list of sights with given bird name from user."""

        sights = self._sight_repository.get_sights_by_name(birdname, user.get_username())
        return sights

    def get_sights_10(self, user):
        """ Get list of10 recent sights from user."""

        sights = self._sight_repository.get_sights_10(user.get_username())
        return sights

    def get_unique_sights(self, user):
        """ Get the unique sights from user."""

        sights_tuple = self._sight_repository.get_unique_sights(user.get_username())
        sights = [row[0] for row in sights_tuple]
        return sights

    def get_score_db(self, user):
        """ Get the amount of unique sights from user."""

        score = len(self.get_unique_sights(user))
        return score

    def get_score_year(self, user):
        """ Get the amount of unique sights from user this year."""

        score = len(self._sight_repository.get_sights_this_year(user.get_username()))
        return score

    def get_score_month(self, user):
        """ Get the amount of unique sights from user this month."""

        score = len(self._sight_repository.get_sights_this_month(user.get_username()))
        return score

    def get_score_day(self, user):
        """ Get the amount of unique sights from user today."""

        score = len(self._sight_repository.get_sights_today(user.get_username()))
        return score

    def get_percentage(self, score, birds):
        """ Get the amount of unique sights from user today."""

        percentage = 0
        if score > 0:
            percentage = round(score * 100 / len(birds))
        return percentage

    def get_orderr_statics(self, orderrs, user):
        """ Get the order statics of unique sights from user."""

        orderrs = self._sight_repository.get_unique_sights_orderrs(user.get_username())
        orderrs_dict = dict((x, y) for x, y in orderrs)
        return orderrs_dict


sight_service = SightService()
