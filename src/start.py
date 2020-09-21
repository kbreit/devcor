#!/usr/bin/env python

"""
Author: Nick Russo
Purpose: A simple Flask web app that demonstrates the Model View Controller
(MVC) pattern in a meaningful and somewhat realistic way.
"""

import os
from flask import Flask, render_template, request
from database import Database
from sqlalchemy import exc 
from MySQLdb import _exceptions
from flask_wtf.csrf import CSRFProtect

# Create Flask object
app = Flask(__name__)
db = Database("mysql://root:globomantics@db/db", "data/initial.json")
csrf = CSRFProtect(app)

@app.before_request
def before_request():

    try:
        db.connect()
        app.logger.debug("Connected to db")
    except (exc.IntegrityError, _exceptions.IntegrityError):
        pass

@app.after_request
def after_request(response):
    db.disconnect()
    app.logger.debug("Disconnected from db")
    return response

@app.route("/", methods=["GET", "POST"])
def index():
    """
    This is a view function which responds to requests for the top-level
    URL. It serves as the "controller" in MVC as it accesses both the
    model and the view.
    """

    # The button click within the view kicks off a POST request ...
    if request.method == "POST":

        # This collects the user input from the view. The controller's job
        # is to process this information, which includes using methods from
        # the "model" to get the information we need (in this case,
        # the account balance).
        acct_id = request.form["acctid"]
        acct_balance = db.balance(acct_id.upper())
        app.logger.debug(f"balance for {acct_id}: {acct_balance}")

    else:
        # During a normal GET request, no need to perform any calculations
        acct_balance = "N/A"

    # This is the "view", which is the jinja2 templated HTML data that is
    # presented to the user. The user interacts with this webpage and
    # provides information that the controller then processes.
    # The controller passes the account balance into the view so it can
    # be displayed back to the user.
    return render_template("index.html", acct_balance=acct_balance)


if __name__ == "__main__":
    ctx = ("../ssl/cert.pem", "../ssl/key.pem")
    app.secret_key = os.urandom(24)
    app.run(host="0.0.0.0", debug=True, use_reloader=False, ssl_context=ctx) # nosec

