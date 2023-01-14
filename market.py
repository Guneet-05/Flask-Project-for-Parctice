from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config is a dictionary 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db' #flask can identify the location of the DB
db = SQLAlchemy(app)

# The class that will be converted to the tables in the database is called a model
# We have used the SQLAlchemy 
class Item(db.Model):
    id = db.Column(db.Integer(),primary_key=True)
    name = db.Column(db.String(length=30),nullable=False,unique=True) # creating an instance of column class and assigning it to the variable name
    # limiting the characters to 30 

    price = db.Column(db.Integer(),nullable=False)
    barcode = db.Column(db.String(length=12),nullable = False,unique=True)
    description = db.Column(db.String(length=1024),nullable=False,unique=True)

    def __repr__(self) -> str:
        return f"Item {self.name}"


# route/view - functions routing to a specific route
# if we deploy the web app, DEBUG_MODE should be set to 0 i.e. off
# otherwise the customers will be able to see the errors
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

# What we do in command line for DB
# from market import app,db
# >>> app.app_context().push()
# >>> db.create_all()
# >>> from market import Item
# item1 = Item(name = "Iphone 10", 
# price=500,barcode='129828330912',
# description='Latest iphone 10 piece. 
# Very good quality. Extremey powerful for prodcutive use and great camera as well')
# db.session.add(item1)
# >>> db.session.commit()
# >>> Item.query.all()
# [<Item 1>]

# This name <Item 1> can be changed by us by overriding the __repr__ method
