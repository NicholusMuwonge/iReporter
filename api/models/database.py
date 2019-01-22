"""

where my sql syntax for persisting data in the database will be contained

"""
import psycopg2 
from psycopg2.extras import RealDictCursor
import os
from dotenv import load_dotenv  # loadenv is used to set up an environment
from flask import Flask, json, jsonify


class DatabaseConnection:
    def __init__(self):
        if os.getenv('Heroku_environment') == 'heroku_database':  # set cloud database environment
                self.connection = psycopg2.connect(
                host="", 
                database="", user="",
                port="5432", 
                password=""
                )
        else:
            self.connection = psycopg2.connect(
            host="localhost", 
            database="db_test", user="postgres",
            port="5432", 
            password=""
            )
        self.connection.autocommit = True  # make research of use
        self.cursor = self.connection.cursor()  # a cursor object is created used to connect and communicate with database
        self.dict_cursor = self.connection.cursor(
            cursor_factory=RealDictCursor
            )  # make more research on the realdict cusor

    def create_tables(self):
        """
        This is the function that creates the tables in the database where data will be persisted
        """
        table_creation_commands="""CREATE TABLE IF NOT EXISTS "user_list"(
                    user_id SERIAL NOT NULL PRIMARY KEY,
                    user_name VARCHAR (255) NOT NULL,
                    email VARCHAR (255) UNIQUE NOT NULL,
                    Admin VARCHAR (100) DEFAULT 'FALSE',
                    user_password VARCHAR (255) NOT NULL  
        )""",
        """ CREATE TABLE IF NOT EXISTS "records"(
                    record_no SERIAL (255) NOT NULL PRIMARY KEY,
                    user_id INTEGER NOT NULL,
                    FOREIGN KEY (user_id) REFERENCES "user_list" (user_id),
                    ON UPDATE CASCADE ON DELETE CASCADE ,
                    record_title VARCHAR(255) NOT NULL,
                    record_geolocation FLOAT NOT NULL,
                    record_type VARCHAR(255) NOT NULL,
                    status VARCHAR(255) NOT NULL DEFAULT 'Under Investigation',
                    record_placement_date TIMESTAMP DEFAULT NOW() NOT NULL
            

        )"""
        try:
            for table in table_creation_commands:
                self.cursor.connection(table)
            self.connection.commit()  # make research
            self.cursor.close()  # closes the connection afeter tables function runs.
        except (Exception, psycopg2.DatabaseError) as error:  #make more research about this
            print(error)
        finally:
            if self.connection is not None:  # eplain some more
                self.connection.close()  # the connection is then closed off after all those commands have been executed

    def create_user(self,user_name,user_password,email):
        new_user="""INSERT INTO user_list(
            user_name, email, user_password
            ) 
            VALUES(
            '{0}','{1}','{2}'
        );""".format(user_name,user_password,email)
        self.cursor.execute(new_user)
        response_object={'message':'successfully signed up',
                        'status':'success'}
        return response_object

    def find_user_by_id(self, user_id):
        """
        adminstrator can request for details about a particular user
        """

        user = "SELECT * FROM user_list WHERE user_id ='{}'".format(user_id)
        self.cursor.execute(user)
        user_returned = self.cursor.fetchone()
        return user_returned

    

    

