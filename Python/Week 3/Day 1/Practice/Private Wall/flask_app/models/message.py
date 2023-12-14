from flask_app.config.mysqlconnection import connectToMySQL
from datetime import datetime
from flask_app.models import user
import math

class Message   :
    DB = 'private_wall'
    def __init__(self,db_data):
        self.id = db_data['id']
        self.content = db_data['content']
        self.sender = db_data['sender']
        self.reciever = db_data['receiver']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']





    @classmethod
    def get_user_messages(cls,user_id):
        receiver = user.User.get_by_id(user_id)
        query = """SELECT messages.*,
                first_name, last_name, email, senders.created_at as sender_created_at, senders
                JOIN users as senders on messages.sender_id = senders.id
                WHERE receiver_id =  %(id)s"""
        results = connectToMySQL(cls.DB).query_db(query,{"id": user_id})