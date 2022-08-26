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
            "is_seller": True
        }

        cls.seller = Account.objects.create_user(**cls.seller_account)

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


        cls.common_account = {
            "username": "lucira",
            "first_name": "lucira",
            "last_name": "silva",
            "password": "1234",
            "is_seller": False
        }


    def test_can_create_seller(self):
        response = self.client.post('/api/accounts/', self.seller_account, format='json')

        self.assertEqual(response.status_code, 201)
        self.assertEquals(response.data["username"], self.seller_account['username'])
        self.assertEquals(response.data["first_name"], self.seller_account['first_name'])
        self.assertEquals(response.data["last_name"], self.seller_account['last_name'])
        self.assertEquals(response.data["is_seller"], self.seller_account['is_seller'])


    def test_can_create_not_seller(self):
        response = self.client.post('/api/accounts/', self.common_account, format='json')

        self.assertEqual(response.status_code, 201)
        self.assertEquals(response.data["username"], self.common_account['username'])
        self.assertEquals(response.data["first_name"], self.common_account['first_name'])
        self.assertEquals(response.data["last_name"], self.common_account['last_name'])
        self.assertEquals(response.data["is_seller"], self.common_account['is_seller'])


    def test_login_seller(self):
        response = self.client.post('/api/login/', self.seller_login_account, format='json')

        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.data['token'])

    def test_login_seller(self):
        response = self.client.post('/api/login/', self.seller_login_account_error, format='json')

        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.data, {'detail': 'invalid username or password'})


    def test_can_list_all_users(self):
        accounts = Account.objects.all()

        response = self.client.get('/api/accounts/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(accounts), 1)

