from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

ENVIRONMENT = os.getenv("ENVIRONMENT", default="DEVELOPMENT")

DB_DNS_NAME = "localhost" if ENVIRONMENT.lower() == "development" else "postgres"
DATABASE_NAME = "users"

DB_USERNAME = os.getenv("DB_USERNAME", default="postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", default="password")

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = (
    f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_DNS_NAME}/{DATABASE_NAME}"
)

db = SQLAlchemy(app)


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)


@app.route("/")
def connected_to_database():
    return "connected to the database"


@app.route("/users")
def log_count():
    users = Users.query.all()
    user_list = []
    for user in users:
        user_list.append(
            {"id": user.id, "username": user.username, "email": user.email}
        )
    return user_list


if __name__ == "__main__":
    app.run(host="0.0.0.0")
