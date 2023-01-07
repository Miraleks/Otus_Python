from os import getenv

from flask import Flask, render_template, redirect, flash, logging
from flask import jsonify
from flask import request

from flask_wtf import CSRFProtect
from flask_migrate import Migrate
from sqlalchemy.exc import DatabaseError

from models import db

from views.products import products_app

app = Flask(__name__)

CONFIG_OBJECT = getenv("CONFIG", "ProductionConfig")
app.config.from_object(f"config.{CONFIG_OBJECT}")


app.register_blueprint(products_app, url_prefix="/products")

CSRFProtect(app)
# db.app = app
db.init_app(app)
migrate = Migrate(app=app, db=db, compare_type=True)
# migrate = Migrate(app=app, db=db)


@app.cli.command("db-create-all")
def db_create_all():
    db.create_all()


def print_request():
    print("request:", request)
    print("headers:", request.headers)


@app.get("/", endpoint="index_page")
def get_root():
    return render_template("index.html")


@app.route("/hello/<name>/")
@app.route("/hello/")
def hello_world(name: str = None):
    if not name:
        name = request.args.get("name", "world")  # вторым идет дефолтное значение
    return f"<h2> Hello {name}!!!</h2>"


@app.get("/items/")
def get_items():
    return {
        "items": [
            {"id": 1},
            {"id": 2},
        ],
    }


@app.get("/item_none/")
def get_items_none():
    return jsonify(None)


# конвертер аннотация: int
# /items/123qwe    Error!!!
@app.get("/items/<int:item_id>")
def get_item(item_id: int):
    return {"item": {"id": item_id}}


@app.get("/items/<item_id>")
def get_item_as_string(item_id: str):
    return {"item_id": {"id_str": item_id.upper()}}


@app.errorhandler(DatabaseError)
def handle_database_error(error):
    flash("oops! no db connection!", "danger")
    return redirect("/")
