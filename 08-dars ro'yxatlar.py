# cars = ["bmw", "mercedes benz", "volvo", "general motors", "tesla", "audi"]
# cars.sort()                # RO'YXATNI TARTIBLASH
# print (cars)
# cars.sort(reverse=True)    # RO'YXATNI TESKARI TARTIBLASH
# print (cars)
# print(sorted(cars))         # BIR MARTTA TARTIBLASH
# print(sorted(cars, reverse=True))
# sonlar = [12, 45, 23, 56, 998, 1, -5, -7.2]
# print(sorted(sonlar))
# sonlar.sort()
# sonlar.sort(reverse=True)
# 
# 
# cars.reverse()               # RO'YXATNI TESKARISIGA AYLANTIRISH
# 
# print(len(cars))             #RO'YXATNI UZUNLIGINI ANIQLASH
# print(len(sonlar))
# uzunlik=(len(sonlar))
# 
# sonlar= list(range(0,10))     #RO'YXATGA SONLAR KIRITISH
# 
# list(range(21,31))
# 
# sonlar = list(range(1,11))
# toq_sonlar = list(range(1,20,2))
# juft_sonlar= list(range(0,20,2))
# 
# sanash= list(range(0,101,10))
# print(sanash)
# max_qiymat=max(toq_sonlar)
# print(max_qiymat)
# 
# narxlar = [12000, 22500, 23456, 9800, 5600, 9934, 32874]
# 
# arzon= min(narxlar)
# print(min(narxlar))
# 
# qimmat= max(narxlar)
# print(max(narxlar))
# jami = sum(narxlar)
# print(sum(narxlar))
# 
# 
# print(f"eng arzon narx {arzon}, eng qimmat narx {qimmat}. Jami {jami}")
# print(cars[0])
# 
# print(cars[0:3])
# print(cars[2:5])
# print(cars)
# print(cars[:5])
# print(cars[0:])
# 
# my_cars = cars
# print(cars)
# print(my_cars)
# my_cars.remove("volvo")
# print(my_cars)
# my_cars[0]="lacetti"
# print(my_cars)
# print(cars)
# cars.append("audi")
# print(my_cars)


# cars = ["bmw", "mercedes benz", "volvo", "general motors", "tesla", "audi"]
# 
# my_cars= cars[:]             #RO'YXATDAN NUSXA OLISH
# my_cars.remove("bmw")
# 
# print(cars)
# print(my_cars)

      #tuple
# toys=("bus", "car", "bear", "dino", "snake", "lizard")
# print(toys[0])
# print(toys[-1])
# print(toys[2:5])
# toys[3:]
#toys[0]="teddy"
#toys.append("teddy")
#toys.remove("bear")

#toys = list(toys)

#print(type(toys))
# toys.append("teddy")
# print(toys)
# toys=tuple(toys)





            #AMALIYOT
davlatlar=["O'zbekiston", "Qozog'iston", "Turkmaniston", "Tojikiston", "Qirg'iziston", "Turkiya", "Rassiya", "Xitoy", "Amerika"]
print(len(davlatlar))
print(sorted(davlatlar))
print(sorted(davlatlar, reverse=True))
print(davlatlar)
davlatlar.reverse()
print (davlatlar)

davlatlar.sort()
print(davlatlar)
davlatlar.sort(reverse=True)
print(davlatlar)

sonlar=list(range(120,1201,2))
print(sonlar)

print(sum(sonlar))
print(max(sonlar)-min(sonlar))
print(len(sonlar))

print(sonlar[:20])
print(sonlar[260:280])
print(len(sonlar[260:280]))
print(len(sonlar[260:280]))
print(sonlar[521:])
print(len(sonlar[521:]))

taomlar = ["osh", "tuxumli non", "honim", "dimlama", "lavash"]
nonushta= taomlar[:]

nonushta.remove("osh")
nonushta.remove("honim")
nonushta.remove("dimlama")
print(nonushta)
nonushta.append("non va qaymoq")
nonushta.append("issiq non")
print(taomlar)
print(nonushta)
nonushta=tuple(nonushta)

nonushta(0)= "murabbo"     