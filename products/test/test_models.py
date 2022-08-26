from django.test import TestCase
from accounts.models import Account
from products.models import Product


class ProductModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.account = {
            'username': 'akirinhaz',
            'first_name':'iasmim',
            'last_name':'dantas',
            'password': '1234',
            'is_seller': True
        }

        cls.seller = Account.objects.create_user(**cls.account)

        cls.product_data = {
            'description': 'cookie da ias',
            'price': 100.00,
            'quantity': 2,
            'seller': cls.seller
        }

        cls.products = Product.objects.create(**cls.product_data)

    def test_product_atributes(self):
        product = Product.objects.get(pk=self.products.id)

        self.assertEquals(product.description, self.product_data["description"])
        self.assertEquals(product.price, self.product_data["price"])
        self.assertEquals(product.quantity, self.product_data["quantity"])
        self.assertEquals(product.seller, self.product_data["seller"])
