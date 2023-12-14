from flask_app import app
from flask import redirect, render_template,request
from ..models.maker import FilmMaker

@app.route('/')
def index():
    return render_template("maker.html")