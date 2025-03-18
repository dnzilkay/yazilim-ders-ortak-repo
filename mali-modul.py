class MaasTablosu:
    def __init__(self, maaslar):
        self.maaslar = maaslar

    def toplam_maas_gideri(self):
        return sum(self.maaslar)
