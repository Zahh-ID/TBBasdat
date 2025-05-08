from kamar import kamar
from datetime import datetime, timedelta

class Booking(kamar):
    def __init__(self, id_hotel, nama, alamat, telepon, desc, rating, id_kamar, tipe, harga, kapasitas,status):
        super().__init__(id_hotel, nama, alamat, telepon, desc, rating, id_kamar, tipe, harga, kapasitas,status)
        self._check_in = None
        self._check_out = None
        self._total_harga = 0

    def set_check_in(self, check_in):
        self._check_in = check_in

    def set_check_out(self, check_out):
        self._check_out = check_out

    def booking(self):
        if self._check_in and self._check_out:
            check_in_date = datetime.strptime(self._check_in, "%Y-%m-%d")
            check_out_date = datetime.strptime(self._check_out, "%Y-%m-%d")
            duration = (check_out_date - check_in_date).days
            if duration > 0:
                self._total_harga = duration * self.getharga_kamar()
                return True
            else:
                return False
        return False
    
    def cancel_booking(self):
        self._check_in = None
        self._check_out = None
        self._total_harga = 0
        
    

kmr1 = Booking(1, "Hotel A", "Jakarta", "021-123456", "Hotel bintang 5", 4.5, 101, "Deluxe", 1000000, 2, True)
kmr1.set_check_in("2023-10-01")
kmr1.set_check_out("2023-10-05")
if kmr1.booking():
    print(f"Booking successful! Total price: {kmr1._total_harga}")