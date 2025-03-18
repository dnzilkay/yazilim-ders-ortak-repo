class DepoVeri():
    def __init__(self):
        self.depo_sicaklik = 0
        self.depo_nem = 0
        self.depo_doluluk = 0

    def depo_ısı(self):
        print("\n Depo Verilerini Girin:")
        self.depo_sicaklik = float(input("Sıcaklık: "))
        self.depo_nem = float(input("Nem: "))
    def depo_islem(self):
        print("\nDepo İşlemleri:")
        print("1- Ürün ekle")
        print("2- Ürün Çıkar")
        secim = int(input("Seçim: "))
        if secim == 1:
            self.depo_doluluk = self.sicak_depo_doluluk+int(input("Eklencek ürün miktarı: "))

        elif secim == 2:
            self.depo_doluluk = self.sicak_depo_doluluk-int(input("Çıkarılcak ürün miktarı: "))

            pass
        else:
            print("Hatalı Seçim!")


    def goster(self):
        print("\nDepo Durumları:")
        print(
            f"Depo -> Sıcaklık: {self.depo_sicaklik}°C, Nem: {self.depo_nem}%, Doluluk: {self.depo_doluluk}%")


#