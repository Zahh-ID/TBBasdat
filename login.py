from tkinter import *
from tkinter import messagebox
from confirm import checker  # Assuming this function checks login credentials
from createaccount import createaccount
from PIL import Image, ImageTk, ImageFilter

window = Tk()
appwidth = 1080
appheight = 700
screenwidth = window.winfo_screenwidth()
screenheight = window.winfo_screenheight()
x = (screenwidth/2) - (appwidth/2)
y = (screenheight/2) - (appheight/2)
window.geometry(f'{appwidth}x{appheight}+{int(x)}+{int(y)}')
window.resizable(False, False)
def eventButton(event):
    print(event)
window.bind("<Button-1>", eventButton)
def reset():
    pass

background_img = Image.open("./assets/uiawal2.png") 
background_tk = ImageTk.PhotoImage(background_img)

img_width, img_height = background_img.size
canvas = Canvas(window, width=appwidth, height=appheight)
canvas.pack()

canvas.create_image(0, 0, anchor=NW, image=background_tk)
left, upper, right, lower = 100, 100, 600, 900
blur_area = background_img.crop((left, upper, right, lower))
blurred_img = blur_area.filter(ImageFilter.GaussianBlur(radius=10))
blurred_tk = ImageTk.PhotoImage(blurred_img)

canvas.create_image(0, 0, anchor=NW, image=blurred_tk)

canvas.create_text(260, 58, text="Sign In", fill="white", font=("Microsoft JhengHei UI", 18))
canvas.create_text(260,550,text="Not an existing user?",fill="white", font=("Helvetica", 14))

def confirm():
    user = username.get()
    passwd = password.get()
    username.delete(0, END)
    password.delete(0, END)
    
    if checker(user, passwd): 
        show_mainpage()  
    else:
        messagebox.showinfo("Sign In", message="Invalid username or password")

def clear_window():
    for widget in window.winfo_children():
        widget.destroy()

def focus_inU(event):
    username.delete(0, END)
    username.config(fg="black")

def focus_outU(event):
    if username.get() == "":
        username.insert(0, "Username")
    username.config(fg="#939597")

def focus_inP(event):
    password.delete(0, END)
    password.config(fg="black")

def focus_outP(event):
    if password.get() == "":
       password.insert(0, "PASSWORD")
    password.config(fg="#939597")

username = Entry(window, width=35, border=0, font=("consolas", 14), borderwidth=0, fg="#939597",bd=0, highlightthickness=0)
username.insert(0, "Username")
username.place(x=80 ,y=135)
username.bind("<FocusIn>", focus_inU)
username.bind("<FocusOut>", focus_outU)
username_line = Frame(window, width=380, height=2, bg="black", border=0).place(x=65, y=165)

password = Entry(window, width=35, border=0, font=("consolas", 14), borderwidth=0, fg="#939597")
password.insert(0, "Password")
password.place(x=80, y=235)
password.bind("<FocusIn>", focus_inP)
password.bind("<FocusOut>", focus_outP)
password_line = Frame(window, width=380, height=2, bg="black", border=0).place(x=65, y=265)

def loginpage():
    background_img = Image.open("./assets/uiawal2.png") 
    background_tk = ImageTk.PhotoImage(background_img)

    img_width, img_height = background_img.size
    canvas = Canvas(window, width=appwidth, height=appheight)
    canvas.pack()

    canvas.create_image(0, 0, anchor=NW, image=background_tk)
    left, upper, right, lower = 100, 100, 600, 900
    blur_area = background_img.crop((left, upper, right, lower))
    blurred_img = blur_area.filter(ImageFilter.GaussianBlur(radius=10))
    blurred_tk = ImageTk.PhotoImage(blurred_img)

    canvas.create_image(0, 0, anchor=NW, image=blurred_tk)

    canvas.create_text(260, 58, text="Sign In", fill="white", font=("Microsoft JhengHei UI", 18))
    canvas.create_text(260,550,text="Not an existing user?",fill="white", font=("Helvetica", 14))

def signup():
    clear_window()
    canvas.destroy()
    
    cvup = Canvas(window, width=appwidth, height=appheight)
    cvup.pack()
    cvup.create_image(0, 0, anchor=NW, image=background_tk)
    lefts, uppers, rights, lowers = 120, 150, 450, 350
    blurarea = background_img.crop((lefts, uppers, rights, lowers))
    blurimg = blurarea.filter(ImageFilter.GaussianBlur(radius=10))
    blurrtk = ImageTk.PhotoImage(blurimg)
    cvup.create_image(0, 0, anchor=NW, image=blurrtk)
    cvup.create_text(800, 58, text="Sign Up", fill="white", font=("Microsoft JhengHei UI", 18))
    cvup.create_text(800,550,text="Already have an account?",fill="white", font=("Helvetica", 14))

    username2 = Entry(window, width=35, border=0, font=("consolas", 14), borderwidth=0, fg="#939597")
    username2.insert(0, "Username")
    username2.place(x=640, y=185)
    
    password2 = Entry(window, width=35, border=0, font=("consolas", 14), borderwidth=0, fg="#939597")
    password2.insert(0, "Password")
    password2.place(x=640, y=335)

    passwordc = Entry(window, width=35, border=0, font=("consolas", 14), borderwidth=0, fg="#939597")
    passwordc.insert(0, "Confirm Password")
    passwordc.place(x=640, y=435)

confirm_button = Button(window, text="Confirm", font=("Microsoft JhengHei UI", 12), border=0, fg="white", bg="#cc4735", width=20, height=2, command=confirm).place(x=160, y=353)
signup = Button(window, text="Sign Up", font=("Didot", 13), border=0, bg="white", fg="#662622", activebackground="white", activeforeground="#ba3a30", command=signup).place(x=220, y=580)
window.mainloop()
