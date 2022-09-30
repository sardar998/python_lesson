# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 23:32:37 2022

@author: Sardar king
"""

#def salom_ber():
#    """Salom beruvchi funksiya"""
#    print("Assalomu alaykum!")
#print(salom_ber())
#def salom_ber(ism):
 #   """Foydalanuvchi ismini qabul qilib,unga salom beruvchi funksiya"""
  #  print(f'Assalomu alaykum,hurmatli {ism.title()}!')
#   print(salom_ber('Sardor'))
#print(salom_ber("sardar"))
#print(salom_ber("sardar").__doc__)
#salom_ber('sard')
#def toliq_ism(ism,familiya):
#   """Foydalanuvchi ism va familya jamlap chiqaruvchi funksiya"""
#   print(f'Foydalanuvchi familya ismi: {ism.title()}\n'
#          f'foydaluvchi familiyasi: {familiya.title()}')
#print(toliq_ism('sardar', 'abdezov'))
#def yosh_hisobla(ism,tugilgan_yil):
 #   """Foydaluvchi yoshini hisovlichi dastur"""
#   print(f"{ism.title()} {2022-tugilgan_yil} yoshda")
#print(yosh_hisobla("sardar", 1998))    
#print(yosh_hisobla("sardar", 1997))
#
#def yosh_hisobla(tugilgan_yil,joriy_yil=2022):
#    """Foydaluvchi tug\'ilgan yilidan uning yoshini hisoblaydi"""
#    print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")
    
#print(yosh_hisobla(198))
#print(yosh_hisobla(1998,2023))

#def yosh_hisobla(tugilgan_yil,joriy_yil=2022):
#   """Foydalanuvchi tug'ilgan yilidan uning yoshini hisoblaydi"""
#    print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")
#tyil=int(input("Tug'ilgan yilingizni kiriting:"))
#print(yosh_hisobla(tyil))

#def salom_ber(ism):
#    """Salom beruvchi funksiya"""
#    print(f"Assalomu alaykum {ism.title()}!")

#salom_ber('hasan')

     
    #1
#def ask_age(age,this_year=2022):
#    """This function find somebody age"""
#    print(f"You are {this_year-age} years old")
#age1=int(input("Write your born year:"))
#print(ask_age(age1))
    #2
#print("I think it is very usefull for you.")
#def age_number(number):
#    """find square and cube """  
#    print(f"Your number square is {number**2} \n Your number cube is {number**3}")
#number1=int(input("Write number:"))    
#print(age_number(number1))
    #3
#print("This funtion find number is even or odd")
#question=int(input("Write number:"))
#n=question
#def even_odd(number):
 #   """this funtion find even or odd""" 
#    if n%2:
#        print(f"Your number {n} is even")
#    else:
#        print(f"Your number {n} is odd")
#print(even_odd(n))
#print("Write two numbers")
#a=int(input("Write first number:"))
#b=int(input("Write second number:"))        
#def number(number1,number2):
#    """comparative number each other"""
#    if a<b:
#        print(b)
#    elif a>b:
#        print(a)
#    else:
#        print(a,b)
#print(number(a, b))
         #4
#def bolisg_amali(son):
#    """sonni qoldiqsiz boladi"""
#    for n in range(1,101):
#        if not son%n:
#         print(f'{son} {n}ga qoldiqsiz bolinadi')
         
#print(bolisg_amali(333))

#def toliq_ism_yasa(ism,familiya):
#    """toliq ism qaytaruvchi funksiya"""
#    toliq_ism=f"{ism.title()} {familiya.title()}"
#    return toliq_ism
#talaba1=toliq_ism_yasa("Olim", "hakimov")
#talaba2=toliq_ism_yasa("hakim", "olimov")
#print(talaba1,talaba2)

#def toliq_ism_yasa(ism,familiya,otasining_ismi=''):
#    """Toliq ism qaytauvchi funksiya"""
#    if otasining_ismi:
#        toliq_ism=f"{ism} {otasining_ismi} {familiya}"
#    else:
#        toliq_ism=f"{ism} {familiya}"
#   return toliq_ism.title()
#talaba1=toliq_ism_yasa("olim", "hakimov")
#talaba2=toliq_ism_yasa("hakim", "olimov","abrorov")  
#print(talaba1,
#      talaba2)
  
def avto_info(kompaniya,model,rangi,korobka,yili,narhi=None):
    avto={"kompaniya":kompaniya,"model":model,"rang":rangi
          ,"korobka":korobka,"yil":yili,'narh':narhi}
    return avto
#avto1=avto_info("GM",'Malibu','Qora','Avtomat',2018)
#avto2=avto_info("GM",'Gentra',"Oq",'Mexanika',2016,15000)
#avtolar=[avto1, avto2]
#print("Onlayn bozordagi mavjud avtomashinalar:")
#for avto in avtolar:
#    if avto["narh"]:
#        narh=avto["narh"]
#    else:
#        narh="Nomalum"
#    print(f"{avto['rang']} {avto['model']}.Narhi: {narh}")
    
#def oraliq(min,max):
#    sonlar=[]
#    while min<max:
#        sonlar.append(min)
#        min+=1
#    return sonlar
#print(oraliq(0, 10))
#print(oraliq(10, 21))
    
#def oraliq(min,max,so=""):
#    sonlar=[]
#    while min<max:
#     if so:
#        sonlar.append(min)
#        min+=so
#     else:
#         sonlar.append(min)
#         min+=1
#    return sonlar
#print(oraliq(0, 101,10))
print("Saytimizdagi avtolar ro\'yxatini shakllantiramiz.")
avtolar=[]
while True:
    print("\nQuyidagi ma\'lumotlani kiriting",end='')
    kompaniya=input("\nIshlab chiqauvchi:")
    model=input("Modeli:")
    rangi=input("Rangi:")
    korobka=input("Korobka: ")
    yili=input("Ishlab chiqailgan yili:")
    narhi=int(input("Narhi:"))
    
    avtolar.append(avto_info(kompaniya,model,rangi,korobka,yili,narhi))
    
    javob=input("Yana avto qo\'shasizmi? (yes/no):")
    if javob=='no':
        break







    