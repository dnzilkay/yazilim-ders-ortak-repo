from datetime import datetime, timedelta

def satis_raporu(satislar, zaman_araligi):
    """Belirtilen zaman aralığında satış raporu oluşturur."""
    bugun = datetime.now()
    
    if zaman_araligi == "gunluk":
        baslangic_tarihi = bugun.replace(hour=0, minute=0, second=0, microsecond=0)
    elif zaman_araligi == "haftalik":
        baslangic_tarihi = bugun - timedelta(days=7)
    else:
        return "⚠️ Geçersiz zaman aralığı! Sadece 'gunluk' veya 'haftalik' seçilebilir."

    filtrelenmis_satislar = [s for s in satislar if datetime.fromisoformat(s['tarih']) >= baslangic_tarihi]
    
    toplam_satis = sum(s['tutar'] for s in filtrelenmis_satislar)
    return f"📊 Toplam {zaman_araligi} satış: {toplam_satis} TL"

def stok_raporu(stoklar):
    """Stok raporunu oluşturur, kritik seviyedeki ürünleri listeler."""
    kritik_stok = [urun for urun in stoklar if urun['stok_adedi'] < 5]

    if kritik_stok:
        return "⚠️ Kritik stok seviyesinde olan ürünler:\n" + "\n".join([f"{urun['ad']} - {urun['stok_adedi']} adet" for urun in kritik_stok])
    else:
        return "✅ Tüm ürünlerin stoğu yeterli."

# Kullanıcıdan veri girişi için liste oluştur
satislar = []
stoklar = []

if __name__ == "__main__":
    while True:
        print("\n📌 MENÜ")
        print("1 - Satış Ekle")
        print("2 - Stok Ekle")
        print("3 - Günlük Satış Raporu")
        print("4 - Haftalık Satış Raporu")
        print("5 - Stok Raporu")
        print("6 - Çıkış")
        
        secim = input("Seçiminiz: ").strip()

        if secim == "1":
            tarih = input("📅 Satış tarihi (YYYY-MM-DDTHH:MM:SS): ")
            try:
                datetime.fromisoformat(tarih)  # Format kontrolü
                tutar = float(input("💰 Satış tutarı: "))
                satislar.append({"tarih": tarih, "tutar": tutar})
                print("✅ Satış başarıyla eklendi.")
            except ValueError:
                print("⚠️ Geçersiz tarih veya tutar formatı!")

        elif secim == "2":
            ad = input("📦 Ürün adı: ")
            try:
                stok_adedi = int(input("🔢 Stok adedi: "))
                stoklar.append({"ad": ad, "stok_adedi": stok_adedi})
                print("✅ Stok başarıyla eklendi.")
            except ValueError:
                print("⚠️ Lütfen geçerli bir sayı girin!")

        elif secim == "3":
            print("\n📅 Günlük Satış Raporu:")
            print(satis_raporu(satislar, "gunluk"))

        elif secim == "4":
            print("\n📅 Haftalık Satış Raporu:")
            print(satis_raporu(satislar, "haftalik"))

        elif secim == "5":
            print("\n📦 Stok Raporu:")
            print(stok_raporu(stoklar))

        elif secim == "6":
            print("🚪 Çıkış yapılıyor...")
            break

        else:
            print("⚠️ Geçersiz seçim! Lütfen tekrar deneyin.")
