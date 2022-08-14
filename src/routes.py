from app import app
import secrets
from flask import abort, redirect, render_template, request, session
from services.user_service import user_service
from services.sight_service import sight_service
from services.bird_service import bird_service
from entities.user import UserAccount


@app.route("/")
def index():
    # check if the users exist or not
    if not session.get("user"):
        return redirect("/login")

    user = user_service.from_json(session["user"])
    score = user.get_score()
    username = user.get_username()
    score_year = sight_service.get_score_year(user)
    score_month = sight_service.get_score_month(user)
    score_day = sight_service.get_score_day(user)
    sights10 = sight_service.get_sights_10(user)
    unique_sights = sight_service.get_unique_sights(user)
    birds_list = bird_service.get_birds_list()
    birds = bird_service.get_birds()
    birdnames = bird_service.get_birdnames()
    birdnames_json = bird_service.to_json(birdnames)
    percentage = sight_service.get_percentage(score, birds)
    orderrs = bird_service.get_orderrs()
    orderr_nums = bird_service.get_birdnums_in_orderrs()
    orderr_statics = sight_service.get_orderr_statics(orderrs, user)

    return render_template("index.html", session=session, username=username,
                            sights10=sights10, unique_sights=unique_sights,
                            score=score, score_year=score_year,
                            score_month=score_month, score_day=score_day,
                            birds=birds, birds_list=birds_list,
                            birdnames_json=birdnames_json,
                            percentage=percentage, orderrs=orderrs, 
                            orderr_nums=orderr_nums, orderr_statics=orderr_statics)

@app.route("/signup", methods=["GET"])
def signuppage():
    return render_template("signup.html")

@app.route("/signup", methods=["POST"])
def signup():
    username = request.form["username"]
    password = request.form["password"]
    success, error = user_service.create_user(username, password)
    if success:
        user = UserAccount(username, password)
        user_json = user_service.to_json(user)
        session["user"] = user_json
        session["csrf_token"] = secrets.token_hex(16)
        return redirect("/")
    return render_template("signup.html", error=error)

@app.route("/login", methods=["GET"])
def loginpage():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    success, error = user_service.login(username, password)
    if success:
        user = UserAccount(username, password)
        user.set_score(sight_service.get_score_db(user))
        user_json = user_service.to_json(user)
        session["user"] = user_json
        session["csrf_token"] = secrets.token_hex(16)
        return redirect("/")
    return render_template("login.html", error=error)

@app.route("/logout")
def logout():
    del session["user"]
    del session["csrf_token"]
    return redirect("/")

@app.route("/add-sight", methods=["GET"])
def sight():
    return render_template("sight.html")

@app.route("/add-sight", methods=["POST"])
def add():
    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)

    birdname = request.form["birdname"]
    date = request.form["date"]

    user = user_service.from_json(session["user"])
    birdnames = bird_service.get_birdnames()
    sight_service.add_sight(birdnames, birdname, date, user)
    user_json = user_service.to_json(user)
    session["user"] = user_json
    return redirect("/")

if __name__=='__main__':
    app.run()
