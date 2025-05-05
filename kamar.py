from hotel import hotel


class kamar(hotel):
    def __init__(self, id_hotel, nama, alamat, telepon, desc, rating, id_kamar, tipe, harga, kapasitas,status):
        super().__init__(id_hotel, nama, alamat, telepon, desc, rating)
        self._id_kamar = id_kamar
        self._tipe = tipe
        self._harga = harga
        self._kapasitas = kapasitas
        self._status = status

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


hotel1 = kamar(1, "Hotel A", "Jakarta", "021-123456", "Hotel bintang 5", 4.5, 101, "Deluxe", 1000000, 2, True)
hotel2 = kamar(2, "Hotel B", "Bandung", "022-654321", "Hotel bintang 4", 4.0, 102, "Superior", 800000, 3, True)   
hotel3 = kamar(3, "Hotel C", "Bali", "0361-987654", "Hotel bintang 3", 3.5, 103, "Standard", 600000, 2, True)
hotel4 = kamar(4, "Hotel D", "Yogyakarta", "0274-123456", "Hotel bintang 2", 3.0, 104, "Economy", 400000, 1, True)

print(hotel1.getnama())
print(hotel1.gettipe_kamar())
print(hotel1.getharga_kamar())
print(hotel1.getkapasitas_kamar()) 
print(hotel1.getstatus_kamar())