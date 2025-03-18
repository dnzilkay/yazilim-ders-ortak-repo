class Personel:
    def __init__(self, id, ad, soyad, pozisyon, maas):
        self.id = id
        self.ad = ad
        self.soyad = soyad
        self.pozisyon = pozisyon
        self.maas = maas
        self.izinler = []  # İzinler için bir liste
        self.reyon_gorevleri = []  # Reyon görevlendirmeleri için bir liste

    def izin_ekle(self, tarih, sebep):
        self.izinler.append({'tarih': tarih, 'sebep': sebep})

    def reyon_gorevlendirme(self, reyon):
        self.reyon_gorevleri.append(reyon)

    def maas_guncelle(self, yeni_maas):
        self.maas = yeni_maas

    def __str__(self):
        return f"{self.ad} {self.soyad} - {self.pozisyon} - Maaş: {self.maas}"


class MüşteriDestekReyon:
    def __init__(self, id, ad):
        self.id = id
        self.ad = ad
        self.gorevli_personel = []

    def gorevli_personel_ekle(self, personel):
        self.gorevli_personel.append(personel)

    def gorevli_personel_listele(self):
        for p in self.gorevli_personel:
            print(p)


class MaaşTablosu:
    def __init__(self):
        self.maas_tablosu = {}

    def maas_ekle(self, personel, yeni_maas):
        self.maas_tablosu[personel.id] = yeni_maas

    def maas_listele(self):
        for id, maas in self.maas_tablosu.items():
            print(f"Personel ID: {id} - Maaş: {maas}")


# Kullanıcı Verileri Örneği
personel1 = Personel(1, "Ali", "Yılmaz", "Müşteri Destek", 5000)
personel2 = Personel(2, "Ayşe", "Kaya", "Reyon Görevlisi", 4000)

# İzin eklemek
personel1.izin_ekle("2025-03-20", "Yıllık izin")

# Reyon görevlendirme
reyon1 = MüşteriDestekReyon(1, "Müşteri Destek")
reyon1.gorevli_personel_ekle(personel1)
reyon1.gorevli_personel_ekle(personel2)

# Maaş güncelleme
personel2.maas_guncelle(4500)

# Maas Tablosu
maas_tablosu = MaaşTablosu()
maas_tablosu.maas_ekle(personel1, personel1.maas)
maas_tablosu.maas_ekle(personel2, personel2.maas)

# Çıktılar
print("Reyon 1 Görevli Personeller:")
reyon1.gorevli_personel_listele()

print("\nMaaş Tablosu:")
maas_tablosu.maas_listele()
