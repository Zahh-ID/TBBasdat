from tkinter import *
from hotelpage import *
def clear_window(window):
    for widget in window.winfo_children():
        widget.destroy()

def Mainpage(window):
    clear_window(window)
    frame = Frame(window)
    frame.pack(fill="both", expand=True)

    # Menambahkan label judul
    title_label = Label(frame, text="Selamat Datang di Halaman Utama", font=("Arial", 16))
    title_label.pack(pady=20)

    # Menambahkan tombol "Pesan Sekarang"
    pesan_button = Button(frame, text="Pesan Sekarang", command=hotelPage, width=20, height=2)
    pesan_button.pack(pady=10)

    # Menambahkan tombol "Logout"
    logout_button = Button(frame, text="Logout", command=window.destroy, width=20, height=2)
    logout_button.pack(pady=10)