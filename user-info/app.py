from flask import Flask
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
import os

ENVIRONMENT = os.getenv("ENVIRONMENT", default="DEVELOPMENT")

# see note about different port for local container database re: non-standard port
DB_DNS_NAME = "localhost:6432" if ENVIRONMENT.lower() == "development" else "postgres"
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
def default_route():
    return "ready to serve info about users"


@app.route("/users")
def get_users():
    users = Users.query.all()
    user_list = []
    for user in users:
        user_list.append(
            {"id": user.id, "username": user.username, "email": user.email}
        )
    return user_list


@app.route("/user/<int:user_id>")
def get_user_by_id(user_id):
    user = Users.query.get(user_id)
    if user is None:
        return jsonify({"error": f"no users found with id: {user_id}"})
    return jsonify({"id": user.id, "username": user.username, "email": user.email})


if __name__ == "__main__":
    app.run(host="0.0.0.0")
