class produk:
    
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga

    def __str__(self):
        return f" produk: {self.nama}, Harga: Rp{self.harga}"
    
    def __eq__(self, other):
        return self.harga == other.harga
    
    def __gt__(self, other):
        return self.harga > other.harga

    def __lt__(self, other):
        return self.harga < other.harga 
    
produk1 = produk("laptop", 10000000)
produk2 = produk("hp", 3000000)
produk3 = produk("ipad", 20000000)

print(produk1)
print(produk2)
print(produk3)

print("====================")

print(produk1 == produk3)
print(produk1 > produk2)
print(produk2 < produk1)
        