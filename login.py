from tkinter import *
from tkinter import messagebox
from confirm import checker  # Assuming this function checks login credentials
from createaccount import createaccount
from PIL import Image, ImageTk, ImageFilter
from signup import signup
from hotel import getdesc, getname,getalamat,getRating


window = Tk()
window.title("BOOKNOW")
appwidth = 1080
appheight = 700
screenwidth = window.winfo_screenwidth()
screenheight = window.winfo_screenheight()
x = (screenwidth/2) - (appwidth/2)
y = 0
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

def load_hotel_images(image_paths):
    for idx, path in enumerate(image_paths, start=1):
        # Membaca dan meresize gambar
        img = Image.open(path).resize((1080, 700))
        # Membuat nama variabel secara dinamis dan menyimpan gambar
        globals()[f"hotel{idx}_img"] = ImageTk.PhotoImage(img)

# Daftar file gambar hotel
image_paths = [
    "./assets/hotel/hotel1.jpeg",
    "./assets/hotel/hotel2.jpeg",
    "./assets/hotel/hotel3.jpeg",
    "./assets/hotel/hotel4.jpeg",
    "./assets/hotel/hotel5.jpeg",
    "./assets/hotel/hotel6.jpeg"
]

# Memuat gambar-gambar hotel dan membuat variabel dinamis
load_hotel_images(image_paths)

kamar1_img = ImageTk.PhotoImage(Image.open("./assets/kamar/hotel1/kamar1.jpeg").resize((1080, 700)))
kamar2_img = ImageTk.PhotoImage(Image.open("./assets/kamar/hotel1/kamar2.jpeg").resize((1080, 700)))
kamar3_img = ImageTk.PhotoImage(Image.open("./assets/kamar/hotel1/kamar3.jpeg").resize((1080, 700)))
kamar4_img = ImageTk.PhotoImage(Image.open("./assets/kamar/hotel1/kamar4.jpeg").resize((1080, 700)))
kamar5_img = ImageTk.PhotoImage(Image.open("./assets/kamar/hotel1/kamar5.jpeg").resize((1080, 700)))
kamar6_img = ImageTk.PhotoImage(Image.open("./assets/kamar/hotel1/kamar6.jpeg").resize((1080, 700)))
def hotel1page():
    clear_window()
    canvas = Canvas(window)
    canvas.pack(side=LEFT, fill=BOTH, expand=True)

    # Create a Scrollbar linked to the Canvas
    scrollbar = Scrollbar(window, orient=VERTICAL, command=canvas.yview)
    scrollbar.pack(side=RIGHT, fill=Y)

    canvas.config(yscrollcommand=scrollbar.set)

    # Create a Frame inside the Canvas that will contain all the buttons
    frame = Frame(canvas)
    canvas.create_window((0, 0), window=frame, anchor="nw")

    # Configure rows and columns for the frame using grid
    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(1, weight=1)
    frame.columnconfigure(2, weight=1)
    frame.rowconfigure(0, weight=2)
    frame.rowconfigure(1, weight=4)
    frame.rowconfigure(2, weight=3)

    # Add buttons with text and images to the frame using grid
    Button(frame, text="Back", font=("Arial", 12), fg="#01406c", bg="#FF7B07", compound="top", command=show_mainpage).grid(row=0, column=0, sticky="wesn",columnspan=1)
    Button(frame, text="Hotel 2", font=("Arial", 12), fg="white", bg="#cc4735", compound="top", command=lambda: print("info")).grid(row=0, column=2, sticky="wesn",columnspan=1)
    kamar_data = [
    {"id": "kamar1", "img": kamar1_img},
    {"id": "kamar2", "img": kamar2_img},
    {"id": "kamar3", "img": kamar3_img},
    {"id": "kamar4", "img": kamar4_img},
    {"id": "kamar5", "img": kamar5_img},
    {"id": "kamar6", "img": kamar6_img},
    # Tambahkan hotel lainnya sesuai kebutuhan
    ]

    # Hotel buttons with images
    for index, kamar in enumerate(kamar_data, start=1):
        name = getname(kamar["id"])
        desc = getdesc(kamar["id"])
        alamat = getalamat(kamar["id"])
        rating = getRating(kamar["id"])
        kamar_img = kamar["img"]
        
        # Membuat tombol untuk setiap hotel
        hotel_button = Button(frame, text=f"{name}\n{desc}\n{alamat}\n{rating}", 
                            font=("Helvetica Neue", 12, "bold"), fg="white", bg="#01B489", 
                            image=kamar_img, compound="top", command=lambda h=kamar["id"]: print(f"{h} selected"))
        hotel_button.grid(row=index, column=0, sticky="wesn", columnspan=3)

    # Update the scrollable region
    frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

    # Enable scrolling with mouse wheel
    def on_mouse_wheel(event):
        canvas.yview_scroll(int(-1*(event.delta/120)), "units")

    canvas.bind_all("<MouseWheel>", on_mouse_wheel)
    #Kamar
    window.title("Main Page")

