# route/view - functions routing to a specific route
# if we deploy the web app, DEBUG_MODE should be set to 0 i.e. off
# otherwise the customers will be able to see the errors

from market import app
from flask import render_template
from market.models import Item

@app.route("/")
@app.route("/home")
def home_page():
    return render_template('home.html')

# # Dynamic Routes
# @app.route("/about/<username>")
# def about_page(username):
#     return f"<h1>About Page {username}</h1>"

@app.route('/market')
def market_page():
    items = Item.query.all()
    return render_template('market.html',items=items)
    # in items=items, the RHS is the actual list and the LHS is a variable name
