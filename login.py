from tkinter import *
from tkinter import messagebox
from confirm import checker 
from PIL import Image, ImageTk, ImageFilter
from tkcalendar import Calendar
from signup import signup
from hotel import getdesc, getname,getalamat,getRating,fasilitass
from datetime import date
import mysql.connector
from user import *
from reservasi import *



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
    pesan_button = Button(frame, text="Pesan Sekarang", command=hotelpage, width=20, height=2)
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
    
def validasi_jumlah_orang(jumlah_entry):
    input_jumlah = jumlah_entry.get().strip()  # Ambil teks dan hapus spasi
    if input_jumlah and input_jumlah != "Jumlah Orang":
        try:
            int(input_jumlah)  # Coba konversi ke integer
            return True  # Jika berhasil, input adalah angka yang valid
        except ValueError:
            return False  # Jika gagal, input bukan angka
    else:
        return False

def tampilkan_error_jumlah_orang(canvas, window):
    # Hapus pesan error sebelumnya jika ada
    if hasattr(window, "error_jumlah_orang"):
        canvas.delete(window.error_jumlah_orang)
    
    # Tampilkan pesan error baru
    window.error_jumlah_orang = canvas.create_text(
        15, 340,  # Posisi di bawah Entry jumlah
        text="Harap masukkan jumlah orang yang valid (angka).",
        fill="red",
        anchor="w",  # Teks dimulai dari kiri
        font=("Microsoft JhengHei UI", 10)
    )

def hapus_error_jumlah_orang(canvas, window):
    if hasattr(window, "error_jumlah_orang"):
        canvas.delete(window.error_jumlah_orang)
        del window.error_jumlah_orang  # Hapus atribut error dari window
    
def proses_form(jumlah_entry,canvas,window):
        """Fungsi contoh untuk memproses form (termasuk validasi jumlah orang)."""
        if validasi_jumlah_orang(jumlah_entry):
            hapus_error_jumlah_orang(canvas, window) #hapus error
            global jmlOrg
            jmlOrg = jumlah_entry.get()
            ConfirmRes(jumlah_entry.get())
        else:
            tampilkan_error_jumlah_orang(canvas, window) #tampilkan error
            print("Input jumlah orang tidak valid.")


def ConfirmRes(jumlah):
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

        background_imgs = Image.open("./assets/uiawal2.png")
        background_img = background_imgs.resize((appwidth, appheight))  # Perhatikan tanda kurung dan penugasan kembali
        cvup = Canvas(w, width=appwidth, height=appheight)
        cvup.pack()
        blurimg = background_img.filter(ImageFilter.GaussianBlur(radius=10))
        blurrtk = ImageTk.PhotoImage(blurimg)
        cvup.create_image(0, 0, anchor=NW, image=blurrtk)

        cvup.create_text(850, 58, text="Sign Up", fill="white", font=("Microsoft JhengHei UI", 18))
        cvup.create_text(850, 550, text="Already have an account?", fill="white", font=("Helvetica", 14))
        useras = getUserdata(uid)
        if not useras:
            print(f"Data pengguna dengan ID {uid} tidak ditemukan.")
        # Menyimpan objek gambar untuk mencegah garbage collection
        cvup.image = blurrtk  # Simpan gambar di dalam canvas untuk mencegah penghapusan
        cvup.create_text(230,70,text=f"Atas Nama\t\t: {useras.getNama()}\nTelp\t\t\t: {useras.getTelp()}\nAlamat\t\t\t: {useras.getAlamat()}\nTanggal Check In\t\t: {tglCheckin()}\nTanggal Check Out\t: {tglCheckOut()}\nTotal Hari\t\t: {jmlHari(str(tglCheckin()),str(tglCheckOut()))}\nHarga permalam\t\t: Rp.{getharga(kamarid,hotelid)}\nTotal Harga\t\t: Rp.{jmlHari(tglCheckin(),tglCheckOut())*getharga(kamarid,hotelid)}",fill="white",font=("Helvfetica", 12,"bold"))
        def canceled():
            insertToDb(uid,hotelid,getIdKamar(kamarid,hotelid),str(tglCheckin()),str(tglCheckOut()),jumlah,"Canceled",getharga(kamarid,hotelid)*jmlHari(str(tglCheckin()),str(tglCheckOut())))
            w.destroy()

        def paid():
            insertToDb(uid,hotelid,getIdKamar(kamarid,hotelid),str(tglCheckin()),str(tglCheckOut()),jumlah,"Paid",getharga(kamarid,hotelid)*jmlHari(str(tglCheckin()),str(tglCheckOut())))
            w.destroy()

        Button(cvup, text="Bayar", font=("Microsoft JhengHei UI", 12), border=0, fg="white", bg="#cc4735", width=20, height=2, command=paid).place(x=400,y=200)
        Button(cvup, text="Batal", font=("Microsoft JhengHei UI", 12), border=0, fg="white", bg="#cc4735", width=20, height=2, command=canceled).place(x=20,y=200)
        w.attributes("-topmost", 1)
        w.mainloop()

