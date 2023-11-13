class Shaxs:
    def __init__(self, ism, familiya, passport, tyil):
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil
    def get_info(self):
        info = f"{self.ism} {self.familiya}."
        info += f"Passport; {self.passport}, {self.tyil} - yilda tug'ilgan "
        return info
    def get_age(self,yil):
        return yil - self.tyil
    def __gt__(self, other):
        return self.tyil < other

class Talaba(Shaxs):
    def __init__(self, ism, familiya, passport, tyil, idraqam, manzil):
        super().__init__(ism, familiya, passport, tyil)
        self.idraqam = idraqam
        self.bosqich = 1
        self.manzil = manzil
    def get_id(self):
        return self.idraqam
    def get_bosqich(self):
        return self.bosqich
    def get_info(self):
        info = f"{self.ism} {self.familiya}."
        info +=f"{self.get_bosqich()}-bosqich. ID raqami: {self.idraqam}"
        return info
    def __eq__(self, talaba):
        return self.idraqam == talaba

talaba1 = Shaxs("Bahodir", "Abdurahmanov", "AE33443", 2008)
talaba2 = Shaxs("Bahodir", "Abdurahmanov", "AE33443", 2010)
talaba3 = Talaba("Bahodir", "Abdurahmanov", "AB23462", 2009, 123521, "Urgench")
talaba4 = Talaba("Bahodir", "Abdurahmanov", "AB23462", 2009, 15452352, "Urgench")
print(talaba3 == talaba4)
print(talaba1 > talaba2)
