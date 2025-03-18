class DepoVeri():
    def __init__(self):
        self.sicak_depo_sicaklik = 0
        self.sicak_depo_nem = 0
        self.sicak_depo_doluluk = 0
        self.soguk_depo_sicaklik = 0
        self.soguk_depo_nem = 0
        self.soguk_depo_doluluk = 0

    def sicakdepo_ısı(self):
        print("Sıcak Depo Verilerini Girin:")
        self.sicak_depo_sicaklik = float(input("Sıcaklık: "))
        self.sicak_depo_nem = float(input("Nem: "))
        #self.sicak_depo_doluluk = float(input("Doluluk Oranı (%): "))
    def sogukdepo_ısı(self):
        print("\nSoğuk Depo Verilerini Girin:")
        self.soguk_depo_sicaklik = float(input("Sıcaklık: "))
        self.soguk_depo_nem = float(input("Nem: "))
        #self.soguk_depo_doluluk = float(input("Doluluk Oranı (%): "))
    def sicakdepo_islem(self):
        print("\nSıcak Depo İşlemleri:")
        print("1- Ürün ekle")
        print("2- Ürün Çıkar")
        secim = int(input("Seçim: "))
        if secim == 1:
            self.sicak_depo_sicaklik = self.sicak_depo_doluluk+int(input("Eklencek ürün miktarı: "))

        elif secim == 2:
            self.sicak_depo_nem = self.sicak_depo_doluluk-int(input("Çıkarılcak ürün miktarı: "))

            pass
        else:
            print("Hatalı Seçim!")

    def sogukdepo_islem(self):
        print("\nSıcak Depo İşlemleri:")
        print("1- Ürün ekle")
        print("2- Ürün Çıkar")
        secim = int(input("Seçim: "))
        if secim == 1:
            self.sicak_depo_sicaklik = self.soguk_depo_doluluk + int(input("Eklencek ürün miktarı: "))

        elif secim == 2:
            self.sicak_depo_nem = self.soguk_depo_doluluk - int(input("Çıkarılcak ürün miktarı: "))

            pass
        else:
            print("Hatalı Seçim!")


    def goster(self):
        print("\nDepo Durumları:")
        print(
            f"Sıcak Depo -> Sıcaklık: {self.sicak_depo_sicaklik}°C, Nem: {self.sicak_depo_nem}%, Doluluk: {self.sicak_depo_doluluk}%")
        print(
            f"Soğuk Depo -> Sıcaklık: {self.soguk_depo_sicaklik}°C, Nem: {self.soguk_depo_nem}%, Doluluk: {self.soguk_depo_doluluk}%")


#