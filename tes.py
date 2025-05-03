from tkinter import *
from PIL import Image, ImageTk

# Membuat window Tkinter
window = Tk()
window.title("Entry Transparan dengan Gambar Latar Belakang")
window.geometry("800x600")  # Sesuaikan ukuran jendela

# Membuka gambar latar belakang
background_img = Image.open("./assets/uiawal2.png")  # Ganti dengan path gambar Anda
background_tk = ImageTk.PhotoImage(background_img)

# Membuat canvas untuk menggambar gambar latar belakang
canvas = Canvas(window, width=800, height=600)
canvas.pack()

# Menampilkan gambar latar belakang di canvas
canvas.create_image(0, 0, anchor=NW, image=background_tk)

# Membuat Entry untuk username
username = Entry(window, width=35, font=("consolas", 14), fg="#939597", bd=0, highlightthickness=0)
username.insert(0, "USERNAME")
username.config(bg="white")  # Membuat latar belakang transparan (di atas canvas)

# Menambahkan Entry ke dalam window
username.place(x=80, y=136)

# Membuat garis bawah untuk Entry (Frame)
username_line = Frame(window, width=380, height=2, bg="black")
username_line.place(x=65, y=165)

# Menjalankan aplikasi Tkinter
window.mainloop()
