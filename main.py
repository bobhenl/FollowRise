from urllib.parse import urljoin
from flask import Flask, jsonify, render_template, redirect, request, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import timedelta, datetime
import sqlite3

app = Flask(__name__)
app.secret_key = "Ef1fBVB4AeMFBnYV"
app.permanent_session_lifetime = timedelta(days=1)

# GLOBAL VARIABLES#
password_hash_type = "MD5"
admin_passwords = ["..", "Renzojegay123"]



# REQUESTS
@app.route("/signup", methods=["POST", "GET"])
def register():
    if request.method == "POST":

        email = request.form.get("email")
        password = request.form.get("password")


        with sqlite3.connect("data.db") as conn:

            does_exist = conn.cursor().execute("SELECT * FROM customers WHERE email=?",(email,)).fetchall() #
                                                                                                            # Check if E-mail already exist
            if len(does_exist) == 0:                                                                        #

                balance = 0
                password_hash = generate_password_hash(password, password_hash_type)
                date_created = f"{datetime.now().day}.{datetime.now().month}.{datetime.now().year}"

                conn.cursor().execute("INSERT INTO customers(date_created, balance, email , password_hash) VALUES(?, ?, ?, ?)", (date_created, balance, email , password_hash,))
                conn.commit()

                return redirect(url_for("login"))

            else:
                return render_template("signup.html", error_msg="This email is already in use")
    

    else:
        if "user" in session:
            return redirect(url_for("store"))
        else:
            return render_template("signup.html")


# NOTE: Přidat admin login
@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":

        email = request.form.get("email")
        password = request.form.get("password")

        # Admin Login
        if email == "admin" and password == "Renzojegay123":
            session["admin"] = "Admin"
            print("LOGGED AS: ", session["admin"])
            return redirect(url_for("adminpanel"))

        with sqlite3.connect("data.db") as conn:
            db_data = conn.cursor().execute("SELECT password_hash, id FROM customers WHERE email=?", (email,)).fetchall()

            if len(db_data) == 0:
                return render_template("login.html", error_msg="This email is not registered")
            else:
                if check_password_hash(db_data[0][0], password) == True:
                    session["user"] = db_data[0][1]
                    print("LOGGED AS: #", session["user"])
                    return redirect(url_for("store"))
                else:
                    return render_template("login.html", error_msg="Invalid login credentials")
    else:
        if "user"in session:
            return redirect(url_for("store"))
        else:
            return render_template("login.html")





@app.route("/")
def mainpage():
    if "user" in session:
        return redirect(url_for("store"))
    else:
	    return render_template("mainpage.html")

@app.route("/store")
def store():
    if "user" in session:
        return render_template("store.html")
    else:
        return redirect(url_for("login"))

@app.route("/forgot-password")
def forgot_password():
    return render_template("forgot-password.html")

@app.route("/new-password")
def new_password():
    return render_template("new-password.html")

@app.route("/logout")
def logout():
    if "user" in session:
        session.pop("user")
    if "admin" in session:
        session.pop("admin")
    return redirect(url_for("mainpage"))
    

@app.route("/admin")
def adminpanel():
    if "admin" in session:
        return render_template("admin_codePen.html")
    else:
        return redirect(url_for("login"))


# ----- CUSTOMERS ----- #
@app.route("/admin/customers_table")
def adminpanel_customers_table():
    if "admin" in session:
        return render_template("customers_table.html")
    else:
        return redirect(url_for("login"))

@app.route("/admin/customers_data")
def adminpanel_customers_data():
    if "admin" in session:
        with sqlite3.connect("data.db") as conn:
            customers = conn.cursor().execute("SELECT * FROM customers").fetchall()
        return jsonify(customers=customers)
    else:
        return redirect(url_for("login"))


# ----- ORDERS ----- #
@app.route("/admin/orders_table")
def adminpanel_orders_table():
    if "admin" in session:
        return render_template("orders_table.html")
    else:
        return redirect(url_for("login"))



@app.errorhandler(404)
def page_not_found(e):
    return redirect(url_for("mainpage"))

app.run(debug=True, port=8080, host="0.0.0.0")
