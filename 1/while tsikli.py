# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 22:41:16 2022

@author: Sardar king
"""

#ism=input("Ismingiz nima?")
#print(f'Salom, {ism.title()} ')
#ism=input('Ismingiz nima?>>>')
#savol=f'Salom, {ism.title()}. Yoshingiz nechida?'
#yosh=input(savol)
#yosh=int(yosh)
#height=input("Boyingiz necha metr?")
#height=float(height)
#son=1
#while son<=5:
 #   print(son, end='')
  #  son=son+1
#print("Kiritilgan sonning kvadratini qaytauvchi dastur.")
#savol="Istalgan son kiiting " 
#savol+="(dasturni to\'xtatish ochun 'exet' dep yozing):"
#qiymat=''
#while qiymat !='exit':
 #   qiymat=input(savol)
  #  if qiymat != 'exit':
   #     print(float(qiymat)**2)
#son=input("son yozing")
#daraja=input('bu birinchi sonning darajasi')
#son=int(son)
#daraja=int(daraja)
#while son !='exit':
    
    
 #       print(son**daraja)
#print("Kiritilgan sonning kvadratini qaytauvchi dastur .")
#savol="Istalgan son kiiting\n"
#savol+="(dasturni to\'xtatish uchun 'exit' deb yozing \n)"
#ishora=True
#while ishora:
 #   qiymat=input(savol)
  #  if qiymat =='exit':
   #    ishora=False
   # else:
    #    print(float(qiymat)**2)
#while True:
#    qiymat = input(savol)
#    if qiymat == 'exit':
##        break
#    else:
 #       print(float(qiymat)**2)

#sonlar=list(range(1,11))
#for son in sonlar:
 #   if son == 10:
  #      continue
   # print(f'{son}ning kvadrati {son**2} ga teng')
    
#son=0
#while son<10:
 #   son+=1
  #  if son%2!=0:
   #     continue
   # else:
    #    print(son)
#son =0
#while son<10:
 #   if son%2!=0:
  #      continue
   # else:
    #    print(son)
#savol=("Sevimli kitobingizni yozing   :")
#savol+='(dasturni tugatish uchun exet deb yozing  :)'
#while True:
 #   kitob=input(savol)
  #  if kitob=='exit':
   #     break
   # print('Raxmat')
#savol='How old are you:'

#while True:
#    qiymat=input(savol)
#    if qiymat =='exit' or qiymat=='quit':
#        break
#    yosh=int(qiymat)
#    
#    if yosh<7:
#        price=2
#    elif 7<=yosh<18:
#        price=3
#    elif 18<=yosh<65:
#        price=10
#    elif 65<=yosh<1000:
#         price=0
    
#    if price==0:
#        print("You can come free  ")
#    else:
#        print(f'Your ticket {price} dollar ')
        
#savol='kiritilgan sonning ildizini qaytaruvchi dastur.\n'
#savol+='Musbat son kiriting '
#savol+='Dasturni toztatish uchun exit deb yozing. \n>>>>'

#while True:
 #   qiymat=input(savol)
#    if qiymat =='exit':
#        break
#    elif float(qiymat)<0:
#        continue
#    else:
#        ildiz=float(qiymat)**(0.5)
#        print(f'{qiymat} ning ildizi {ildiz} ga teng')
#ismlar=[]
#print("yaqin do\'stingiz ismini kiriting :")
#n=1
#while True:
#    savol=f'{n}-do\'stingizning ismini kiriting:'
#    ism=input(savol)
#    ismlar.append(ism)
#    javob=input("Yana ism qo\'shasizmi (ha/yo\'q)")
#    if javob =='ha':
#        n+=1
#        continue
#    else:
#        break        
#print("Dostlaringiz ro\'yhati:")
#for ism in ismlar:
#    print(ism.title())

#cars=[]
#n=1
#while True:
    
 #   question=f'Write {n}-name of your dream car:>>>'
  #  name=input(question)
#    cars.append(name)
#    answer=input("Do you add a car(yes/no)")
#    if answer=='yes':
#     n+=1
#     continue
#    else:
#        break
    
#print("list of your dream cars:")
#for name in cars:
#    print(name.title())
    


#print("Dostingiding yoshlarini saqlaymiz .")
#dostlar={}
#ishora=True
#while ishora:
#    ism=input("Do\'stingizning ismini kiriting :")
#    yosh=input(f'{ism.title()}ning yoshini kiriting:')
#    dostlar[ism]=int(yosh)
#    
#    javob=input("Yana malumot qo\'shasizmi? (ha/yo\'q')")
#    if javob=="yo\'q":
#        ishora=False
#for ism,yosh in dostlar.items():
#    print(f"{ism.title()} {yosh} yoshda ")
        
#cars=['lacetti','nexia','toyota','nexia','audi','malibu','nexia']
#car='toyota'
#while car in cars:
#    cars.remove(car)
#print(cars)
#students=['hasan','husan','olim','botir']
#baholangan_talabalar={}
#while students:
#    student=students.pop()
#    baho=input(f'{student.title()}ning bahosini kiriting:')
#    print(f'{student.title()} baholandi')
#    baholangan_talabalar[student]=baho
#savat =[]
while True:
    mahsulot = input("Savatga mahsulot qo'shing:")
    savat.append(mahsulot)
    javob = input("Yana mahsulot qo\'shasizmi?(ha/yo\'q)")
    if javob != 'ha':
        break    
mahsulotlar = {}
while True:
    mahsulot = input("Mahsulot nomini kiriting: ")
    narh = input(f"{mahsulot.title()}ning narhini kiriting: ")
    mahsulotlar[mahsulot] = narh
    javob = input("Yana mahsulot qo'shasizmi?(ha/yo'q)")
    if javob != 'ha':
        break

buyurtmalar = ['olma','anjir','uzum','qovun']
mahsulotlar = {'olma':20000,
               'shaftoli':25000,
               'tarvuz':18000,
               'uzum':22000}

while buyurtmalar:
    buyurtma = buyurtmalar.pop()
    if buyurtma in mahsulotlar.keys():
        narh = mahsulotlar[buyurtma]
        print(f"{buyurtma.title()} - {narh} so'm")
    else:
        print(f"Bizda {buyurtma} yo'q")

































    