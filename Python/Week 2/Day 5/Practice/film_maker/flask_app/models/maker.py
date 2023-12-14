from ..config.mySqlConnection import connectToMySQL
from flask_app import DATABASE 

class FilmMaker:
    def __init__(self , data):
        self.id=data['id']
        self.name=data['name']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']

#** Create
@classmethod
def save(cls,data):
    query="""
            insert into film_makers (name) values (%(name)s);
            """
    return connectToMySQL(DATABASE).query_db(query,data)
