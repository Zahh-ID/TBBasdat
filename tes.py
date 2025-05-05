import mysql.connector
from PIL import Image
import io

# Fungsi untuk mengonversi gambar menjadi format biner
def convert_image_to_binary(image_path):
    with open(image_path, 'rb') as file:
        binary_data = file.read()
    return binary_data

# Fungsi untuk menyimpan gambar ke database
def save_image_to_db(hotel_id, image_path):
    conn = mysql.connector.connect(
        host="localhost",        # Ganti dengan host MySQL kamu
        user="root",             # Ganti dengan username MySQL kamu
        password="",             # Ganti dengan password MySQL kamu
        database="tb"            # Ganti dengan nama database kamu
    )

    cursor = conn.cursor()
    
    # Mengonversi gambar ke format biner
    image_binary = convert_image_to_binary(image_path)
    
    # Menyimpan gambar dalam database
    sql = "UPDATE hotel SET gambar = %s WHERE id_hotel = %s;"
    cursor.execute(sql, (image_binary,hotel_id))
    conn.commit()
    
    print(f"Image for {hotel_id} saved successfully.")
    conn.close()

# Menyimpan gambar-gambar hotel ke database
save_image_to_db("Hotel1", "./assets/hotel/hotel1.jpeg")
save_image_to_db("Hotel2", "./assets/hotel/hotel2.jpeg")
save_image_to_db("Hotel3", "./assets/hotel/hotel3.jpeg")
save_image_to_db("Hotel4", "./assets/hotel/hotel4.jpeg")
save_image_to_db("Hotel5", "./assets/hotel/hotel5.jpeg")
save_image_to_db("Hotel6", "./assets/hotel/hotel6.jpeg")
