# import the function that will return an instance of a connection
import re
from flask import flash
from dojo_survey.config.mysqlconnection import connectToMySQL
# model the class after the friend table from our database
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class Friend:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM friends;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('first_flask').query_db(query)
        # Create an empty list to append our instances of friends
        friends = []
        # Iterate over the db results and create instances of friends with cls.
        for friend in results:
            friends.append( cls(friend) )
        return friends

    @staticmethod
    def validate_user( user ):
        is_valid = True
        print(user)
        # test whether a field matches the pattern
        if user['name'] == '': 
            flash("Name cannot be blank")
            is_valid = False
        elif len(user['name']) < 3:
            flash("Name is too short.")
            is_valid = False

        if user['location'] == "--Select A Location--" : 
            flash("Please select a location.")
            is_valid = False

        if user['language'] == '--Select A Language--': 
            flash("Please select a language.")
            is_valid = False

        if user['comment'] == '': 
            flash("Please provide a comment.")
            is_valid = False

        print(is_valid)
        return is_valid
            
