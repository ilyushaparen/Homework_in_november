import unittest
from homework_talaba import Shaxs
from homework_talaba import Talaba
class Shaxs_test(unittest.TestCase):

    def setUp(self):
        self.shahs1 = Shaxs("Bahodir", "Abdurahmanov", "AE234235", 1996)

    def test_parametr_shahs(self):
        self.assertIsNotNone(self.shahs1.ism)
        self.assertIsNotNone(self.shahs1.familiya)
        self.assertIsNotNone(self.shahs1.passport)
        self.assertIsNotNone(self.shahs1.tyil)
    def test_metod_shahs(self):
        self.shahs1.get_info()
        self.shahs1.fullname()


class Talaba_test(unittest.TestCase):
    def setUp(self):
        self.shahs2 = Talaba("Hasan","Husan", "AB45292", 2000, 234421, "Urgench")
        self.shahs3 = Talaba("Husan", "Hasan", "AB2314", 1996, idraqam=77800900, manzil="Urgench")
    def test_parametr_Talaba(self):
        self.assertIsNotNone(self.shahs2.ism)
        self.assertIsNotNone(self.shahs2.familiya)
        self.assertIsNotNone(self.shahs2.passport)
        self.assertIsNotNone(self.shahs2.tyil)
        self.assertIsNotNone(self.shahs2.idraqam)
        self.assertIsNotNone(self.shahs2.manzil)
        self.assertIsNone(self.shahs2.get_bosqich())
        self.assertEqual(77800900,self.shahs3.idraqam)
    def test_metod_Talaba(self):
        self.shahs2.get_id()
        self.shahs2.get_bosqich()
        self.shahs2.get_info()


unittest.main

