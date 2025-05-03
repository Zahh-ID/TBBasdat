from tkinter import *
from tkinter import messagebox
import mysql.connector

# Database connection
con = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='tb'
)

def createaccount(username, password):
    cur = con.cursor()

    # Check if the username already exists
    sql2 = "SELECT * FROM users WHERE username = %s"
    data2 = (username,)
    cur.execute(sql2, data2)
    existing_user = cur.fetchone()

    if existing_user:
        messagebox.showinfo("Sign Up", message="Username already exists")
        return  # Prevent further execution

    # Insert new account into the database
    try:
        sql = "INSERT INTO users (username, password) VALUES (%s, %s)"
        data = (username, password)
        cur.execute(sql, data)
        con.commit()

        # Verify if the account was created
        cur.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
        new_user = cur.fetchone()

        if new_user:
            messagebox.showinfo("Sign Up", message="Signed Up successfully")
        else:
            messagebox.showinfo("Sign Up", message="Error during sign up")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Something went wrong: {err}")
    finally:
        cur.close()

