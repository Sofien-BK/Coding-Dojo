from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.user_model import User
from flask_app import DATABASE
from flask import flash


class Recipes:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.descreption = data["descreption"]
        self.instructions = data["instructions"]
        self.under = data["under"]
        self.date = data["date"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.user_id = data["user_id"]
        self.poster = User.get_user_by_id({"id": self.user_id})

    # * ==================== CREATE Recipe ====================
    @classmethod
    def create_recipe(cls, data):
        query = """
                INSERT INTO recipes.all_recipes (name , descreption, instructions,under , date,  user_id)
                VALUES (%(name)s,%(descreption)s,%(instructions)s,%(under)s,%(date)s,%(user_id)s);
                """
        print(query)
        return connectToMySQL(DATABASE).query_db(query, data)

    # * ==================== Get Recipe By ID ====================
    @classmethod
    def get_by_id(cls, data):
        query = """
                     SELECT * FROM recipes.all_recipes
                    WHERE id = %(id)s;
                """
        result = connectToMySQL(DATABASE).query_db(query, data)
        if result:
            return cls(result[0])
        return None

    # * ==================== Get All Recipe ====================
    @classmethod
    def get_all(cls):
        query = """
                    SELECT * FROM recipes.all_recipes;
                """
        results = connectToMySQL(DATABASE).query_db(query)
        all_recipes = []
        for row in results:
            all_recipes.append(cls(row))
        return all_recipes

    # * ==================== Update Recipe ====================
    @classmethod
    def edit(cls, data):
        query = """ UPDATE recipes.all_recipes
                    SET name = %(name)s, descreption = %(descreption)s,instructions= %(instructions)s,under = %(under)s,date = %(date)s,user_id = %(user_id)s
                    WHERE id = %(id)s; 
                """
        return connectToMySQL(DATABASE).query_db(query, data)

    # * ==================== Delete Recipe ====================
    @classmethod
    def delete(cls, data):
        query = """DELETE FROM recipes.all_recipes WHERE id=%(id)s;
        """
        return connectToMySQL(DATABASE).query_db(query, data)

    # * ==================== Recipe VALIDATOR ====================
    @staticmethod
    def validate(data):
        is_valid = True

        if len(data["name"]) < 3:
            flash("name must be at least 3 characters !", "cre" , "tt")
            is_valid = False
        if len(data["descreption"]) < 3:
            flash("descreption must be at least 3 characters !", "cre")
            is_valid = False
        if len(data["instructions"]) < 3:
            flash("instructions must be at least 3 characters !", "cre")
            is_valid = False
        if len(data["date"]) == 0:
            flash("Date Must Not Be Blank", "cre")
            is_valid = False
        else:
            return is_valid
