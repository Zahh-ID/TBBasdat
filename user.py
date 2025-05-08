import mysql.connector

class user:
    def __init__(self, Id_User, Username, Password, Nama, Telp, Alamat):
        self._Id_User = Id_User
        self._Username = Username
        self._Password = Password
        self._Nama = Nama
        self._Telp = Telp
        self._Alamat = Alamat

    def getUser(self):
        return self._Username
    
    def getNama(self):
        return self._Nama

    def getUid(self):
        return self._Id_User

    def getTelp(self):
        return self._Telp

    def getAlamat(self):
        return self._Alamat

    def setUser(self, Username):
        self._Username = Username

    def setPassword(self, Password):
        self._Password = Password

    def setNama(self, Nama):
        self._Nama = Nama

    def setTelp(self, Telp):
        self._Telp = Telp

    def setAlamat(self, Alamat):
        self._Alamat = Alamat
    

def getUserdata(id):
    # Sambungkan ke database
    conn = mysql.connector.connect(
        host="localhost",        # Ganti dengan host MySQL kamu
        user="root",             # Ganti dengan username MySQL kamu
        password="",             # Ganti dengan password MySQL kamu
        database="tb"            # Ganti dengan nama database kamu
    )
    
    cursor = conn.cursor()
    sql = "SELECT * FROM user WHERE Id_User = %s"
    cursor.execute(sql, (id,))  # Query untuk mengambil data berdasarkan ID
    result = cursor.fetchone()  # Ambil satu hasil
    conn.close()
    
    if result:
        print(result)
        return user(result[0], result[1], result[2], result[3], result[4], result[5])  # Mengembalikan objek Hotel
    else:
        return None