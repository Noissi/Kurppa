from app import app
from flask import redirect, render_template, request, session
from services.user_service import user_service
from services.sight_service import sight_service
from entities.user import UserAccount


@app.route("/")
def index():
    # check if the users exist or not
    if not session.get("user"):
        return redirect("/login")

    return render_template("index.html")

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
        user_json = user_service.to_json(user)
        session["user"] = user_json
        return redirect("/")
    return render_template("login.html", error=error)

@app.route("/logout")
def logout():
    del session["user"]
    return redirect("/")

@app.route("/add-sight", methods=["GET"])
def sight():
    return render_template("sight.html")

@app.route("/add-sight", methods=["POST"])
def add():
    birdname = request.form["birdname"]
    date = request.form["date"]

    user = user_service.from_json(session["user"])
    sight_service.add_sight(birdname, date, user)
    user_json = user_service.to_json(user)
    session["user"] = user_json
    return redirect("/")

if __name__=='__main__':
    app.run()
