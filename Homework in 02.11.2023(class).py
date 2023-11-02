class user:
    def __init__(self, name, now_name, email):
        self.name = name
        self.new_name = now_name
        self.mail = email
    def names(self):
        return f"Assolomu Alaykum: {self.name} Hush kelibsiz"
    def new(self):
        return f"Sizning nikingiz {self.new_name}"
    def mails(self):
        return f"Sizning emailingiz {self.mail}"
    def get_info(self):
        return f" Foydalanuvchi: {self.new_name}, ismi: {self.name}, email: {self.mail}"

talaba1 = user("Bahodir Abdurahmanov", "Bahodir7780", "bakhodirabdurakhmano@gmail.com")
talaba2 = user("Artur Fayzullin", "fayzullin3344", "fayzart090@gmail.com")

print(talaba1.names())
print(talaba1.new())
print(talaba1.mails())
print(talaba1.get_info())

print(talaba2.names())
print(talaba2.new())
print(talaba2.mails())
print(talaba2.get_info())