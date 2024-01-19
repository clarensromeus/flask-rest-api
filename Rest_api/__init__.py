from flask import Flask
from Rest_api.Helper.ENV.environment import Configuration
from flask_sqlalchemy import SQLAlchemy


# environment variable configuration
ENV_VAR = Configuration('.env')
DATABASE_USERNAME = ENV_VAR["DATABASE_USERNAME"]
DATABSE_PASSWORD = ENV_VAR["DATABASE_PASSWORD"]
DATABASE_HOST = ENV_VAR["DATABASE_HOST"]
DATABASE_PORT = ENV_VAR["DATABASE_PORT"]
DATABASE_NAME = ENV_VAR["DATABASE_NAME"]

app  = Flask(__name__)
app.config["ENV"] = ENV_VAR["PROJECT_MODE"]
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://root:clarens1998@localhost:3306/REST_API'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = ENV_VAR["DATABASE_TRACK_MODIFICATION"]
db = SQLAlchemy(app)
app.app_context().push()
    

# for the sake of avoiding circular dependency i call the all routes all down the file
from Rest_api.Route import routes
