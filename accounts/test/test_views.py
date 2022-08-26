from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from accounts.models import Account


class UserModelTest(APITestCase):
    @classmethod
    def setUpTestData(cls):

        cls.seller_account = {
            "username": "schneider",
            "password": "1234",
            "first_name": "schneider",
            "last_name": "ratao",
            "is_seller": True,
        }

        cls.seller_account_2 = {
            "username": "schneider2",
            "password": "1234",
            "first_name": "schneider",
            "last_name": "ratao",
            "is_seller": True,
        }

        cls.seller_instance = Account.objects.create_user(**cls.seller_account_2)
        cls.seller_token = Token.objects.get_or_create(user=cls.seller_instance)

        cls.seller_account_2_updated = {
            "username": "schneiderPATCH"
        }

        cls.seller_login_account = {
            "username": "schneider",
            "password": "1234",
        }

        cls.seller_login_account_error = {
            "username": "schneider",
            "password": "12343",
        }

        cls.admin_account = {
            "username": "akirinhaz",
            "first_name": "iasmim",
            "last_name": "dantas",
            "password": "1234",
            "is_superuser": True,
        }

        cls.admin_instance = Account.objects.create_user(**cls.admin_account)
        cls.admin_token = Token.objects.get_or_create(user=cls.admin_instance)

        cls.common_account = {
            "username": "lucira",
            "first_name": "lucira",
            "last_name": "silva",
            "password": "1234",
            "is_seller": False,
        }

        cls.account_deactivated = {
            "username": "tere",
            "first_name": "victor",
            "last_name": "milhoratti",
            "password": "1234",
            "is_seller": False,
            "is_active": False
        }

        cls.account_deactivated_instance = Account.objects.create_user(**cls.account_deactivated)


    def test_can_create_seller(self):
        response = self.client.post(
            "/api/accounts/", self.seller_account, format="json"
        )

        self.assertEqual(response.status_code, 201)
        self.assertEquals(response.data["username"], self.seller_account["username"])
        self.assertEquals(
            response.data["first_name"], self.seller_account["first_name"]
        )
        self.assertEquals(response.data["last_name"], self.seller_account["last_name"])
        self.assertEquals(response.data["is_seller"], self.seller_account["is_seller"])

    def test_can_create_not_seller(self):
        response = self.client.post(
            "/api/accounts/", self.common_account, format="json"
        )

        self.assertEqual(response.status_code, 201)
        self.assertEquals(response.data["username"], self.common_account["username"])
        self.assertEquals(
            response.data["first_name"], self.common_account["first_name"]
        )
        self.assertEquals(response.data["last_name"], self.common_account["last_name"])
        self.assertEquals(response.data["is_seller"], self.common_account["is_seller"])

    def test_login_seller(self):
        response = self.client.post(
            "/api/login/", self.seller_login_account, format="json"
        )

        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.data["token"])

    def test_login_seller(self):
        response = self.client.post(
            "/api/login/", self.seller_login_account_error, format="json"
        )

        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.data, {"detail": "invalid username or password"})

    def test_update_own_account(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.seller_token[0].key)

        response = self.client.patch(
            f"/api/accounts/{self.seller_instance.id}/",
            self.seller_account_2_updated,
            format="json",
            follow=True,
        )

        self.assertEqual(response.status_code, 200)

    def test_activated_account(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.admin_token[0].key)

        response = self.client.patch(
            f"/api/accounts/{self.account_deactivated_instance.id}/",
            {"is_active": True},
            format="json",
            follow=True,
        )

        self.assertEqual(response.status_code, 200)


    def test_deactivated_account(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.admin_token[0].key)

        response = self.client.patch(
            f"/api/accounts/{self.account_deactivated_instance.id}/",
            {"is_active": False},
            format="json",
            follow=True,
        )

        self.assertEqual(response.status_code, 200)


    def test_can_list_all_users(self):
        response = self.client.get("/api/accounts/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 4)
