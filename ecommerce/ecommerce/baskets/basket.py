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

    def _save(self):
        self.session.modified = True

    def __len__(self):
        return sum(item['quantity'] for item in self.basket.values())
