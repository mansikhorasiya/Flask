from base import app
from flask import render_template

# category_blueprint = Blueprint('category', __name__, url_prefix='/category')

@app.route('/')
def home():
    # Logic related to the category page
    return render_template("home.html")

@app.route("/load_category")
def load_category():
    return render_template()