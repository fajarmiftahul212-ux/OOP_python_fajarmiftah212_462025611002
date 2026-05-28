class DompetDigital:

    def __init__(self, nama, pin, saldo):
        self.__nama = nama
        self.__pin = pin
        self.__saldo = saldo

    def get_nama(self):
        return self.__nama

    def get_saldo(self, pin):
        if pin == self.__pin:
            return f"Saldo Anda: Rp{self.__saldo}"
        else:
            return "PIN salah! Akses ditolak."

    def tarik_uang(self, jumlah, pin):
        if pin == self.__pin:

            if jumlah <= self.__saldo:
                self.__saldo -= jumlah
                return f"Tarik uang berhasil. Sisa saldo: Rp{self.__saldo}"

            else:
                return "Saldo tidak cukup."

        else:
            return "PIN salah! Transaksi gagal."



akun1 = DompetDigital("Fadjar", "1234", 500000)


print(akun1.get_nama())

print("===================")


print(akun1.get_saldo("1234"))

print(akun1.get_saldo("1111"))

print("===================")

print(akun1.tarik_uang(100000, "1234"))

print(akun1.tarik_uang(50000, "0000"))

print("===================")
