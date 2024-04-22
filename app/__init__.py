import os
from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)

# Load configuration from environment variables
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
    "DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/ascend"
)
app.config["TOKEN_SECRET_KEY"] = os.getenv(
    "TOKEN_SECRET_KEY", "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"
)

# Initialize SQLAlchemy and Flask-Migrate
db = SQLAlchemy(app)
migrate = Migrate(app, db)
