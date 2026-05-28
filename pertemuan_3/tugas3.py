class karyawan:

    def __init__(self, nama, jabatan, gaji):
        self.nama = nama
        self.jabatan = jabatan
        self.gaji = gaji 

    def tampilkan_info(self):
        return f"Nama: {self.nama}, jabatan: {self.jabatan}, Gaji: Rp{self.gaji}"
    
    def bonus_tahunan(self):
        bonus = self.gaji * 0.1 
        return f"Bonus Tahunan {self.nama}: Rp{bonus}"
    
    @staticmethod
    def perusahaan():
        return "PT Fajar jaya indonesia"
    
karyawan1 = karyawan("Bg jago", "Ceo", 70000000)

karyawan2 = karyawan("keke", "manager", 30000000)

karyawan3 = karyawan("luke", "staff", 20000000)

print(karyawan1.tampilkan_info())
print(karyawan1.bonus_tahunan())

print(karyawan2.tampilkan_info())
print(karyawan2.bonus_tahunan())

print(karyawan3.tampilkan_info())
print(karyawan3.bonus_tahunan())

print(karyawan.perusahaan())

print(karyawan1.perusahaan())
