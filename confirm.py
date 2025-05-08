import mysql.connector

# Database connection
con = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='tb'
)

def checker(username, password):
    cur = con.cursor()
    
    # Query untuk mencari username dan password yang cocok
    sql = "SELECT * FROM user WHERE username = %s AND password = %s"
    data = (username, password)
    
    try:
        cur.execute(sql, data)
        user = cur.fetchone()  # Ambil satu hasil yang cocok (username dan password)
        
        if user:
            # Jika username dan password ditemukan, login berhasil
            return True
        else:
            # Jika tidak ditemukan, login gagal
            return False
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return False  # Jika ada error pada query, anggap login gagal
    finally:
        cur.close()
