import json
data = {"Model" : "Malibu", "Rang" : "Qora", "Yil":2020, "Narh":40000}
data_json = json.dumps(data)
print(data_json)


talaba_json = {"ism":"Hasan",
                 "familiya":"Husanov",
                 "tyil":2000}
ism = talaba_json["ism"]
familiya = talaba_json["familiya"]
print(f"Talaba: \nIsmi: {ism}. \nfamiliyasi: {familiya} ")


talaba = json.dumps(f"{data} {talaba_json}")
print(talaba)