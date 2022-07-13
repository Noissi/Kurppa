from app import app
from flask import redirect, render_template, request, session
from services.user_service import user_service
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
