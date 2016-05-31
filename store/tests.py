from django.test import TestCase

from models import SecretType, SecretStore
from . import get_secret

class StoreTest(TestCase):
    USERNAME = "usernam3"
    PASSWORD = "passw0rd"
    TOKEN = "t0k3n"
    TEST_KEY = "Hello"  

    def setUp(self):
        un_type = SecretType(name="USERNAME")
        pw_type = SecretType(name="PASSWORD")
        t_type = SecretType(name="TOKEN")
        un_type.save()
        pw_type.save()
        t_type.save()
        
        SecretStore(key=self.TEST_KEY, type=un_type, value=self.USERNAME).save()
        SecretStore(key=self.TEST_KEY, type=pw_type, value=self.PASSWORD).save()
        SecretStore(key=self.TEST_KEY, type=t_type, value=self.TOKEN).save()
    
    def test_possitive_cases(self):
        secret = get_secret(self.TEST_KEY)
        self.assertEqual(secret.get_user_name(), self.USERNAME)
        self.assertEqual(secret.get_password(), self.PASSWORD)
        self.assertEqual(secret.get_token(), self.TOKEN)
        self.assertEqual(secret.get("TOKEN"), self.TOKEN)

    def test_negative_cases(self):
        secret = get_secret(self.TEST_KEY)
        self.assertEqual(secret.get("YELLOW"), None)
        secret = get_secret("ORANGE")
        self.assertEqual(secret.get_user_name(), None)
        self.assertEqual(secret.get_password(), None)
        self.assertEqual(secret.get_token(), None)
        self.assertEqual(secret.get("TOKEN"), None)