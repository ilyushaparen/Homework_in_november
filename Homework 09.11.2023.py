class Shaxs:
    __tyil = 0
    def __init__(self, ism, familiya, passport, tyil):
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil
        Shaxs.__tyil +=5
    def get_info(self):
        info = f"{self.ism} {self.familiya}."
        info += f"Passport; {self.passport}, {self.tyil} - yilda tug'ilgan "
        return info

    def odamlar_soni(self):
        return self.__tyil
    def __it__(self, yangi_son):
        return self.tyil < yangi_son

class Talaba(Shaxs):
    __shahs = 5
    def __init__(self, ism, familiya, passport, tyil, idraqam, manzil):
        super().__init__(ism, familiya, passport, tyil)
        self.idraqam = idraqam
        self.bosqich = 1
        self.manzil = manzil
        self.tyil = tyil
        Talaba.__shahs += 1
    def talabalar_soni(self, km):
        if self.bosqich >= 5:
            print(f" Odamni soni: {self.bosqich}")
        else:
            self.bosqich += km
            print(f"Odam soni 5 dan kam bomasliki kerak")
    def get_info(self):
        info = f"{self.ism} {self.familiya}."
        info +=f"{self.get_bosqich()}-bosqich. ID raqami: {self.idraqam}"
        return info
    @classmethod
    def talabalar_soni(cls):
        return cls.__shahs
    def __repr__(self):
        info =  f"Foydalanuvchi: {self.ism} {self.familiya}. "
        info += f"\nPassport:{self.passport}. \nID raqam :{self.idraqam}. \nManzil:{self.manzil} "
        return info

talaba1 = Talaba("Bahodir", "Abdurahamnov", " Hozircha yoq", 2008, "Urgench", "Urgench")
talaba2 = Talaba("Artur", "Fayzullin", "Hozircha yoq", 2007, "Urgech", "Urgench")
talaba3 = Shaxs("Bahodir", "Abdurahamnov", " Hozircha yoq", 2008)
talaba4 = Shaxs("Artur", "Fayzullin", "Hozircha yoq", 2007)

print(talaba1.talabalar_soni())
print(talaba1)
