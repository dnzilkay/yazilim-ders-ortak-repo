class StockManager:
    """Stok yönetimini yapan sınıf"""
    def __init__(self):
        self.stock = {}  # Ürünleri ve stok miktarlarını saklar

    def add_stock(self, product_name: str, quantity: float):
        """Belirli bir ürüne stok ekler"""
        if product_name in self.stock:
            self.stock[product_name] += quantity
        else:
            self.stock[product_name] = quantity

    def remove_stock(self, product_name: str, quantity: float):
        """Belirli bir üründen stok düşer"""
        if product_name in self.stock and self.stock[product_name] >= quantity:
            self.stock[product_name] -= quantity
        else:
            print(f"Yetersiz stok: {product_name}")

    def check_stock(self, product_name: str) -> float:
        """Belirtilen ürünün stok miktarını döndürür"""
        return self.stock.get(product_name, 0)

class Supplier:
    """Tedarikçi sınıfı, markete ürün sağlamak için kullanılır"""
    def __init__(self, name: str):
        self.name = name

    def supply_product(self, product_name: str, quantity: float):
        """Ürünü belirli bir miktarda sağlar"""
        print(f"{self.name} tedarikçisi {quantity} birim {product_name} sağladı.")
        return quantity

# 🛒 Kullanım Örneği
if __name__ == "__main__":
    # Stok yönetimi başlatılıyor
    stock_manager = StockManager()
    supplier = Supplier("ABC Gıda")

    # Tedarikçiden ürün alınıyor
    supplied_quantity = supplier.supply_product("Elma", 100)  # 100 kg elma tedarik edildi
    stock_manager.add_stock("Elma", supplied_quantity)

    supplied_quantity = supplier.supply_product("Süt", 50)  # 50 adet süt tedarik edildi
    stock_manager.add_stock("Süt", supplied_quantity)

    # Stok durumunu kontrol etme
    print(f"Elma Stok: {stock_manager.check_stock('Elma')} kg")
    print(f"Süt Stok: {stock_manager.check_stock('Süt')} adet")
