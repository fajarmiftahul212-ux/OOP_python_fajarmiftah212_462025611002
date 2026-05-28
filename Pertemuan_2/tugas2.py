class Hewan_Ternak:
    def __init__(self, nama, jenis, umur):
        self.nama = nama
        self.jenis = jenis
        self.umur = umur

    def tampilkan_info(self):
        return f"Nama: {self.nama},  Jenis: {self.jenis}, Umur: {self.umur} tahun"
    
Hewan_ternak1 = Hewan_Ternak("jono", "ayam kampung", 2)
Hewan_ternak2 = Hewan_Ternak("boer", "kambing", 3)
Hewan_ternak3 = Hewan_Ternak("etawa", "sapi", 4)

print(Hewan_ternak1.tampilkan_info())
print(Hewan_ternak2.tampilkan_info())
print(Hewan_ternak3.tampilkan_info())