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
    def fullname(self):
        return self.ism, self.familiya
class Talaba(Shaxs):
    def __init__(self, ism, familiya, passport, tyil, idraqam, manzil, boosqich = None):
        super().__init__(ism, familiya, passport, tyil)
        self.idraqam = idraqam
        self.bosqich = boosqich
        self.manzil = manzil
    def get_id(self):
        return self.idraqam
    def get_bosqich(self):
        return self.bosqich
    def get_info(self):
        info = f"{self.ism} {self.familiya}."
        info +=f"{self.get_bosqich()}-bosqich. ID raqami: {self.idraqam}"
        return info
        return 

