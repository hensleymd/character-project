from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models import user, character

@app.route("/dashboard")
def all_characters_page():
    if "user_id" not in session:
        return redirect("/")
    data = {
        "id": session["user_id"]
    }
    return render_template("dashboard.html", this_user= user.User.get_user_by_id(data), all_characters = character.Character.get_all_characters())

# route that will show the new character page
@app.route("/new/character")
def new_character():
    if "user_id" not in session:
        return redirect("/")
    data = {
        "id": session["user_id"]
    }
    return render_template("/create_character.html", this_user = user.User.get_user_by_id(data))

# shows a specific character
@app.route("/show/<int:id>")
def view_character(id):
    if "user_id" not in session:
        return redirect("/")
    data = {
        "id": id,
    }
    dict = {
        "id": session["user_id"]
    }
    return render_template("/view_character.html", this_user = user.User.get_user_by_id(dict), this_character = character.Character.get_one_character(data))

# route that will show a character to edit
@app.route("/edit/<int:id>")
def edit_character(id):
    if "user_id" not in session:
        return redirect("/")
    data = {
        "id": id,
    }
    return render_template("/edit_character.html", this_character = character.Character.get_one_character(data))

# deletes character from database
@app.route("/characters/delete/<int:id>")
def delete_character(id):
    if "user_id" not in session:
        return redirect("/")
    data = {
        "id": id,
    }
    character.Character.delete_character(data)
    return redirect("/dashboard")

# add a character to database
@app.route("/characters/add_to_db", methods=["POST"])
def add_character_to_db():
    if "user_id" not in session:
        return redirect("/")
    if not character.Character.validate_character(request.form):
        return redirect("/new/character")

    data = {
        "name": request.form["name"],
        "race": request.form["race"],
        "classname": request.form["classname"],
        "level": request.form["level"],
        "user_id": session["user_id"],
    }
    character.Character.add_character(data)
    return redirect("/dashboard")

# edit a character in the database
@app.route("/characters/edit_in_db/<int:id>", methods=["POST"])
def edit_character_in_db(id):
    if "user_id" not in session:
        return redirect("/")
    if not character.Character.validate_character(request.form):
        return redirect(f"/edit/{id}")

    data = {
        "name": request.form["name"],
        "race": request.form["race"],
        "classname": request.form["classname"],
        "level": request.form["level"],
        "id": id,
    }
    character.Character.edit_character(data)
    return redirect("/dashboard")