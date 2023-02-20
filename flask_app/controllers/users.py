from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models import user
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route("/")
def login_page():
    return render_template("login.html")

@app.route("/user/characters")
def users_character():
    if "user_id" not in session:
        return redirect("/")
    data = {
        "id": session["user_id"]
    }
    return render_template("users_characters.html", this_users_characters = user.User.get_users_character(data))

@app.route("/register", methods=["POST"])
def register_user():
    if not user.User.validate_registration(request.form):
        return redirect("/")
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        "password": bcrypt.generate_password_hash(request.form["password"]),
    }
    session["user_id"] = user.User.register_user(data)

    return redirect("/dashboard")

@app.route("/login", methods=["POST"])
def log_user_in():
    found_user_or_false = user.User.validate_login(request.form)
    if not found_user_or_false:
        return redirect("/")
    session["user_id"] = found_user_or_false.id
    return redirect("/dashboard")


@app.route("/logout")
def logout_user():
    session.clear()
    return redirect('/')