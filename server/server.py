import json
from flask import Flask
from flask_restful import Resource, Api
import mysql.connector
import time

from flask import Flask
from flask_graphql import GraphQLView as View
from database import db_session
from graph_ql.schema import schema



app = Flask(__name__)
api = Api(app)

connected = False

db = mysql.connector.MySQLConnection()

while not connected:
    try:
        db = mysql.connector.connect(
            host="nirnroot-db",
            user="admin",
            password="toor",
            port=3306,
            database="nirnroot",
            autocommit=True # without this the api will only update locally and things act funny
        )

        connected = True
    except:
        time.sleep(1)
        print('fail')

cursor = db.cursor()

class Greetings(Resource):
    def get(self):
        return {'hello': 'hello, world'}, 200

api.add_resource(Greetings, '/Greetings')

app.add_url_rule("/graphql", view_func=View.as_view("graphql", graphiql=True, schema=schema))

if __name__ == '__main__':
    app.run(host='0.0.0.0')  # run our Flask app
