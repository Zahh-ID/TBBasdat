import tkinter as tk
from tkinter import ttk,Frame

def validasi_jumlah_orang(jumlah_entry):
    """
    Fungsi untuk memvalidasi input jumlah orang.

    Args:
        jumlah_entry (tk.Entry): Entry widget yang berisi input jumlah orang.

    Returns:
        bool: True jika input valid (angka dan bukan hanya spasi), False jika tidak valid.
    """
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
    """
    Menampilkan pesan error di canvas.

    Args:
        canvas (tk.Canvas): Canvas untuk menampilkan pesan error.
        window (tk.Tk): Jendela utama Tkinter.
    """
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
    """
    Menghapus pesan error dari canvas.

    Args:
        canvas (tk.Canvas): Canvas yang berisi pesan error.
        window (tk.Tk): Jendela utama Tkinter.
    """
    if hasattr(window, "error_jumlah_orang"):
        canvas.delete(window.error_jumlah_orang)
        del window.error_jumlah_orang  # Hapus atribut error dari window

def focus_inJ(e):
    """Fungsi untuk menangani event focus in pada Entry jumlah."""
    if jumlah.get() == "Jumlah Orang":
        jumlah.delete(0, "end")
        jumlah.config(fg="black")  # Ubah warna teks saat mulai mengetik

def focus_outJ(e):
    """Fungsi untuk menangani event focus out pada Entry jumlah."""
    if not jumlah.get().strip():
        jumlah.insert(0, "Jumlah Orang")
        jumlah.config(fg="#939597")  # Kembalikan warna teks placeholder

def buat_entry_jumlah(canvas, window):
    """
    Membuat Entry untuk input jumlah orang dan elemen terkait.

    Args:
        canvas (tk.Canvas): Canvas untuk menempatkan elemen-elemen.
        window (tk.Tk): Jendela utama Tkinter.
    """
    global jumlah  # Membuat variabel jumlah menjadi global agar dapat diakses di fungsi lain
    
    canvas.create_text(160, 285, text="Jumlah Orang Yang Menampati Kamar", fill="white", font=("Helvfetica", 12, "bold"))
    jumlah = ttk.Entry(canvas, width=35, font=("Microsoft JhengHei UI", 14)) #hilangkan border
    jumlah.insert(0, "Jumlah Orang")
    jumlah.place(x=15, y=300)
    jumlah.bind("<FocusIn>", focus_inJ)
    jumlah.bind("<FocusOut>", focus_outJ)
    jumlah_line = Frame(window, width=400, height=2, bg="black", border=0).place(x=10, y=330)

    return jumlah  # Kembalikan objek Entry

if __name__ == '__main__':
    window = tk.Tk()
    window.geometry("600x400")  # Contoh ukuran window
    canvas = tk.Canvas(window, width=600, height=400, bg="lightblue")  # Contoh warna latar
    canvas.pack()

    jumlah_entry = buat_entry_jumlah(canvas, window) #buat entry jumlah

    def proses_form():
        """Fungsi contoh untuk memproses form (termasuk validasi jumlah orang)."""
        if validasi_jumlah_orang(jumlah_entry):
            print("Jumlah Orang:", jumlah_entry.get())  # Lakukan sesuatu dengan input yang valid
            hapus_error_jumlah_orang(canvas, window) #hapus error
            # Lanjutkan dengan pengolahan data lainnya...
        else:
            tampilkan_error_jumlah_orang(canvas, window) #tampilkan error
            print("Input jumlah orang tidak valid.")

    # Tambahkan tombol untuk memicu pemrosesan form
    tombol_proses = ttk.Button(window, text="Proses", command=proses_form)
    tombol_proses.pack(pady=10)

    window.mainloop()
