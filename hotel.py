import mysql.connector
from tkinter import *

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
    


class hotel:
    def __init__(self, id_hotel,nama, alamat, telepon, desc,rating):
        self._id_hotel = id_hotel
        self._name = nama
        self._alamat = alamat
        self._telepon = telepon
        self._desc = desc
        self._rating = rating

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

def get_hotel_data(id_hotel):
    # Sambungkan ke database
    conn = mysql.connector.connect(
        host="localhost",        # Ganti dengan host MySQL kamu
        user="root",             # Ganti dengan username MySQL kamu
        password="",             # Ganti dengan password MySQL kamu
        database="tb"            # Ganti dengan nama database kamu
    )
    
    cursor = conn.cursor()
    sql = "SELECT * FROM hotel WHERE id_hotel = %s"
    cursor.execute(sql, (id_hotel,))  # Query untuk mengambil data berdasarkan ID
    result = cursor.fetchone()  # Ambil satu hasil
    conn.close()

    if result:
        return hotel(result[0], result[1], result[2], result[3], result[4], result[5])  # Mengembalikan objek Hotel
    else:
        return None  # Jika tidak ditemukan hotel dengan ID tersebut

