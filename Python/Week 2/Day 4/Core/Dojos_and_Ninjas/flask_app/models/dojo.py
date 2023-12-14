from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import dojo

from pprint import pprint

DATABASE = "dojos_ninjas"


class Dojo:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"] 
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        # self.all_quotes = []

    #! READ ALL
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(DATABASE).query_db(query)
        dojos = []
        for row in results:
            one_dojo = cls(row)
            dojos.append(one_dojo)

        return dojos

    #! CREATE
    @classmethod
    def save(cls, data):
        query = """
                    INSERT INTO dojos(name)
                    VALUES (%(name)s);
                """

        result = connectToMySQL(DATABASE).query_db(query, data)
        # print(result)
        return result

    #! GET ONE BY ID
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"

        result = connectToMySQL(DATABASE).query_db(query, data)
        dojo = cls(result[0])

        return dojo

    #! UPDATE

    @classmethod
    def update(cls, data):
        update_query = """  
                            UPDATE dojos
                            SET name = %(name)s, 
                            WHERE id = %(id)s;

                        """
        result = connectToMySQL(DATABASE).query_db(update_query, data)
        print(f"====>Upadte result: ")
        return result

    #! DELETE
    # TODO

    #! Get One User with quotes
    # get one user with their quote
    @classmethod
    def one_user_dojos(cls, data):
        query = """
                    SELECT * from dojos
                    JOIN quotes
                    ON ninjas.dojo_id = dojos.id
                    WHERE users.id = %(id)s;
                """

        results = connectToMySQL(DATABASE).query_db(query, data)
        this_dojo = cls(results[0])
        quotes = []
        for row in results:
            #! format the data here for the quote
            #! preapre the dict for the quote constructor

            quote_dict = {
                "id": row["quotes.id"],
                "quote_body": row["quote_body"],
                "created_at": row["quotes.created_at"],
                "updated_at": row["quotes.updated_at"],
                "dojo_id": row["dojo_id"],
            }
            #! now we need to import our Quote model to init it
            this_ninja = ninja.Quote(ninja_dict)

            quotes.append(this_ninja)

        this_dojo.all_ninjas = ninja

        return this_dojo