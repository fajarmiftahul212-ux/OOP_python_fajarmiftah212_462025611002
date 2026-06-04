class AlatPembayaran:
    def proses_bayar(self):
        print("Memproses pembayaran...")

class KartuKredit(AlatPembayaran):
    def proses_bayar(self):
        print("Pembayaran berhasil menggunakan kartu kredit")

class Ewallet(AlatPembayaran):
    def proses_bayar(self):
        print("Pembayaran berhasil menggunakan kartu kredit")

def jalankan_transaksi(objek):
    objek.proses_bayar()

kartu = KartuKredit()
ewallet = Ewallet()

jalankan_transaksi(kartu)
jalankan_transaksi(ewallet)
