from db import db


class SightRepository:
    """Class that handles database queries for sights."""

    def __init__(self):
        """Class constructor"""

    def add_sight(self, sight):
        """Adds a new sight to database."""

        try:
            sql = "INSERT INTO sights (name_fi, date, place, amount, username) \
                   VALUES (:name, :date, :place, :amount, :username)"
            db.session.execute(sql, {"name": sight.get_name(), "date": sight.get_date(),
                                     "place": sight.get_place(), "amount": sight.get_amount(),
                                     "username": sight.get_username()})
            db.session.commit()
            return True
        except Exception as exception:
            print(exception)
            return False

    def get_sights(self, username):
        """Returns all sights from the user."""
        
        sql = "SELECT * FROM sights WHERE username=:username ORDER BY date DESC"
        result = db.session.execute(sql, {"username":username})
        sights = result.fetchall()
        return sights

    def get_sights_by_name(self, name_fi, username):
        """Returns all sights with specific birdname from the user."""
        
        sql = "SELECT * FROM sights WHERE username=:username AND name_fi=:name_fi ORDER BY date DESC"
        result = db.session.execute(sql, {"username":username, "name_fi":name_fi})
        sights = result.fetchall()
        return sights

    def get_sights_10(self, username):
        """Returns 10 recent sights from the user."""
        
        sql = "SELECT * FROM sights WHERE username=:username ORDER BY date DESC LIMIT 10"
        result = db.session.execute(sql, {"username":username})
        sights = result.fetchall()
        return sights

    def get_sight_by_id(self, sight_id):
        """Returns a sight with given sight_id."""

        sql = "SELECT * FROM sights WHERE sight_id=:sight_id"
        result = db.session.execute(sql, {"sight_id": sight_id})
        sight = result.fetchone()
        if not sight:
            return False
        return sight

    def get_unique_sights(self, username):
        """Returns the amount of unique sights for user."""

        sql = "SELECT DISTINCT (name_fi) FROM sights WHERE username=:username"
        result = db.session.execute(sql, {"username": username})
        sights = result.fetchall()
        return sights

    def get_sights_this_year(self, username):
        """Returns the amount of unique sights for user this year."""

        sql = "SELECT DISTINCT (name_fi) FROM sights WHERE username=:username AND date >= date_trunc('year', CURRENT_DATE)"
        result = db.session.execute(sql, {"username": username})
        sights = result.fetchall()
        return sights

    def get_sights_this_month(self, username):
        """Returns the amount of unique sights for user this month."""

        sql = "SELECT DISTINCT (name_fi) FROM sights WHERE username=:username AND date >= date_trunc('month', CURRENT_DATE)"
        result = db.session.execute(sql, {"username": username})
        sights = result.fetchall()
        return sights

    def get_sights_today(self, username):
        """Returns the amount of unique sights for user this month."""

        sql = "SELECT DISTINCT (name_fi) FROM sights WHERE username=:username AND date >= date_trunc('day', CURRENT_DATE)"
        result = db.session.execute(sql, {"username": username})
        sights = result.fetchall()
        return sights

    def get_unique_sights_orderrs(self, username):
        """Returns the amount orders of unique sights for user."""

        sql = """SELECT orderr, COUNT(*) FROM birds WHERE (name_fi, orderr)
                 IN (SELECT DISTINCT (sights.name_fi), birds.orderr
                     FROM sights JOIN birds ON sights.name_fi = birds.name_fi
                     WHERE username=:username)
                 GROUP BY orderr ORDER BY orderr ASC"""
        result = db.session.execute(sql, {"username": username})
        counts = result.fetchall()
        return counts


sight_repository = SightRepository()
