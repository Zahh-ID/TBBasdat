import mysql.connector
from hotel import hotel

def load_hotels_from_db():
    hotels = []
    conn = None
    cursor = None
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="tb"  # Ganti dengan nama database Anda
        )
        cursor = conn.cursor()
        sql = "SELECT * FROM hotel"
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            hotel_obj = hotel(row[0], row[1], row[2], row[3], row[4],8)
            hotels.append(hotel_obj)
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if cursor:
            cursor.close()
        if conn and conn.is_connected():
            conn.close()
    return hotels

def load_hotel_facilities_from_db(hotel_id):
    facilities = []
    conn = None
    cursor = None
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="tb"  # Ganti dengan nama database Anda
        )
        cursor = conn.cursor()
        sql = "SELECT Nama_Fasilitas FROM fasilitas WHERE Id_Hotel = %s"
        cursor.execute(sql, (hotel_id,))
        results = cursor.fetchall()
        for row in results:
            facilities.append(row[0])
    except mysql.connector.Error as err:
        print(f"Error loading facilities: {err}")
    finally:
        if cursor:
            cursor.close()
        if conn and conn.is_connected():
            conn.close()
    return facilities

# Contoh Penggunaan:
list_of_hotels = load_hotels_from_db()

if list_of_hotels:
    for hotel in list_of_hotels:
        hotel.fasilitas = load_hotel_facilities_from_db(hotel.getId())
        print(f"ID: {hotel.getId()}, Nama: {hotel.getnama()}, Rating: {hotel.getrating()}, Fasilitas: {hotel.fasilitas}")

    # Sekarang Anda dapat menggunakan list_of_hotels yang berisi objek-objek Hotel
    # yang datanya dimuat dari tabel database
    # Misalnya, Anda bisa menggunakannya untuk membuat tombol-tombol UI:
    # for index, hotel_obj in enumerate(list_of_hotels, start=1):
    #     # ... kode pembuatan tombol menggunakan atribut hotel_obj ...