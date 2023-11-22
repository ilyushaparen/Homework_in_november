import unittest
from homework import max_sonlar
from homework import text_list


class test(unittest.TestCase):
    def son1(self):
        son = max_sonlar(25, 50, 100)
        self.assertEqual(son, 100)

    def kichhi(self):
        katta = text_list("bahodir")
        self.assertEqual(katta, "Bahodir")


unittest.main()