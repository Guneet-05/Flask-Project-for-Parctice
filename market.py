from flask import Flask, render_template

app = Flask(__name__)

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
    items = [
        {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
        {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
        {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150}
    ]
    return render_template('market.html',items=items)
    # in items=items, the RHS is the actual list and the LHS is a variable name