class SaldoMinimalError(Exception):
    pass

class Bank: 
    def __init__(self, saldo):
        self.saldo = saldo 
    
    def tarik_uang(self, jumlah):
        if jumlah > self.saldo:
            raise SaldoMinimalError(
                "saldo tidak mencukupi"
            )
        self.saldo -= jumlah
        print("Penarikan berhasil")
        print("Sisa saldo:", self.saldo)

nasabah = Bank(100000)

try:
    nasabah.tarik_uang(150000)

except SaldoMinimalError as e:
    print("Error:", e)

finally:
    print("proses pemeriksaan selesai")
        