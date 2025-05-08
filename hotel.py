import mysql.connector
from tkinter import *

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="tb"
)

def getdesc(id):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="tb"
    )

    cursor = conn.cursor()
    sql = "SELECT deskripsi FROM hotel WHERE id_hotel = %s"
    cursor.execute(sql, (id,))
    result = cursor.fetchone()
    conn.close()
    
    if result:
        return result[0]
    return "Deskripsi tidak ditemukan"

def getname(id):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="tb"
    )

    cursor = conn.cursor()
    sql = "SELECT nama_hotel FROM hotel WHERE id_hotel = %s"
    cursor.execute(sql, (id,))
    result = cursor.fetchone()
    conn.close()
    
    if result:
        return result[0]
    return "Deskripsi tidak ditemukan"

def getalamat(id):
    conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="tb"
        )
    cursor = conn.cursor()
    sql = "SELECT alamat FROM hotel WHERE id_hotel = %s"
    cursor.execute(sql, (id,))
    result = cursor.fetchone()
    conn.close()
    if result:
        return result[0]
    return "Deskripsi tidak ditemukan"

def getRating(id):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="tb"
    )

    cursor = conn.cursor()
    sql = "SELECT rating FROM hotel WHERE id_hotel = %s"
    cursor.execute(sql, (id,))
    result = cursor.fetchone()
    conn.close()
    if result:
        return result[0]
    return "Deskripsi tidak ditemukan"

def fasilitass(id):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="tb"
    )
    cursor = conn.cursor()
    sql = "CALL GetFasilitasByHotelId(%s)"
    cursor.execute(sql,(id,))
    result = cursor.fetchall()
    conn.close()
    if result:
        fasilitas_list = [row[0] for row in result]  # Ambil hanya nama fasilitas dari setiap tuple
        fasilitas_string = ", ".join(fasilitas_list)
        return fasilitas_string
    return "Deskripsi Tidak ditemukan"
    



class hotel:
    def __init__(self, id_hotel,nama, alamat, desc,fasilitas,rating):
        self._id_hotel = id_hotel
        self._name = nama
        self._alamat = alamat
        self._desc = desc
        self._fasilitas =fasilitas
        self._rating = rating

    def getfasilitas(self):
        return self._fasilitas
    
    def getId(self):
        return self._id_hotel

    def getnama(self):
        return self._name
    
    def getalamat(self):
        return self._alamat
    
    def gettelepon(self):
        return self._telepon
    
    def getdesc(self):
        return self._desc
    
    def getrating(self):
        return self._rating
    
    def getid_hotel(self):
        return self._id_hotel
    
    def setnama(self, nama):
        self._name = nama

    def setalamat(self, alamat):
        self._alamat = alamat

    def settelepon(self, telepon):
        self._telepon = telepon
    
    def setdesc(self, desc):
        self._desc = desc
    
    def setrating(self, rating):
        self._rating = rating

    def setFasilitas(self,fas):
        self._fasilitas = fas

def get_hotel_data(id_hotel):
    cursor = conn.cursor()
    sql = "SELECT * FROM hotel WHERE Id_Hotel = %s"
    cursor.execute(sql, (id_hotel,))  # Query untuk mengambil data berdasarkan ID
    result = cursor.fetchone()  # Ambil satu hasil
    conn.close()

    if result:
        return hotel(result[0], result[1], result[2], result[3], fasilitass(id_hotel), result[4])  # Mengembalikan objek Hotel
    else:
        return None  # Jika tidak ditemukan hotel dengan ID tersebut

