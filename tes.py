from tkinter import *
from PIL import Image, ImageTk

# Membuat window Tkinter
window = Tk()
window.title("Gambar dengan Ukuran Sama")
window.geometry("800x600")  # Ukuran window sesuai kebutuhan

# Ukuran gambar yang diinginkan
desired_width = 300  # Lebar yang diinginkan
desired_height = 200  # Tinggi yang diinginkan

# Daftar gambar yang ingin ditampilkan (ganti dengan path gambar Anda)
image_paths = [
    "./assets/s.png",  # Ganti dengan path gambar yang sesuai
    "./assets/screen.png",  # Ganti dengan path gambar yang sesuai
    "./assets/uiawal2.png",  # Ganti dengan path gambar yang sesuai
    # Tambahkan gambar lainnya
]

# Membuat canvas untuk menampilkan gambar
canvas = Canvas(window, width=800, height=600)
canvas.pack()

# Menampilkan gambar-gambar dengan ukuran yang sama
x_position = 0  # Posisi x untuk gambar pertama
y_position = 0  # Posisi y untuk gambar pertama

for image_path in image_paths:
    img = Image.open(image_path)  # Membuka gambar
    img_resized = img.resize((desired_width, desired_height))  # Mengubah ukuran gambar
    img_tk = ImageTk.PhotoImage(img_resized)  # Mengonversi gambar untuk Tkinter
    
    # Menampilkan gambar pada canvas
    canvas.create_image(x_position, y_position, anchor=NW, image=img_tk)
    
    # Menyimpan gambar agar tidak hilang
    canvas.image = img_tk  # Menyimpan gambar di dalam canvas untuk mencegah penghapusan

    # Memperbarui posisi untuk gambar berikutnya
    y_position += desired_height + 10  # Menambah jarak antar gambar (10 piksel)

# Menjalankan aplikasi Tkinter
window.mainloop()
