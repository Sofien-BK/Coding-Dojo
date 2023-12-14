from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
import re

EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$")

class User:
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
    
    # * ==================== CREATE A USER ====================
    @classmethod
    def create(cls, data):
        query = """
                INSERT INTO users (first_name ,last_name, email)
                VALUES (%(first_name)s,%(last_name)s,%(email)s);
                """
        print(query)
        return connectToMySQL(DATABASE).query_db(query,data)
    
    # * ==================== GET USER BY ID ====================
    @classmethod
    def get_user_by_id(cls,data):
        query = """
                     SELECT * FROM users
                    WHERE users.id = %(id)s;
                """
        result = connectToMySQL(DATABASE).query_db(query,data)
        if len(result) < 1 :
            return False
        return cls(result[0])
    
    # * ==================== Get All Users ====================
    @classmethod
    def get_all(cls):
        query = """
                    SELECT * FROM user_crud.users;
                """
        results = connectToMySQL(DATABASE).query_db(query)
        all_users = []
        for row in results:
            all_users.append(cls(row))
        return all_users

    # * ==================== USER VALIDATOR ====================
    @staticmethod
    def validate(data):
        is_valid = True
        if len(data["first_name"]) < 1:
            is_valid = False
            flash("first_name Required !", "reg")
        if len(data["email"]) < 1:
            is_valid = False
            flash("email Required !" , "reg")
        elif not EMAIL_REGEX.match(data["email"]):
            flash("Invalid email address", "reg")
            is_valid = False
        return is_valid
    
     # * ==================== Update Recipe ====================
    @classmethod
    def edit(cls, data):
        query = """ UPDATE user_crud.users
                    SET first_name = %(first_name)s, last_name = %(last_name)s,email= %(email)s
                    WHERE id = %(id)s; 
                """
        return connectToMySQL(DATABASE).query_db(query, data)

    # * ==================== Delete Recipe ====================
    @classmethod
    def delete(cls, data):
        query = """DELETE FROM user_crud.users WHERE id=%(id)s;
        """
        return connectToMySQL(DATABASE).query_db(query, data)


