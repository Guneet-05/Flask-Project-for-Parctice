from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config is a dictionary 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db' #flask can identify the location of the DB
db = SQLAlchemy(app)

from market import routes

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
