class Foydalanuvchi:
    def __init__(self, ism, familiya, tyil, adress):
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
        self.adress = adress
    def get_info(self):
        return f"{self.ism} {self.familiya}. Tyil: {self.tyil}."

    def get_adress(self):
        return f"Adress: {self.adress}"

class Admin(Foydalanuvchi):
    def __init__(self,ism,familiya,tyil, adress, parol, nik, idraqam):
        super().__init__(ism,familiya,tyil,adress)
        self.parol = parol
        self.nik = nik
        self.idraqam = idraqam
    def get_nik(self):
        return f" Info : {self}"
    def ban_user(self):
        return f" Foydalanuvchi: {self.ism} {self.familiya} blooklandi. NIki: {self.nik}.  "
talaba1 = Admin("Bahodir", "Abdurahmanov", 2008, "ilyushaparen", "ILyusha", "Ilyusha","A09080")
print(talaba1.get_nik())
print(talaba1.get_info())