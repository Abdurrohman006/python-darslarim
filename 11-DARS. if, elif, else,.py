############## 11-DARS. if, elif, else ###############

# son=50
# 
# if son<0:
#     print("Manfiy son")
# else:
#     print("musbat son")


# yosh=int(input("Yoshingiz nechchida!"))

# if yosh<=4:
#     narx = 0
# elif yosh<=12:
#     narx=5000
# elif yosh<=18:
#     narx=8000
# else:
#     narx=10000

# print(f"Sizga kirish {narx} so'm")


# kun= input("Bugun nima kun?>>>")
# if kun.lower()=="shanba" or kun.lower()=="yakshnaba":        # or = yoki
#     print("bugun dam olish kuni")                            # and = va
# else:
#     print("Bugun ish kuni")
    
# kun= input("Bugun nima kun?\n")
# harorat= float(input("Havo harorati qanday\n"))
# if kun.lower()=="yakshanba" or kun.lower()=="shanba" and harorat>=30:
#     print("Cho'milgani ketdik!")
# elif kun.lower()=="yakshanba" or kun.lower()=="shanba" and harorat<30:
#     print("Uyda dam olamiz!")
# else:
#     print("harorat qanaqa bo'lishidan qat'i nazar ishinga bor")


# narx=15000
# choy=True
# salat=False
# if choy and salat:
#     narx= narx+10000
# elif choy or salat:
#     narx= narx+5000
# print(f"Jami narx {narx} so'm")


# narx=15000
# choy=True           # True ni o'rniga 1 qo'ysa bo'ladi
# salat=False         # False ni o'rniga 0 qo'ysa bo'ladi
# non=True
# kompot=True
# assorti=False
# if choy:
#     print("Mijoz choy oldi")
#     narx= narx+3000
# if salat:
#     print("Mijoz salat oldi")
#     narx= narx+5000
# if non:
#     print("Mijoz non oldi")
#     narx= narx+2000
# if kompot:
#     print("Mijoz kompot oldi")
#     narx= narx+5000 
# if assorti:    
#     print("Mijoz assorti oldi")
#     narx= narx+15000
#     
# print(f"jami narx {narx} so'm")

# menu= ["osh", "qozonkabob", "shashlik", "norin", "somsa"]
# "manti" in menu          # menu da manti bormi?
# ovqat=input("Nima ovqat yeysiz?>>>")
# if ovqat.lower() in menu:
#     print("Buyurtma qabul qilindi")
# else:
#     print("Afsuski bizda bunday ovqat yo'q")
    
    
# menu= ["osh", "qozonkabob", "shashlik", "norin", "somsa"]
# buyurtmalar=["osh", "somsa", "manti", "shashlik"]
# 
# if buyurtmalar:                       # royxatda element bolsa bu  ifoda true qaytaradi
#     for taom in buyurtmalar:
#         if taom in menu:
#             print(f"Menuda {taom} bor")
#         else:
#             print(f"Kechirasiz, menuda {taom} yo'q")
# else:                          # agar royxat bosh bolsa
#             print("Savatchangiz bo'sh")
   
   

# if buyurtmalar:
#     print(f"ro'yxatda {len(buyurtmalar)} ta taom bor")
# else:
#     print("Savatchangiz bo'sh")

####################### AMALLAR##################

# son = float(input("Juft son kiriting: "))
# 
# if son%2:
#     print("Bu son juft son emas")
# else:
#     print("Rahmat")


# yosh= int(input("Yoshingiz nechida: "))
# 
# if yosh<=4 or yosh>=60:
#     print("Sizga kirish be'pul")
# elif yosh<18:
#     print("Sizga kirish 10000 so'm")
# else:
#     print("Sizga kirish 20000 so'm")


# x=float(input("Birinchi sonni kiriting: "))
# y=float(input("Ikkinchi sonni kiriting: "))
# if x==y:
#     print(f"{x}={y}")
# elif x>y:
#     print(f"{x}>{y}")
# elif x<y:
#     print(f"{x}<{y}")
    
# mahsulotlar=["coca cola", "non", "sabzi", "tarvuz", "qovun", "tuxum", "qurt", "shokolad", "pepsi", "olma", "uzum"]
# savat=[]
# for n in range(1,6):
#     savat.append(input(f"Savatga {n}-mahsulotni qo'shing: "))
#     
# 
# for mahsulot in savat:
#     if mahsulot.lower() in mahsulotlar:
#         print(f"Do'konimizda {mahsulot.lower()} bor!")
#     else:
#         print(f"Do'konimizda {mahsulot.lower()} yo'q!")



# mahsulotlar=["coca cola", "non", "sabzi", "tarvuz", "qovun", "tuxum", "qurt", "shokolad", "pepsi", "olma", "uzum"]
# savat=[]
# for n in range(1,6):
#     savat.append(input(f"{n}-mahsulotni kiriting: ").lower())
# bor_mahsulot=[]
# yoq_mahsulot=[]
# for mahsulot in savat:
#     if mahsulot.lower() in mahsulotlar:
#         bor_mahsulot.append(mahsulot)
#     else:
#         yoq_mahsulot.append(mahsulot)
# if len(bor_mahsulot)==5:
#     print("Siz so'ragan barcha mahsulotlar bor")
# for n in yoq_mahsulot:
#     print(f"Bizda {n} yo'q")
    
# foydalanuvchilar = ["sobir", "bobur", "nodir", "qodir", "komil"]
# login = input("Login kiriting: ").lower()
# if login in foydalanuvchilar:
#     print("Bu login band, boshqa login tanlang")
# else:
#     print(f"Xush kelibsiz, {login.title()}")
        


son = int(input("Istalgan butun son kiriting: "))
for x in range(2, 11):
    if not(son%x):
        print(f"{son} soni {x} ga qoldiqsiz bo'linadi.")
    