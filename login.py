from tkinter import *
from tkinter import messagebox
from confirm import checker 
from PIL import Image, ImageTk, ImageFilter
from tkcalendar import Calendar
from signup import signup
from hotel import getdesc, getname,getalamat,getRating
from datetime import date
import mysql.connector



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
        img = Image.open(path).resize((1080, 700))
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


def Mainpage():
    clear_window()
    frame = Frame(window)
    frame.pack(fill="both", expand=True)

    # Menambahkan label judul
    title_label = Label(frame, text="Selamat Datang di Halaman Utama", font=("Arial", 16))
    title_label.pack(pady=20)

    # Menambahkan tombol "Pesan Sekarang"
    pesan_button = Button(frame, text="Pesan Sekarang", command=show_mainpage, width=20, height=2)
    pesan_button.pack(pady=10)

    # Menambahkan tombol "Logout"
    logout_button = Button(frame, text="Logout", command=window.destroy, width=20, height=2)
    logout_button.pack(pady=10)

def jmlHari(tgl1_str, tgl2_str):
    bulan1, hari1, tahun_pendek1 = map(int, tgl1_str.split('/'))
    tahun1 = 2000 + tahun_pendek1
    tanggal1 = date(tahun1, bulan1, hari1)

    bulan2, hari2, tahun_pendek2 = map(int, tgl2_str.split('/'))
    tahun2 = 2000 + tahun_pendek2
    tanggal2 = date(tahun2, bulan2, hari2)

    selisih = tanggal2 - tanggal1
    return selisih.days  # Mengembalikan hanya jumlah hari


    selisih = tanggal2 - tanggal1
    return selisih
    
def validasiTgl(tanggal_terpilih_str):
    try:
        tanggal_terpilih = date.fromisoformat(tanggal_terpilih_str)
        tanggal_sekarang = date.today()
        if tanggal_terpilih >= tanggal_sekarang:
            return True
        else:
            return False
    except ValueError:
        return False
    
def reservasi():
    clear_window()
    canvas = Canvas(window, width=appwidth, height=appheight)
    canvas.pack()
    p = background_img.filter(ImageFilter.GaussianBlur(radius=10))
    z = ImageTk.PhotoImage(p)
    window.z = z

    canvas.create_image(0, 0, anchor=NW, image=z)

    canvas.create_text(110, 20, text="Reservation Form", fill="white", font=("Microsoft JhengHei UI", 18))
    window.title("CheckIn")
    


    canvas.create_text(80,65,text="Tanggal Check In",fill="white",font=("Helvfetica", 12,"bold"))
    
    cekIn = Calendar(canvas, selectmode='day',
               year=2025, month=5, day=8)  # Tanggal awal
    cekIn.place(x=15, y=80)
    

    canvas.create_text(370,65,text="Tanggal Check Out",fill="white",font=("Helvfetica", 12,"bold"))
    CekOut = Calendar(canvas,selectmode='day',
                      year=2025,month=5,day=8)
    CekOut.place(x=300,y=80)
    def tglCheckin():
        return cekIn.get_date()
    
    def tglCheckOut():
        return CekOut.get_date()


    def ConfirmRes(canvas):
        w = Toplevel()
        appwidth = 700
        appheight = 500

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

        def saveRes(username, password):
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

        background_imgs = Image.open("./assets/uiawal2.png")
        background_img = background_imgs.resize((appwidth, appheight))  # Perhatikan tanda kurung dan penugasan kembali
        cvup = Canvas(w, width=appwidth, height=appheight)
        cvup.pack()
        blurimg = background_img.filter(ImageFilter.GaussianBlur(radius=10))
        blurrtk = ImageTk.PhotoImage(blurimg)
        cvup.create_image(0, 0, anchor=NW, image=blurrtk)

        cvup.create_text(850, 58, text="Sign Up", fill="white", font=("Microsoft JhengHei UI", 18))
        cvup.create_text(850, 550, text="Already have an account?", fill="white", font=("Helvetica", 14))

        # Menyimpan objek gambar untuk mencegah garbage collection
        cvup.image = blurrtk  # Simpan gambar di dalam canvas untuk mencegah penghapusan
        cvup.create_text(180,50,text=f"Tanggal Check In: {tglCheckin()}\nTanggal Check Out: {tglCheckOut()}\nTotal Hari: {jmlHari(str(tglCheckin()),str(tglCheckOut()))}Harga:-",fill="white",font=("Helvfetica", 12,"bold"))
        Button(window, text="Confirm", font=("Microsoft JhengHei UI", 12), border=0, fg="white", bg="#cc4735", width=20, height=2, command=lambda:print(""))
        
        w.attributes("-topmost", 1)
        w.mainloop()


    tombol_ambil = Button(window, text="Confirm", font=("Microsoft JhengHei UI", 12), border=0, fg="white", bg="#cc4735", width=20, height=2, command=lambda:ConfirmRes(canvas))
    tombol_ambil.place(x=90,y=350)

    def focus_inJ(event):
        jumlah.delete(0, END)
        jumlah.config(fg="black")

    def focus_outJ(event):
        if jumlah.get() == "":
            jumlah.insert(0, "Username")
            jumlah.config(fg="#939597")
    canvas.create_text(160,285,text="Jumlah Orang Yang Menampati Kamar",fill="white",font=("Helvfetica", 12,"bold"))
    jumlah = Entry(canvas, width=35, border=0, font=("Microsoft JhengHei UI", 14), borderwidth=0, fg="#939597")
    jumlah.insert(0, "Jumlah Orang")
    jumlah.place(x=15, y=300)
    jumlah.bind("<FocusIn>", focus_inJ)
    jumlah.bind("<FocusOut>", focus_outJ)
    jumlah_line = Frame(window, width=400, height=2, bg="black", border=0).place(x=10, y=330)

          
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
                            image=kamar_img, compound="top", command=reservasi)
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
                            image=kamar_img, compound="top", command=reservasi)
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
    Button(frame, text="Back", font=("Arial", 12), fg="#01406c", bg="#FF7B07", compound="top", command=Mainpage).grid(row=0, column=0, sticky="wesn",columnspan=1)
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
        Mainpage()
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
