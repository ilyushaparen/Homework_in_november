import re
matn = "Mening ismim Bahodir. Yoshim 15 da. Veb manxilim: https://github.com/ilyushaparen.com Bu githunb manzil."
tekshiruvchi = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*|\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
tekshirish = re.findall(tekshiruvchi,matn)
print(tekshirish)


with open("web_manzil.txt", 'w+') as file:
    for address in tekshirish:
        file.write(address)