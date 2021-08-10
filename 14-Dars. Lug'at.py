################# 14-Dars. Lug'at (Dictionary) ####################

car_0 = {"model":"ferrari","rang":"qizil"}
# print(car_0["model"])
# print(car_0["rang"])
# en_uz = {"apple":"olma","apricot":"o'rik", "banana":"banan"}
# print(en_uz)
# 
# print(en_uz["apple"])

# mevalar={"olma":10000, "tarvuz": 8000, "qovun": 10000}
# print(f"Olma narhi {mevalar['olma']} so'm")
# 
# talaba_0 = {"ism":"murod olimov", "yosh":20, "t_yil":2000}
# print(f'{talaba_0["ism"].title()},\
#   {talaba_0["t_yil"]}-yilda tug\'ilgan,\
#   {talaba_0["yosh"]} yoshda')
# 
# talaba_0["kurs"] = 4
# talaba_0["fakultet"] = "informatika"
# talaba_0["ism"] = "abdulloh"
# print(talaba_0)

talaba_1 = {}
talaba_1["ism"]= "qobil rasulov"
talaba_1["kurs"]= 3
talaba_1["yosh"]= 20

# print(talaba_1)
# print(f"Talaba {talaba_1['ism'].title()} {talaba_1['kurs']}-kurs")

# talaba_1["kurs"]=4
# print(f"Talaba {talaba_1['ism'].title()} {talaba_1['kurs']}-kurs")
# 
# talaba_0 = {"ism":"murod olimov", "yosh":20, "t_yil":2000}
# 
# del talaba_0["yosh"]
# print(talaba_0)
# 
# telefonlar = {
#     "ali" : "iphone x",
#     "vali" : "galaxy s9",
#     "olim" : "mi 10 pro",
#     "orif" : "nokia 3310"
#     }
# phone = telefonlar.get("hasan", "Bunday ism mavjud emas")  # get metodi:'hasan' kalit soz bolsa chiqaradi, yoki 2 chisini
# print(phone)

# phone = telefonlar.get("hasan")



################### AMALLAR ####################

# akam={"ism":"abduvali", "yil":"2000", "shahri":"Toshkent shahri"}
# print (f'Akamning ismi {akam["ism"].title()}, {akam["yil"]}-yilda, {akam["shahri"]}da tug\'ilganlar')



# taomlar= {"mustafo":"qozon kabob", "muhammadzohid":"manti", "muhammadsolih":"somsa", "umar":"shashlik", "sobir":"osh"}
# print (
#     f'Mustafoning sevimli taomi {taomlar["mustafo"]},\
#     \nMuhammadzohidning sevimli taomi {taomlar["muhammadzohid"]}\
#     \nMuhammadsolihning sevmli taomi {taomlar["muhammadsolih"]}\
# ')



python_lugat = {
    "integer":"Butun son",
    "float": "O'nlik son",
    "string": "Matn",
    "if": "Agar",
    "else":"Aks holda",
    "for":"Uchun",
    "true":"Rost",
    "false":"Yolg'on",
    "list":"Ro'yxat",
    "tuple":"O'zgarmas ro'yxat"}


x = input("Kalit so'z kiriting:")
tarjima=python_lugat.get(x,"none")


if tarjima=="none":
    print("Bunday so'z mavjud emas")
else:
    print(f'{x} so\'zi "{python_lugat[x]}" deb tarjima qilinadi')
