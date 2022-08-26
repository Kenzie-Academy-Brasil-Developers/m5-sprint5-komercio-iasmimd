# from rest_framework.authtoken.models import Token
# from rest_framework.test import APITestCase

# from accounts.models import Account
# from products.models import Product


# class ProductViewTest(APITestCase):
#     @classmethod
#     def setUpTestData(cls):
#         cls.seller_account = {
#             "username": "schneider",
#             "first_name": "gabriel",
#             "last_name": "schneider",
#             "password": "1234",
#             "is_seller": True,
#         }

#         cls.seller = Account.objects.create_user(**cls.seller_account)
#         cls.seller_token = Token.objects.get_or_create(user=cls.seller)

#         cls.admin_account = {
#             "username": "akirinhaz",
#             "first_name": "iasmim",
#             "last_name": "dantas",
#             "password": "1234",
#             "is_superuser": True,
#         }

#         cls.admin = Account.objects.create_user(**cls.admin_account)
#         cls.admin_token = Token.objects.get_or_create(user=cls.admin)

#         cls.common_account = {
#             "username": "lucira",
#             "first_name": "lucira",
#             "last_name": "silva",
#             "password": "1234",
#         }

#         cls.common = Account.objects.create_user(**cls.common_account)
#         cls.common_token = Token.objects.get_or_create(user=cls.common)

#         cls.product_data = {
#             "description": "cookie da ias",
#             "price": 100.00,
#             "quantity": 2,
#         }

#         cls.product_instance = Product.objects.create(
#             **cls.product_data, seller=cls.seller
#         )

#         cls.product_updated_data = {"price": "cookie da ias atualizado"}

#         cls.product_data_wrong_keys = {
#             "descripption": "cookie da ias",
#             "priceee": 100.00,
#             "qqqquantity": 2,
#         }

#     def test_product_create_seller_account(self):
#         self.client.credentials(HTTP_AUTHORIZATION="Token " + self.seller_token[0].key)

#         response = self.client.post(
#             "/api/products/", self.product_data, format="json", follow=True
#         )
#         self.assertEqual(response.status_code, 201)

#     def test_product_create_common_account(self):
#         self.client.credentials(HTTP_AUTHORIZATION="Token " + self.common_token[0].key)
#         response = self.client.post(
#             "/api/products/", self.product_data, format="json", follow=True
#         )
#         self.assertEqual(response.status_code, 403)

#     def test_product_create_wrong_keys(self):
#         self.client.credentials(HTTP_AUTHORIZATION="Token " + self.seller_token[0].key)

#         response = self.client.post(
#             "/api/products/", self.product_data_wrong_keys, format="json", follow=True
#         )
#         self.assertEqual(response.status_code, 400)

#     def test_product_update_seller_account(self):
#         self.client.credentials(HTTP_AUTHORIZATION="Token " + self.seller_token[0].key)

#         response = self.client.patch(
#             f"/api/products/{self.product_instance.id}/",
#             self.product_updated_data,
#             format="json",
#             follow=True,
#         )

#         self.assertEqual(response.status_code, 200)

#     def test_product_update_common_account(self):
#         self.client.credentials(HTTP_AUTHORIZATION="Token " + self.common_token[0].key)

#         response = self.client.patch(
#             f"/api/products/{self.product_instance.id}/",
#             self.product_updated_data,
#             format="json",
#             follow=True,
#         )
#         self.assertEqual(response.status_code, 404)

#     def test_product_list(self):
#         response = self.client.get("/api/products/")

#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(
#             response.data["results"][0]["description"], self.product_data["description"]
#         )
#         self.assertEqual(response.data["results"][0]["price"], "100.00")
#         self.assertEqual(
#             response.data["results"][0]["quantity"], self.product_data["quantity"]
#         )
#         self.assertNotEqual(response.data["results"][0]["seller_id"], None)
