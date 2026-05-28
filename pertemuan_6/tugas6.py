# Parent Class
class Kendaraan:
    def __init__(self):
        print("Class Kendaraan")

    def info(self):
        print("Ini adalah kendaraan")


# Child Class dari Kendaraan
class Mobil(Kendaraan):
    def __init__(self):
        super().__init__()
        print("Class Mobil")

    def jalan(self):
        print("Mobil berjalan di jalan raya")


# Child Class dari Kendaraan
class Motor(Kendaraan):
    def __init__(self):
        super().__init__()
        print("Class Motor")

    def jalan(self):
        print("Motor berjalan di jalan kecil")


# Multiple Inheritance
class KendaraanDarat(Mobil, Motor):
    def __init__(self):
        super().__init__()
        print("Class KendaraanDarat")

    def jalan(self):
        super().jalan()
        print("Kendaraan darat sedang berjalan")


# Program Utama
print("=== Diamond Problem Example ===")

kendaraan = KendaraanDarat()

print("\nMethod Resolution Order:")
print(KendaraanDarat.__mro__)

print("\nMenjalankan Method:")
kendaraan.info()
kendaraan.jalan()