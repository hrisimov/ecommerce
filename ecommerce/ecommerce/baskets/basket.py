from copy import deepcopy
from decimal import Decimal

from ecommerce.products.models import Product


class Basket:
    def __init__(self, request):
        self.session = request.session
        self.basket = self.session['basket'] = self.session.get('basket', {})

    def add(self, product, quantity):
        pk = str(product.pk)
        self.basket[pk] = self.basket.get(pk, {})
        self.basket[pk]['quantity'] = self.basket[pk].get('quantity', 0)
        self.basket[pk]['quantity'] += quantity
        self._save()

    def update(self, product, new_quantity):
        pk = str(product.pk)
        self.basket[pk]['quantity'] = new_quantity
        self._save()

    def delete(self, product):
        pk = str(product.pk)
        del self.basket[pk]
        self._save()

    def calculate_subtotal_price(self):
        """
        Available after visiting basket summary since subtotal price is needed for first time there.
        """
        return sum(item['quantity'] * Decimal(item['price']) for item in self.basket.values())

    def is_empty(self):
        return len(self.basket) == 0

    def _save(self):
        self.session.modified = True

    def __iter__(self):
        product_pks = self.basket.keys()
        products = Product.objects.filter(pk__in=product_pks).prefetch_related('productimage_set')
        basket = deepcopy(self.basket)

        for product in products:
            pk = str(product.pk)
            basket[pk]['product'] = product
            basket[pk]['quantity'] = self.basket[pk]['quantity'] = min(self.basket[pk]['quantity'], product.stock)
            self.basket[pk]['price'] = str(product.price)

        for item in basket.values():
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.basket.values())
