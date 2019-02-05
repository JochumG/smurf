#https://www.codementor.io/sagaragarwal94/building-a-basic-restful-api-in-python-58k02xsiq
#https://virtualenv.pypa.io/en/latest/installation/

#stappen om een poort open te gooien
#python -m virtualenv venv
#./venv/bin/activate
#pip install flask flask-jsonpify flask-sqlalchemy flask-restful
#pip freeze
#python server.py
#run in background?


from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
#from flask.ext.jsonpify import jsonify


app = Flask(__name__)
app.config['DEBUG'] = True
api = Api(app)

class Deebot(Resource):
    def get(self):
        return '{start}'


        

api.add_resource(Deebot, '/deebot') # Route_1


if __name__ == '__main__':
     app.run(port='80')
     