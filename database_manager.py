from datetime import datetime
import sqlite3
from click import password_option
from werkzeug.security import generate_password_hash



conn = sqlite3.connect("data.db")

email = "test@test.test"
balance = 24.8
password = "Renzojegay123"
password_hash = generate_password_hash(password, "MD5")

date_created = f"{datetime.now().day}.{datetime.now().month}.{datetime.now().year}"

password_db_data = conn.cursor().execute(f"DELETE FROM customers WHERE email=?", (email,))
conn.commit()



#conn.cursor().execute("CREATE TABLE customers(id INTEGER PRIMARY KEY AUTOINCREMENT, date_created TEXT, balance REAL, email TEXT, password_hash TEXT)")
# conn.cursor().execute("INSERT INTO customers(date_created, balance, email , password_hash) VALUES(?, ?, ?, ?)", (date_created, balance, email , password_hash,))
# conn.commit()