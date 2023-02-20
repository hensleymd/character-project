from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from flask_bcrypt import Bcrypt
from flask_app import app
bcrypt = Bcrypt(app)
from flask_app.models import character

class User:
    db_name = "character_project_schema"

    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.password = data["password"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.characters = []

    @classmethod
    def register_user(cls, data):
        query = """
        INSERT INTO users
        (first_name, last_name, email, password)
        VALUES 
        (%(first_name)s, %(last_name)s, %(email)s, %(password)s);
        """
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def get_user_by_id(cls, data):
        query = """
        SELECT * FROM users
        WHERE id = %(id)s;
        """
        results = connectToMySQL(cls.db_name).query_db(query, data)
        if len(results) == 0:
            return None
        else:
            return cls(results[0])
        
    @classmethod
    def get_user_by_email(cls, data):
        query = """
        SELECT * FROM users
        WHERE email = %(email)s;
        """
        results = connectToMySQL(cls.db_name).query_db(query, data)
        if len(results) == 0:
            return None
        else:
            return cls(results[0])

    @classmethod
    def get_users_character(cls, data):
        query = """
        SELECT * FROM users
        LEFT JOIN characters
        ON users.id = characters.user_id
        WHERE users.id = %(id)s;
        """
        results = connectToMySQL(cls.db_name).query_db(query, data)
        if len(results) == 0:
            return []
        else:
            user_obj = cls(results[0])
            for user_character in results:
                character_dictionary = {
                    "id": user_character["characters.id"],
                    "name": user_character["name"],
                    "race": user_character["race"],
                    "classname": user_character["classname"],
                    "level": user_character["level"],
                    "created_at": user_character["characters.created_at"],
                    "updated_at": user_character["characters.updated_at"]
                }
                character_obj = character.Character(character_dictionary)
                user_obj.characters.append(character_obj)
            return user_obj
    
    @staticmethod
    def validate_registration(form_data):
        is_valid = True
        if len(form_data["first_name"]) < 2:
            flash("First name must be 2 or more characters", "register")
            is_valid = False
        if len(form_data["last_name"]) < 2:
            flash("Last name must be 2 or more characters", "register")
            is_valid = False
        if not EMAIL_REGEX.match(form_data['email']): 
            flash("Invalid email address!", "register")
            is_valid = False
        data = {
            "email": form_data["email"]
        }
        found_user_or_none = User.get_user_by_email(data)
        if found_user_or_none != None:
            flash("Email already taken", "register")
            is_valid = False
        if len(form_data["password"]) < 8:
            flash("Password must be 8 or more characters", "register")
            is_valid = False
        if form_data["password"] != form_data["confirm_password"]:
            flash("Passwords don't match", "register")
            is_valid = False
        return is_valid

    @staticmethod
    def validate_login(form_data):
        if not EMAIL_REGEX.match(form_data['email']): 
            flash("Invalid login credentials", "login")
            return False
        data = {
            "email": form_data["email"]
        }
        found_user_or_none = User.get_user_by_email(data)
        if found_user_or_none == None:
            flash("Invalid login credentials", "login")
            return False
        if not bcrypt.check_password_hash(found_user_or_none.password, form_data["password"]):
            flash("Invalid login credentials", "login")
            return False

        return found_user_or_none