def hotel2page():
    clear_window()
    canvas = Canvas(window)
    canvas.pack(side=LEFT, fill=BOTH, expand=True)

    # Create a Scrollbar linked to the Canvas
    scrollbar = Scrollbar(window, orient=VERTICAL, command=canvas.yview)
    scrollbar.pack(side=RIGHT, fill=Y)

    canvas.config(yscrollcommand=scrollbar.set)

    # Create a Frame inside the Canvas that will contain all the buttons
    frame = Frame(canvas)
    canvas.create_window((0, 0), window=frame, anchor="nw")

    # Configure rows and columns for the frame using grid
    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(1, weight=1)
    frame.columnconfigure(2, weight=1)
    frame.rowconfigure(0, weight=2)
    frame.rowconfigure(1, weight=4)
    frame.rowconfigure(2, weight=3)

    # Add buttons with text and images to the frame using grid
    Button(frame, text="Back", font=("Arial", 12), fg="#01406c", bg="#FF7B07", compound="top", command=show_mainpage).grid(row=0, column=0, sticky="wesn",columnspan=1)
    Button(frame, text="Hotel 2", font=("Arial", 12), fg="white", bg="#cc4735", compound="top", command=lambda: print("info")).grid(row=0, column=2, sticky="wesn",columnspan=1)
    kamar_data = [
    {"id": "kamar1", "img": kamar1_img},
    {"id": "kamar2", "img": kamar2_img},
    {"id": "kamar3", "img": kamar3_img},
    {"id": "kamar4", "img": kamar4_img},
    {"id": "kamar5", "img": kamar5_img},
    {"id": "kamar6", "img": kamar6_img},
    # Tambahkan hotel lainnya sesuai kebutuhan
    ]

    # Hotel buttons with images
    for index, kamar in enumerate(kamar_data, start=1):
        name = getname(kamar["id"])
        desc = getdesc(kamar["id"])
        alamat = getalamat(kamar["id"])
        rating = getRating(kamar["id"])
        kamar_img = kamar["img"]
        
        # Membuat tombol untuk setiap hotel
        hotel_button = Button(frame, text=f"{name}\n{desc}\n{alamat}\n{rating}", 
                            font=("Helvetica Neue", 12, "bold"), fg="white", bg="#01B489", 
                            image=kamar_img, compound="top", command=lambda h=kamar["id"]: print(f"{h} selected"))
        hotel_button.grid(row=index, column=0, sticky="wesn", columnspan=3)

    # Update the scrollable region
    frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

    # Enable scrolling with mouse wheel
    def on_mouse_wheel(event):
        canvas.yview_scroll(int(-1*(event.delta/120)), "units")

    canvas.bind_all("<MouseWheel>", on_mouse_wheel)
    #Kamar
    window.title("Main Page")




def show_mainpage():
    clear_window()  
    canvas = Canvas(window)
    canvas.pack(side=LEFT, fill=BOTH, expand=True)

    # Create a Scrollbar linked to the Canvas
    scrollbar = Scrollbar(window, orient=VERTICAL, command=canvas.yview)
    scrollbar.pack(side=RIGHT, fill=Y)

    canvas.config(yscrollcommand=scrollbar.set)

    # Create a Frame inside the Canvas that will contain all the buttons
    frame = Frame(canvas)
    canvas.create_window((0, 0), window=frame, anchor="nw")

    # Configure rows and columns for the frame using grid
    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(1, weight=1)
    frame.columnconfigure(2, weight=1)
    frame.rowconfigure(0, weight=2)
    frame.rowconfigure(1, weight=4)
    frame.rowconfigure(2, weight=3)

    # Add buttons with text and images to the frame using grid
    Button(frame, text="Back", font=("Arial", 12), fg="#01406c", bg="#FF7B07", compound="top", command=lambda: print("Back")).grid(row=0, column=0, sticky="wesn",columnspan=1)
    Button(frame, text="Hotel 2", font=("Arial", 12), fg="white", bg="#cc4735", compound="top", command=lambda: print("info")).grid(row=0, column=2, sticky="wesn",columnspan=1)
    hotel_data = [
    {"id": "Hotel1", "img": hotel1_img},
    {"id": "Hotel2", "img": hotel2_img},
    {"id": "Hotel3", "img": hotel3_img},
    {"id": "Hotel4", "img": hotel4_img},
    {"id": "Hotel5", "img": hotel5_img},
    {"id": "Hotel6", "img": hotel6_img},
    # Tambahkan hotel lainnya sesuai kebutuhan
    ]

    # Hotel buttons with images
    for index, hotel in enumerate(hotel_data, start=1):
        name = getname(hotel["id"])
        desc = getdesc(hotel["id"])
        alamat = getalamat(hotel["id"])
        rating = getRating(hotel["id"])
        hotel_img = hotel["img"]
        command = lambda h=hotel["id"]: hotel_page(h)
        # Membuat tombol untuk setiap hotel
        hotel_button = Button(frame, text=f"{name}\n{desc}\n{alamat}\n{rating}", 
                            font=("Helvetica Neue", 12, "bold"), fg="white", bg="#01B489", 
                            image=hotel_img, compound="top", command=hotel1page)
        hotel_button.grid(row=index, column=0, sticky="wesn", columnspan=3)

    # Update the scrollable region
    frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

    # Enable scrolling with mouse wheel
    def on_mouse_wheel(event):
        canvas.yview_scroll(int(-1*(event.delta/120)), "units")

    canvas.bind_all("<MouseWheel>", on_mouse_wheel)
    #Kamar
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
