from django.db import models

from ecommerce.common.abstract_models import AuditEntity


class Category(AuditEntity):
    NAME_MAX_LENGTH = 50

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        unique=True,
    )

    slug = models.SlugField(
        unique=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'


class Product(AuditEntity):
    NAME_MAX_LENGTH = 50

    PRICE_MAX_DIGITS = 6
    PRICE_DECIMAL_PLACES = 2

    STOCK_MIN_VALUE = 0

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        unique=True,
    )

    description = models.TextField()

    price = models.DecimalField(
        max_digits=PRICE_MAX_DIGITS,
        decimal_places=PRICE_DECIMAL_PLACES,
    )

    stock = models.PositiveIntegerField()

    slug = models.SlugField(
        unique=True,
    )

    category = models.ForeignKey(
        to=Category,
        on_delete=models.RESTRICT,
    )

    def __str__(self):
        return self.name

    @property
    def in_stock(self):
        return self.stock > self.STOCK_MIN_VALUE

    class Meta:
        ordering = ('-created_on',)


class ProductImage(AuditEntity):
    image = models.ImageField(
        upload_to='product_images/',
        default='product_images/default.png',
    )

    is_main = models.BooleanField(
        default=False,
    )

    product = models.ForeignKey(
        to=Product,
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ('-is_main',)
