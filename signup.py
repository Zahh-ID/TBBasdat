from tkinter import *
from tkinter import messagebox
from confirm import checker  # Assuming this function checks login credentials
from PIL import Image, ImageTk, ImageFilter

import mysql.connector

# Database connection



def signup():
    w = Toplevel()
    appwidth = 1080
    appheight = 700

    def show_message(val):
        w.attributes("-topmost", 0)  # Disable "always on top" for messagebox
        messagebox.showinfo("Info", message=val)
        w.attributes("-topmost", 1)

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
            show_message("Username already exists")
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
                show_message("Signed Up successfully")
            else:
                show_message("Error during sign up")
        except mysql.connector.Error as err:
            show_message(f"Something went wrong: {err}")
        finally:
            cur.close()

    background_img = Image.open("./assets/uiawal2.png") 
    background_tk = ImageTk.PhotoImage(background_img)

    cvup = Canvas(w, width=appwidth, height=appheight)
    cvup.pack()

    cvup.create_image(0, 0, anchor=NW, image=background_tk)
    lefts, uppers, rights, lowers = 600, 100, 1100, 800
    blurarea = background_img.crop((lefts, uppers, rights, lowers))
    blurimg = blurarea.filter(ImageFilter.GaussianBlur(radius=10))
    blurrtk = ImageTk.PhotoImage(blurimg)
    cvup.create_image(600, 0, anchor=NW, image=blurrtk)

    cvup.create_text(850, 58, text="Sign Up", fill="white", font=("Microsoft JhengHei UI", 18))
    cvup.create_text(850, 550, text="Already have an account?", fill="white", font=("Helvetica", 14))

    # Menyimpan objek gambar untuk mencegah garbage collection
    cvup.image = blurrtk  # Simpan gambar di dalam canvas untuk mencegah penghapusan

    # Define Entry widgets for username, password, and confirm password
    username = Entry(w, width=35, border=0, font=("Microsoft JhengHei UI", 14), borderwidth=0, fg="#939597", bd=0, highlightthickness=0)
    username.insert(0, "Username")
    username.place(x=660, y=150)

    password = Entry(w, width=35, border=0, font=("Microsoft JhengHei UI", 14), borderwidth=0, fg="#939597")
    password.insert(0, "Password")
    password.place(x=660, y=230)

    passwordc = Entry(w, width=35, border=0, font=("Microsoft JhengHei UI", 14), borderwidth=0, fg="#939597")
    passwordc.insert(0, "Confirm Password")
    passwordc.place(x=660, y=310)

    # Fungsi fokus untuk Username
    def focus_inU(event):
        username.delete(0, END)
        username.config(fg="black")

    def focus_outU(event):
        if username.get() == "":
            username.insert(0, "Username")
        username.config(fg="#939597")

    # Fungsi fokus untuk Password
    def focus_inP(event):
        password.delete(0, END)
        password.config(fg="black")

    def focus_outP(event):
        if password.get() == "":
            password.insert(0, "Password")
        password.config(fg="#939597")

    # Fungsi fokus untuk Confirm Password
    def focus_inC(event):
        passwordc.delete(0, END)
        passwordc.config(fg="black")

    def focus_outC(event):
        if passwordc.get() == "":
            passwordc.insert(0, "Confirm Password")
        passwordc.config(fg="#939597")

    # Binding focus events
    username.bind("<FocusIn>", focus_inU)
    username.bind("<FocusOut>", focus_outU)
    password.bind("<FocusIn>", focus_inP)
    password.bind("<FocusOut>", focus_outP)
    passwordc.bind("<FocusIn>", focus_inC)
    passwordc.bind("<FocusOut>", focus_outC)

    # Membuat frame untuk garis bawah (input lines)
    Frame(w, width=400, height=2, bg="black", border=0).place(x=655, y=180)
    Frame(w, width=400, height=2, bg="black", border=0).place(x=655, y=260)
    Frame(w, width=400, height=2, bg="black", border=0).place(x=655, y=340)

    def clear_window():
        w.destroy()
    
    def confirm_sign_up():
        user = username.get()
        passwd = password.get()
        cpasswd = passwordc.get()
        if passwd == cpasswd:
            username.delete(0, END)
            password.delete(0, END)
            passwordc.delete(0, END)
            createaccount(user, passwd)
        else:
            show_message("Password and Confirm Password do not match")
            passwordc.delete(0, END)

    # Button untuk membuat akun dan kembali ke login
    Button(w, text="Create Account", font=("Microsoft JhengHei UI", 12), border=0, fg="white", bg="#cc4735", width=20, height=2, command=confirm_sign_up).place(x=750, y=430)
    Button(w, text="Sign In", font=("Didot", 13), border=0, bg="white", fg="#662622", activebackground="white", activeforeground="#ba3a30", command=clear_window).place(x=820, y=580)
    w.attributes("-topmost", 1)
    w.mainloop()
