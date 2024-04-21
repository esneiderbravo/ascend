import os

from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
CORS(app)
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "postgresql://postgres:postgres@localhost:5432/ascend"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

TOKEN_SECRET_KEY = os.getenv("TOKEN_SECRET_KEY")
