from tkinter import *
from tkinter import messagebox
from confirm import checker  # Assuming this function checks login credentials
from createaccount import createaccount
from PIL import Image, ImageTk, ImageFilter
from signup import signup


window = Tk()
window.title("BOOKNOW")
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

window.bind;("<Button-1>", eventButton)

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

def clear_window():
    for widget in window.winfo_children():
        widget.destroy()

def show_mainpage():
    clear_window()  
    window.columnconfigure(0, weight=1)
    window.columnconfigure(1, weight=1)
    window.columnconfigure(2, weight=1)
    window.rowconfigure(0, weight=1)
    window.rowconfigure(1, weight=1)
    Hotel1 = Button(window, text="Hotel 1", font=("Arial", 12), fg="white", bg="#cc4735", command=lambda: print("Hotel 1 selected"))
    Hotel1.grid(row=0, column=0,sticky="wesn")
    Hotel2 = Button(window, text="Hotel 2", font=("Arial", 12), fg="white", bg="#cc4735", command=lambda: print("Hotel 2 selected"))
    Hotel2.grid(row=0, column=1,sticky="wesn")
    Hotel3 = Button(window, text="Hotel 3", font=("Arial", 12), fg="white", bg="#cc4735", command=lambda: print("Hotel 3 selected"))
    Hotel3.grid(row=0, column=2,sticky="wesn")
    Hotel4 = Button(window, text="Hotel 4", font=("Arial", 12), fg="white", bg="#cc4735", command=lambda: print("Hotel 4 selected"))
    Hotel4.grid(row=1, column=0,sticky="wesn")
    Hotel5 = Button(window, text="Hotel 5", font=("Arial", 12), fg="white", bg="#cc4735", command=lambda: print("Hotel 5 selected"))
    Hotel5.grid(row=1, column=1,sticky="wesn")
    Hotel6 = Button(window, text="Hotel 6", font=("Arial", 12), fg="white", bg="#cc4735", command=lambda: print("Hotel 6 selected"))
    Hotel6.grid(row=1, column=2,sticky="wesn")

    # Update window title to reflect main page
    window.title("Main Page")
    
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

username = Entry(window, width=35, border=0, font=("Microsoft JhengHei UI", 14), borderwidth=0, fg="#939597",bd=0, highlightthickness=0)
username.insert(0, "Username")
username.place(x=70 ,y=135)
username.bind("<FocusIn>", focus_inU)
username.bind("<FocusOut>", focus_outU)
username_line = Frame(window, width=400, height=2, bg="black", border=0).place(x=65, y=165)

password = Entry(window, width=35, border=0, font=("Microsoft JhengHei UI", 14), borderwidth=0, fg="#939597")
password.insert(0, "Password")
password.place(x=70, y=225)
password.bind("<FocusIn>", focus_inP)
password.bind("<FocusOut>", focus_outP)
password_line = Frame(window, width=400, height=2, bg="black", border=0).place(x=65, y=255)

confirm_button = Button(window, text="Confirm", font=("Microsoft JhengHei UI", 12), border=0, fg="white", bg="#cc4735", width=20, height=2, command=confirm).place(x=160, y=353)
Button(window, text="Sign Up", font=("Didot", 13), border=0, bg="white", fg="#662622", activebackground="white", activeforeground="#ba3a30", command=signup).place(x=220, y=580)
window.mainloop()
