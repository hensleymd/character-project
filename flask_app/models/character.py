from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user

class Character:
    db_name = "character_project_schema"

    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.race = data["race"]
        self.classname = data["classname"]
        self.level = data["level"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.user = None

    @classmethod
    def add_character(cls, data):
        query = """
        INSERT INTO characters
        (name, race, classname, level, user_id)
        VALUES
        (%(name)s, %(race)s, %(classname)s, %(level)s, %(user_id)s);
        """
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def get_all_characters(cls):
        query = """
        SELECT * FROM characters
        JOIN users
        ON characters.user_id = users.id;
        """
        results = connectToMySQL(cls.db_name).query_db(query)
        if len(results) == 0:
            return []
        else:
            all_character_objects = []
            for character_dictionary in results:
                character_obj = cls(character_dictionary)
                # Grab the user's info
                user_dictionary = {
                    "id": character_dictionary["users.id"],
                    "first_name": character_dictionary["first_name"],
                    "last_name": character_dictionary["last_name"],
                    "email": character_dictionary["email"],
                    "password": character_dictionary["password"],
                    "created_at": character_dictionary["users.created_at"],
                    "updated_at": character_dictionary["users.updated_at"]
                }
                # Create the User object
                user_obj = user.User(user_dictionary)
                # Link this User to this character
                character_obj.user = user_obj
                # Add this character to the list of all character objects
                all_character_objects.append(character_obj)
            return all_character_objects

    @classmethod
    def get_one_character(cls, data):
        query = """
        SELECT * FROM characters
        JOIN users 
        ON characters.user_id = users.id
        WHERE characters.id = %(id)s;
        """
        results = connectToMySQL(cls.db_name).query_db(query, data)
        if len(results) == 0:
            return None
        else:
            # create a variable for results[index] for clarity
            character_dictionary = results[0]
            character_obj = cls(character_dictionary)
            # Grab the user's info
            user_dictionary = {
                "id": character_dictionary["users.id"],
                "first_name": character_dictionary["first_name"],
                "last_name": character_dictionary["last_name"],
                "email": character_dictionary["email"],
                "password": character_dictionary["password"],
                "created_at": character_dictionary["users.created_at"],
                "updated_at": character_dictionary["users.updated_at"]
            }
            # Create the User object
            user_obj = user.User(user_dictionary)
            # Link this User to this character
            character_obj.user = user_obj
        return character_obj

    @classmethod
    def edit_character(cls, data):
        query= """
        UPDATE characters SET
        name = %(name)s,
        race = %(race)s,
        classname = %(classname)s,
        level = %(level)s
        WHERE
        id = %(id)s;
        """
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def delete_character(cls, data):
        query= "DELETE FROM characters WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @staticmethod
    def validate_character(form_data):
        is_valid = True
        if len(form_data["name"]) < 2:
            flash ("Name must be 2 or more characters")
            is_valid = False
        if len(form_data["race"]) < 2:
            flash ("Race must be 2 or more characters")
            is_valid = False
        if len(form_data["classname"]) < 2:
            flash ("Class must be 2 or more characters")
            is_valid = False
        if len(form_data["level"]) < 1:
            flash ("Level must be between 1 and 20")
            is_valid = False
        return is_valid