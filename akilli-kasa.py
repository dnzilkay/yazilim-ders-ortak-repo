from abc import ABC, abstractmethod  # Soyut sınıflar oluşturmak için gerekli modül
from enum import Enum  # Satış türünü belirlemek için

# 🟢 S - Single Responsibility Principle (SRP)
# Her sınıf yalnızca **tek bir sorumluluğa** sahip olmalıdır.

class SaleType(Enum):
    """Ürünün ağırlık ile mi yoksa adet ile mi satılacağını belirten Enum"""
    BY_WEIGHT = "weight"
    BY_QUANTITY = "quantity"

class Product:
    """Ürün bilgilerini temsil eden sınıf"""
    def __init__(self, name: str, price: float, sale_type: SaleType, weight: float = None):
        self.name = name         # Ürünün adı
        self.price = price       # Ürünün fiyatı
        self.sale_type = sale_type  # Ürün ağırlıkla mı, adetle mi satılıyor?
        self.weight = weight if sale_type == SaleType.BY_WEIGHT else None

# 🟢 O - Open/Closed Principle (OCP)
# Yeni ödeme yöntemleri eklenebilir, mevcut kod değiştirilmeden genişletilebilir.

class PaymentMethod(ABC):
    """Ödeme yöntemleri için soyut sınıf"""
    @abstractmethod
    def pay(self, amount: float):
        pass  # Alt sınıflar bu metodu uygulamak zorundadır

class CreditCardPayment(PaymentMethod):
    """Kredi kartı ile ödeme işlemini yöneten sınıf"""
    def pay(self, amount: float):
        print(f"Kredi kartı ile {amount:.2f} TL ödendi.")

class CashPayment(PaymentMethod):
    """Nakit ödeme işlemini yöneten sınıf"""
    def pay(self, amount: float):
        print(f"Nakit olarak {amount:.2f} TL ödendi.")

# 🟢 L - Liskov Substitution Principle (LSP)
# Tüm ödeme yöntemleri PaymentMethod sınıfından türetilmiştir, aynı şekilde kullanılabilir.

class Sale:
    """Satış işlemlerini yöneten sınıf"""
    def __init__(self):
        self.items = []  # Satışa eklenen ürünleri tutan liste

    def add_product(self, product: Product, quantity: float):
        """Satış listesine ürün ekler"""
        self.items.append((product, quantity))

    def calculate_total(self) -> float:
        """Toplam satış tutarını hesaplar"""
        total = 0
        for product, quantity in self.items:
            if product.sale_type == SaleType.BY_WEIGHT:
                total += product.price * quantity  # KG başına fiyat
            else:
                total += product.price * int(quantity)  # Adet başına fiyat
        return total

    def process_payment(self, payment_method: PaymentMethod):
        """Ödeme işlemini gerçekleştirir"""
        total_amount = self.calculate_total()
        payment_method.pay(total_amount)

# 🟢 I - Interface Segregation Principle (ISP)
# Tartılabilir ürünler için ayrı bir arayüz tanımlanmıştır.

class Weighable(ABC):
    """Tartılabilir ürünler için arayüz"""
    @abstractmethod
    def get_weight(self) -> float:
        pass

class WeightedProduct(Product, Weighable):
    """Tartılabilir ürünleri yöneten sınıf"""
    def __init__(self, name: str, price_per_kg: float, weight: float):
        super().__init__(name, price_per_kg, SaleType.BY_WEIGHT, weight)

    def get_weight(self) -> float:
        return self.weight

# 🟢 D - Dependency Inversion Principle (DIP)
# Satış işlemi doğrudan ödeme yöntemlerine bağımlı değildir, soyut bir arayüz kullanır.

# 🛒 Kullanım Örneği
if __name__ == "__main__":
    # Ürünler oluşturuluyor
    apple = Product("Elma", 10, SaleType.BY_WEIGHT)  # Kg başına 10 TL
    milk = Product("Süt", 20, SaleType.BY_QUANTITY)  # 1 kutu süt 20 TL
    bread = Product("Ekmek", 5, SaleType.BY_QUANTITY)  # 1 ekmek 5 TL

    # Satış işlemi başlatılıyor
    sale = Sale()
    sale.add_product(apple, 2)  # 2 kg elma
    sale.add_product(milk, 1)  # 1 kutu süt
    sale.add_product(bread, 3)  # 3 adet ekmek

    print(f"Toplam tutar: {sale.calculate_total()} TL")

    # Ödeme yapılıyor
    payment_method = CreditCardPayment()  # Kredi kartı ile ödeme
    sale.process_payment(payment_method)