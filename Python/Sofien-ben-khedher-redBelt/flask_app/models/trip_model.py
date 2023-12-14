from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.user_model import User
from flask_app import DATABASE
from flask import flash


class Trips:
    def __init__(self, data):
        self.id = data["id"]
        self.destination = data["destination"]
        self.start_date = data["start_date"]
        self.end_date = data["end_date"]
        self.plan = data["plan"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.user_id = data["user_id"]
        self.poster = User.get_user_by_id({"id": self.user_id})

    # * ==================== CREATE Trip ====================
    @classmethod
    def create_trip(cls, data):
        query = """
                INSERT INTO travels.trips (destination , start_date, end_date,plan, user_id)
                VALUES (%(destination)s,%(start_date)s,%(end_date)s,%(plan)s,%(user_id)s);
                """
        print(query)
        return connectToMySQL(DATABASE).query_db(query, data)

    # * ==================== Get Trip By ID ====================
    @classmethod
    def get_by_id(cls, data):
        query = """
                     SELECT * FROM travels.trips
                    WHERE id = %(id)s;
                """
        result = connectToMySQL(DATABASE).query_db(query, data)
        if result:
            return cls(result[0])
        return None

    # * ==================== Get All Trips ====================
    @classmethod
    def get_all(cls):
        query = """
                    SELECT * FROM travels.trips;
                """
        results = connectToMySQL(DATABASE).query_db(query)
        all_trips = []
        for row in results:
            all_trips.append(cls(row))
        return all_trips

    # * ==================== Get All trips for specific user  ====================
    @classmethod
    def get_all_for_user(cls,data):
        query = """
                    SELECT * FROM trips
                    WHERE user_id = %(id)s;
                """
        results = connectToMySQL(DATABASE).query_db(query,data)
        all_trips = []
        for row in results:
            all_trips.append(cls(row))
        return all_trips

    # * ==================== Update Trip ====================
    @classmethod
    def edit(cls, data):
        query = """ UPDATE travels.trips
                    SET destination = %(destination)s, start_date = %(start_date)s,end_date= %(end_date)s,plan = %(plan)s,user_id = %(user_id)s
                    WHERE id = %(id)s; 
                """
        return connectToMySQL(DATABASE).query_db(query, data)

    # * ==================== Delete Trip ====================
    @classmethod
    def delete(cls, data):
        query = """DELETE FROM travels.trips WHERE id=%(id)s;
        """
        return connectToMySQL(DATABASE).query_db(query, data)

    # * ==================== Trip VALIDATOR ====================
    @staticmethod
    def validate(data):
        is_valid = True

        if len(data["destination"]) < 3:
            flash("destination must be at least 3 characters !", "cre")
            is_valid = False
        if len(data["start_date"]) == 0:
            flash("start_date Must Not Be Blank !", "cre")
            is_valid = False
        if len(data["end_date"]) == 0:
            flash("end_date Must Not Be Blank !", "cre")
            is_valid = False
        if len(data["plan"]) < 3:
            flash("plan  must be at least 3 characters", "cre")
            is_valid = False
        else:
            return is_valid
