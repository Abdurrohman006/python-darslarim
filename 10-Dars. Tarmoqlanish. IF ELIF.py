############## 10-DARS. TARMOQLANISH ################

avtolar = ["audi", "bmw", "volvo", "kia", "hyundai"]
# for avto in avtolar:
#     print(avto.title())

# for avto in avtolar:
#     if avto=="bmw":
#         print(avto.upper())
#     else:
#         print(avto.title())
#         
# a= 5
# print (a== 5)       # Tengmi ?
# print(a!=6)         # Teng emasmi?
# 
# 
# ism=input("Ismingiz nima?\n>>>")
# if ism.lower() != "ali":
#     print(f"Uzr, {ism.title()} biz Alini kutyapmiz.")
# else:
#     print("Salom, Ali")
    
# javob = float(input("12x6 nechiga teng?>>>"))
# if javob!= 72:
#     print("javob xato!")

# yosh = int(input("Yoshingiz nechida?>>>"))
# if yosh>18:
#     print("Xush kelibsiz!")
# else:
#     print("Kirish mumkin emas!")
#     
#     
# login=input("Yangi login kiriting>>>")
# if len(login)<=5:
#     print("Login 5 ta harfdan koproq bo'lishi shart!")


# yil=int(input("Tug'ilgan yilingizni kiriting:"))
# if 2020-yil<18:
#     print(f"Yoshingiz {2020-yil}da ekan.")
#     print("Kirish mumkin emas!")
# else:
#     print("Hush kelibsiz!")
#     
#     
# yosh = int(input("Yoshingiz nechida!>>>"))
# if yosh>65: print("Siz COVID-19 risk guruhida ekansiz")


# x, y = 25, 50
# print("x>y") if x>y else print("x<y")

####################### AMALIYOT ######################

# cars= ["toyota", "mazda", "hyundai", "gm", "kia"]
# for car in cars:
#     if car=="gm":
#         print(car.upper())
#     else:
#         print(car.title())
#     
#     
# cars= ["toyota", "mazda", "hyundai", "gm", "kia"]
# for car in cars:
#     if car!="gm":
#         print(car.title())
#     else:
#         print(car.upper())

# login = (input("Assalomu aleykum. Login ismingizni kiriting:\n>>>"))
# if login.title()== "Admin":

#     print(f"Xush kelibsiz, {login.title()}. Foydalanuvchilar ro'yxatini ko'rasizmi")
# else:
#     print(f"Xush kelibsiz, {login.title()}")

# x=float(input("Birinchi sonni kiriting!>>>"))
# y=float(input("Ikkinchi sonni kiriting!>>>"))
# if x==y:
#     print("Sonlar teng!")
# else:
#     print("Sonlar teng emas!")



# son=float(input("Istalgan sonni kiriting!>>>"))
# if son<0:
#     print(f"{float(son)} bu manfiy son!")
# else:
#     print(f"{float(son)} bu musbat son!")


son=float(input("Istalgan sonni kiriting biz u sonni ildizini topib beramiz\n>>>"))
if son>0:
    print(f"{son} bu sonning ildizi {son**(1/2)} ga teng!")
else:
    print(f"{son} bu manfiy son, musbat son kiriting!")
