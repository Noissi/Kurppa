from db import db


class BirdRepository:
    """Class that handles database queries for birds."""

    def __init__(self):
        """Class constructor"""

    def get_birds(self):
        """Returns all birds."""
        
        sql = "SELECT * FROM birds ORDER BY name_fi ASC"
        result = db.session.execute(sql)
        birds = result.fetchall()
        return birds

    def get_birdnames(self):
        """Returns all bird names in Finnish."""
        
        sql = "SELECT name_fi FROM birds ORDER BY name_fi ASC"
        result = db.session.execute(sql)
        birdnames = result.fetchall()
        return birdnames

    def get_names_and_images(self):
        """Returns all bird names in Finnish and images."""
        
        sql = "SELECT name_fi, image FROM birds ORDER BY name_fi ASC"
        result = db.session.execute(sql)
        birds = result.fetchall()
        return birds

    def get_orderrs(self):
        """Returns all orders."""
        
        sql = "SELECT DISTINCT (orderr) FROM birds ORDER BY orderr ASC"
        result = db.session.execute(sql)
        birdnames = result.fetchall()
        return birdnames

    def get_birds_by_order(self, orderr):
        """Returns all birds from selceted order."""
        
        sql = "SELECT * FROM birds WHERE orderr=:orderr ORDER BY name_fi ASC"
        result = db.session.execute(sql, {"orderr": orderr})
        birds = result.fetchall()
        return birds

    def get_birds_by_family(self, family):
        """Returns all birds from selceted family."""
        
        sql = "SELECT * FROM birds WHERE family=:family ORDER BY name_fi ASC"
        result = db.session.execute(sql, {"family": family})
        birds = result.fetchall()
        return birds

    def get_birds_by_rarity(self, rarity):
        """Returns all birds from selceted rarity."""
        
        sql = "SELECT * FROM birds WHERE rarity=:rarity ORDER BY name_fi ASC"
        result = db.session.execute(sql, {"rarity": rarity})
        birds = result.fetchall()
        return birds

    def get_birdnums_in_orderrs(self):
        """Returns the number of birds in every order."""

        sql = """SELECT orderr, COUNT(*) FROM birds
                 GROUP BY orderr ORDER BY orderr ASC"""
        result = db.session.execute(sql)
        counts = result.fetchall()
        return counts

bird_repository = BirdRepository()
