from kamar import *
import mysql.connector

conn = mysql.connector.connect(
        host="localhost",        # Ganti dengan host MySQL kamu
        user="root",             # Ganti dengan username MySQL kamu
        password="",             # Ganti dengan password MySQL kamu
        database="tb"            # Ganti dengan nama database kamu
    )
class reservasi(kamar):
    def __init__(self, id_hotel, nama, alamat, telepon, desc, rating, id_kamar, Nomor, tipe, kapasitas, harga,checkin,checkout,jml_orang,jml_hari):
        super().__init__(id_hotel, nama, alamat, telepon, desc, rating, id_kamar, Nomor, tipe, kapasitas, harga)
        self._checkIn = checkin
        self._checkOut = checkout
        self._jml_orang = jml_orang
        self._totalharga = harga *  jml_hari
        
def insertToDb(uid, IdHotel, kamarid, cekin, cekout, jml, status, total):
    cursor = conn.cursor()
    sql = "INSERT INTO Reservasi (Id_User,Id_Hotel,Id_Kamar,CheckIn,CheckOut,Jml_Org,Status,Total_Harga) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
    try:
        print(uid, IdHotel, kamarid, cekin, cekout, jml, status, total)
        cursor.execute(sql, (uid, IdHotel, kamarid, cekin, cekout, jml, status, total))
        conn.commit()  # Penting untuk menyimpan perubahan
        result = cursor.rowcount  # INSERT tidak mengembalikan data untuk di-fetchall
    except Exception as e:
        # Tangani error jika terjadi masalah saat memasukkan data
        conn.rollback()  # Batalkan perubahan jika terjadi error
        result = f"Terjadi kesalahan saat memasukkan data: {e}"
    finally:
        cursor.close()
    print(result)
    return result

# Contoh bagaimana cara memanggil fungsi ini:
# import mysql.connector

# try:
#     conn = mysql.connector.connect(
#         host="your_host",
#         user="your_user",
#         password="your_password",
#         database="your_database"
#     )
#     if conn.is_connected():
#         uid_value = 1
#         hotel_id_value = 101
#         kamar_id_value = 201
#         checkin_date = "2025-05-10"
#         checkout_date = "2025-05-12"
#         jumlah_orang = 2
#         status_value = "Pending"
#         total_harga = 200000

#         insert_result = insertToDb(conn, uid_value, hotel_id_value, kamar_id_value, checkin_date, checkout_date, jumlah_orang, status_value, total_harga)

#         if insert_result is None:
#             print("Data berhasil dimasukkan ke database.")
#         else:
#             print(insert_result)

# except mysql.connector.Error as err:
#     print(f"Error: {err}")
# finally:
#     if 'conn' in locals() and conn.is_connected():
#         conn.close()
def getharga(id,hotelid):
    cursor = conn.cursor()
    sql = "SELECT Harga FROM kamar where Id_Tipe= %s and Id_Hotel = %s"
    cursor.execute(sql,(id,hotelid))
    result = cursor.fetchone()
    cursor.close()
    return result[0]
