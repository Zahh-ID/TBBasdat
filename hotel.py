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


