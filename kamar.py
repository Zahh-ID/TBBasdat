from hotel import hotel
import mysql.connector

class kamar(hotel):
    def __init__(self, id_hotel, nama, alamat, telepon, desc, rating, id_kamar,Nomor, tipe, kapasitas, harga):
        super().__init__(id_hotel, nama, alamat, telepon, desc, rating)
        self._id_kamar = id_kamar
        self._Nomor = Nomor
        self._tipe = tipe
        self._kapasitas = kapasitas
        self._harga = harga
        

    def getid_kamar(self):
        return self._id_kamar
    
    def gettipe_kamar(self):
        return self._tipe
    
    def getharga_kamar(self):
        return self._harga
    
    def getkapasitas_kamar(self):
        return self._kapasitas
    
    def getstatus_kamar(self):
        return self._status
    
    def setid_kamar(self, id_kamar):
        self._id_kamar = id_kamar
    
    def settipe_kamar(self, tipe):
        self._tipe = tipe

    def setharga_kamar(self, harga):
        self._harga = harga
    
    def setkapasitas_kamar(self, kapasitas):
        self._kapasitas = kapasitas
    
    def setstatus_kamar(self, status):
        self._status = status

def getKamardata(id):
    # Sambungkan ke database
    conn = mysql.connector.connect(
        host="localhost",        # Ganti dengan host MySQL kamu
        user="root",             # Ganti dengan username MySQL kamu
        password="",             # Ganti dengan password MySQL kamu
        database="tb"            # Ganti dengan nama database kamu
    )
    
    cursor = conn.cursor()
    sql = "SELECT * FROM kamar WHERE Id_Kamar = %s"
    cursor.execute(sql, (id,))  # Query untuk mengambil data berdasarkan ID
    result = cursor.fetchone()  # Ambil satu hasil
    conn.close()
    
    if result:
        print(result)
        return kamar(result[0], result[1], result[2], result[3], result[4], result[5])  # Mengembalikan objek Hotel
    else:
        return None
    
import mysql.connector

def getIdKamar(tipe, idHotel):
    conn = None
    cursor = None
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="tb"
        )
        cursor = conn.cursor()
        sql = "SELECT Id_Kamar FROM kamar WHERE Id_Tipe = %s AND Id_Hotel = %s"
        cursor.execute(sql, (tipe, idHotel))
        result = cursor.fetchone()
        if result:
            return result[0]
        else:
            return None  # Mengembalikan None jika kamar tidak ditemukan
    except mysql.connector.Error as err:
        print(f"Error saat mengambil ID Kamar: {err}")
        return None  # Mengembalikan None jika terjadi error database
    finally:
        if cursor:
            cursor.close()
        if conn and conn.is_connected():
            conn.close()

# Contoh Penggunaan:
# id_kamar = getIdKamar("Superior", "HTL001")
# if id_kamar:
#     print(f"ID Kamar yang ditemukan: {id_kamar}")
# else:
#     print("Kamar tidak ditemukan atau terjadi kesalahan.")