def reservasi():
    clear_window()
    print(f"kamarid = {kamarid}")
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
    global tglCheckin
    global tglCheckOut

    def tglCheckin():
        return cekIn.get_date()
    
    def tglCheckOut():
        return CekOut.get_date()


    pesan = Button(window, text="Confirm",borderwidth=2, font=("Microsoft JhengHei UI", 12), border=0, fg="white", bg="#cc4735", width=20, height=2, command=lambda:proses_form(jumlah,canvas,window))
    balikkamar = Button(window, text="Back", font=("Microsoft JhengHei UI", 12), border=0, fg="white", bg="#cc4735", width=20, height=2, command= kamarpage)
    balikkamar.place(x=40,y=350)
    pesan.place(x=400,y=350)
    
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

global kamarid
def kamarpage():
    clear_window()
    print(hotelid)
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
    Button(frame, text="Back", font=("Arial", 12), fg="#01406c", bg="#FF7B07", compound="top", command=hotelpage).grid(row=0, column=0, sticky="wesn",columnspan=1)
    Button(frame, text="Hotel 2", font=("Arial", 12), fg="white", bg="#cc4735", compound="top", command=lambda: print("info")).grid(row=0, column=2, sticky="wesn",columnspan=1)
    kamar_data = [
    {"id": "1", "img": kamar1_img},
    {"id": "2", "img": kamar2_img},
    {"id": "3", "img": kamar3_img},
    {"id": "4", "img": kamar4_img},        
    ]

    for index, kamar in enumerate(kamar_data, start=1):
        name = getname(kamar["id"])
        desc = getdesc(kamar["id"])
        alamat = getalamat(kamar["id"])
        rating = getRating(kamar["id"])
        kamar_img = kamar["img"]
        command = lambda h_id=kamar["id"], idx=index: set_kamar_info(h_id)        
        # Membuat tombol untuk setiap hotel
        hotel_button = Button(frame, text=f"{name}\n{desc}\n{alamat}\n{rating}", 
                            font=("Helvetica Neue", 12, "bold"), fg="white", bg="#01B489", 
                            image=kamar_img, compound="top", command=command)
        hotel_button.grid(row=index, column=0, sticky="wesn", columnspan=3)

    # Update the scrollable region
    frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

    # Enable scrolling with mouse wheel
    def on_mouse_wheel(event):
        canvas.yview_scroll(int(-1*(event.delta/120)), "units")

    canvas.bind_all("<MouseWheel>", on_mouse_wheel)
    def set_kamar_info(kmr_id):
        global kamarid
        kamarid = kmr_id
        reservasi()
    window.title("Kamar Page")



def hotelpage():
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
    {"id": "1", "img": hotel1_img},
    {"id": "2", "img": hotel2_img},
    {"id": "3", "img": hotel3_img},
    {"id": "4", "img": hotel4_img},
    {"id": "5", "img": hotel5_img},
    {"id": "6", "img": hotel6_img},
    # Tambahkan hotel lainnya sesuai kebutuhan
    ]

    # Hotel buttons with images
    global hotelid, index_klik  # Deklarasikan sebagai global di scope ini

    for index, hotel in enumerate(hotel_data, start=1):
        name = getname(hotel["id"])
        desc = getdesc(hotel["id"])
        alamat = getalamat(hotel["id"])
        rating = getRating(hotel["id"])
        fasilitas = fasilitass(hotel["id"])
        hotel_img = hotel["img"]  # Sementara diatur ke None karena penanganan gambar Tkinter perlu ImageTk

        # Membuat command dengan membawa serta hotel_id dan index
        command = lambda h_id=hotel["id"], idx=index: set_hotel_info(h_id, idx)

        # Membuat tombol untuk setiap hotel
        hotel_button = Button(frame, text=f"{name}\n{desc}\nFasilitas : {fasilitas}\n{alamat}\n{rating}",
                                    font=("Helvetica Neue", 12, "bold"), fg="white", bg="#01B489",
                                    image=hotel_img, compound="top", command=command)
        hotel_button.grid(row=index, column=0, sticky="wesn", columnspan=3)

    def set_hotel_info(hotel_id, index):
        global hotelid, index_klik
        hotelid = hotel_id
        index_klik = index
        kamarpage()

    

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

    def getUid(usr):
        conn = mysql.connector.connect(
            host="localhost",        # Ganti dengan host MySQL kamu
            user="root",             # Ganti dengan username MySQL kamu
            password="",             # Ganti dengan password MySQL kamu
            database="tb"            # Ganti dengan nama database kamu
        )
        cursor = conn.cursor()
        cursor.execute(f"select Id_user from user where Username = {usr}")
        result = cursor.fetchone()
        return result[0]

    
    if checker(user, passwd):
        global uid  # Deklarasi global dipindahkan ke awal
        userid = getUid(user)
        if userid is not None:  # Menggunakan 'userid' di sini lebih logis
            uid = userid
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
