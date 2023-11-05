class Avto:
    def __init__(self, model, rang, korobka, narh):
        self.model = model
        self.rang = rang
        self.korobka = korobka
        self.narh = narh
        self.kilometer = 0
    def get_model(self):
        return self.model
    def get_rang(self):
        return self.rang
    def get_korobka(self):
        return self.korobka
    def get_narhi(self):
        return self.narh
    def get_kilometres(self):
        return self.kilometer
    def get_info(self):
        return f"Avtoning modeli: {self.model}. \nRangi: {self.rang}. \nKorobka: {self.korobka}. \nNarh: {self.narh}$. \nKilometer: {self.kilometer} "
    def up_kilometer(self,new_km):
        self.kilometer = new_km

car1 = Avto("M9", "Qora", "Mexanika", 10000)
car1.up_kilometer(500)
print(car1.get_info())

car2 = Avto("R-34", "Qizil", "Paket", 500000)
car2.up_kilometer(0)
print(car2.get_info())