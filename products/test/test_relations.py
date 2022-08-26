# from django.test import TestCase
# from accounts.models import Account
# from products.models import Product


# class ProductRelationTest(TestCase):
#     @classmethod
#     def setUpTestData(cls):
#         cls.account = {
#             'username': 'akirinhaz',
#             'first_name':'iasmim',
#             'last_name':'dantas',
#             'password': '1234',
#             'is_seller': True
#         }

#         cls.seller = Account.objects.create_user(**cls.account)

#         cls.product_data = {
#             'description': 'cookie da ias',
#             'price': 100.00,
#             'quantity': 2,
#             'seller': cls.seller
#         }

#         cls.product = Product.objects.create(**cls.product_data)

#     def test_product_relations(self):
#         self.assertEqual(self.product.seller, self.seller)
