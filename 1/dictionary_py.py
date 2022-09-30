# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 23:51:59 2022

@author: Sardar king
"""

#car_0={'model':'ferrari','rang':'red'}
#print(car_0)
#print(car_0['rang'])
#talaba_0={'ism':'Sardar','age':'24','born_year':'1998'}
#print(f"{talaba_0['ism'].title()},{talaba_0['born_year']} was born,{talaba_0['age']} age old")
#talaba_0['kurs']=4
#talaba_0['fakultet']="informatika"
#print(talaba_0)
#talaba_1={}
#talaba_1["ism"]="Sardar Abdezov"
#talaba_1['kurs']=4
#talaba_1['age']=24
#print(talaba_1)
#print(f"Student {talaba_1['ism'].title()} {talaba_1['kurs']} kurs")
#telefonlar={'ali':'iphone x','vali':'samsung s20','olim':'mi 11'}
#print(telefonlar)
#phone=telefonlar['ali']
#print(f'Alining telefoni {phone}')
#phone=telefonlar.get('hasan','Bunday ism mavjud emas')
#print(phone)
my_friend=['nurbolad','alisher','usen','nurlibay','jappar']
#nurbolad={'age ':24,'surename':'omirzakov','gender':'man'}
#alisher={'age ':24,'surename':'akimov','gender':'man'}
#usen={'age ':24,'surename':'abdumominov','gender':'man'}
#nurlibay={'age ':24,'surename':'zulqaynar','gender':'man'}
#jappar={'age ':24,'surename':'sultanov','gender':'man'}
#print(my_friend)

#print(usen)
#food={'sardar':'shashlik','nurbolad':'plov','usen':'doner','alisher':'samsa'}
#print(f'my foverite food {food}')
#print(food['sardar'])

#talaba_0={'ism':'aligon','falmiliya':'shamshiyev','yosh':22,'fakultet':'matematika','kurs':4}
#print(talaba_0)

#for kalit,qiymat in talaba_0.items():
    #print(f'Kalit:{kalit}')
    #print(f'Qiymat:{qiymat} \n')
    
#telefonlar={'ali':'iphone','vali':'galaxy s9','olim':'mi 10 pro','orif':'nokia 3310','hamida':',galaxty s9','maryam':'huawei p30','tohir':'iphone x','umar':'iphone x'}
#for k,q in telefonlar.items():
 #   print(f'{k.title()}ning telefoni {q}')    

#mahsulotlar={'olma':10000,'anor':20000,'uzum':40000,'anjir':25000,'shaftoli':30000}
#print(mahsulotlar.keys())

#print("do'kondagi mahsulotlar:")
#for mahsulot in mahsulotlar.keys():
 #   print(mahsulot.title())
#bozorlik=['anor','uzum','non','baliq']
#for mahsulot in mahsulotlar:
 #   if mahsulot in bozorlik:
  #      print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} so'm")
 
#for buyum in bozorlik:
 #   if buyum not in mahsulotlar:
  #      print(f"Iltimos ,do'koningizga {buyum} ham olib kling")
#print("Dokonimizdagi mahsulotlar:")
#for mahsulot in sorted(mahsulotlar):
 #   print(mahsulot.title())
    
#print(telefonlar.values())
        
#print(mahsulotlar.values())

#print('Foydalanuchilar quyidagi telefonlarni ishlatishadi:')
#for tel in set(telefonlar.values()) :
 #   print(tel)
    
#malumot={'float':'bu onlik son','for':'biror amalni qayta qayta ishlash','if':'shartlarni tekshirish operatori','integer':'butun  son','len':'guruxtagi narsaing sonin aytadi',"sorted":"alifba bilat chiqarish"}
#for key,value in sorted(malumot.items()):
 #   print(f"{key.title()} -{value}")
#print('Hello world')
#mamlakatlar={"AQSH":'Washington','ITALIYA':'Rim',',malayziya':"Kuala-lumpur","O'zbekiston":"toshkent",'qirgistin':'bishkek'}
#for kalit, qiymat in mamlakatlar.items():
 #   print(f"kalit:{kalit}")
  #  print(f"Qiymat:{qiymat}\n")
#print(f'dunyo davlatlari {mamlakatlar.keys()}')



#print(f'Davlatlaning poytahti {mamlakatlar.values()}')

#davlatlar = {
 #   "o'zbekiston":'toshkent',
  #  'aqsh':'washington d.c.',
   # 'rossiya':'moskva',
#    'tojikiston':'dushanbe',
 #   "qirg'iziston":'bishkek',
  #  'qozog\'iston':'nursulton',
   # 'malayziya':'kuala-lumpur',
#    'singapur':'sungapur',
 #   'italiya':'rim'}
#print('Dunyo davlatlari:')
#for davlat in sorted(davlatlar):
 #   print(davlat.upper())
#print('\nDavlatlarinig poytaxtlari ')
#for poytaxt in sorted(davlatlar.values()):
 #   print(poytaxt.title())    
#country=input('Qaysi davlatning poytaxtini bilishni istaysiz?:').lower()
#capital=davlatlar.get(country)
#if capital==None:
 #   print('Kechirasiz ,bizda bu haqida malumot yoq')
#else:
 #   print(f"{country.upper()}ning poytaxti {capital.title()} shahri")
    
#food={'plov':1200,'guyru lagman':1500,'beshbamak':2000,'qazan kebab':2500,'narin':1300,'sorpa':1190}
#print('3 ta taom buyurtma bering.')
#buyurtmalar=[]
#for n in range(3):
 #   buyurtmalar.append(input(f'{n+1}-taom ?>>>').lower())
#for buyurtma in buyurtmalar:
 #   if buyurtma in food:
  #      print(f'{buyurtma.title()} {food[buyurtma]} som')
   # else:
    #    print(f'Keshirasiz, bizda {buyurtma} yoq')
car0={'model':"lacetti",'rang':'oq','yil':2018,'narh':13000,'km':50000,'korobka':"avtomat"}        
car1={'model':"nexia 3",'rang':'qora','yil':2015,'narh':9000,'km':89000,'korobka':"mexanika"}        
car2={'model':"gentra",'rang':'qizil','yil':2019,'narh':15000,'km':20000,'korobka':"mexanika"}            

#car=car2
#print(f"{car['model'].title()},\
#{car['rang']}rang,\
#{car['yil']}-yil,{car['narh']}$    " )

#cars=[car0,car1,car2]
#for car in cars:
 #   print(f"{car['model'].title()},\
  #  {car['rang']}rang,\
   # {car['yil']}-yil,{car['narh']}$    ")
#print(cars[0])


#malibus=[]
#for n in range(10):
 #   new_car={'model':'malibu','rang':None,'yil':2020,'narh':None,'km':0,'korobka':'avto'} 
  #  malibus.append(new_car)

#for malibu in malibus[:3]:
 #   malibu['rang']='qizil'
#print(malibus)
#for malibu in malibus[3:6]:
 #   malibu['rang']='qizil'
#for malibu in malibus[6:]:
 #   malibu['rang']='qora'
  #  malibu['korobka']='mexanika' 
#for malibu in malibus:
 #   if malibu['korobka']=='avto':
  #     malibu['narh']=40000
   # else:
    #    malibu['narh']=35000
    
#print(malibus)
#dasturchilar={'ali':['python','c++'],'vali':['html','css','js'],'hasan':['php','sql'],'husan':['python','php'],'maryam':['c++','c#']
 #          }
#for ism,tillar in dasturchilar.items():

   # print(f'\n{ism.title()} quyidagi dasturlah tillarini biladi:')
   # for til in tillar:
     #   print(f'{til.upper()} ',end='')

#hamkasblar = {
 #   'ali':{'familiya':'valiyev',
  #         'tyil':1995,
   #        'malumot':'oliy',
    #       'tillar':['python','c++']
    #       },
    #'vali':{'familiya':'aliyev',
     #       'tyil':2001,
      #      'malumot':"o'rta-maxsus",
       #     'tillar':['html', 'css', 'js']},
 #   'hasan':{'familiya':'husanov',
  #           'tyil':1999,
   #          'malumot':'maxsus',
    #         'tillar':['python','php']}
    #}
#for ism, info in hamkasblar.items():
 #  print(f"\n{ism.title()} {info['familiya'].title()}, "
  #        f"{info['tyil']}-yilda tug'ilgan. "
  #        f"Ma'lumoti: {info['malumot']}. \n"
   #       "Quyidagi dasturlash tillarini biladi:")
    #for til in info['tillar']:
     #   print(til.upper())
#mashxur_insonlar={'Abu Abdulla Muhammad ibn Ismoil':{'tugilgan_yil':810,'tugilgan_yer':'Buxoro','yil_umr':60}
#'Abdulla Qodiriy':{"tugilgan_yil":1894,}}
buxoriy = {'ism':'Abu Abdulloh Muhammad ibn Ismoil',
           'tyil':810,
           'vyil':870,
           'tjoy':'Buxoro'
           }

qodiriy = {'ism':'Abdulla Qodiriy',
           'tyil':1894,
           'vyil':1938,
           'tjoy':'Toshkent'
           }

vohidov = {'ism':'Erkin Vohidov',
           'tyil':1936,
           'vyil':2016,
           'tjoy':"Farg'ona"
           }

navoiy = {'ism':'Alisher Navoiy',
           'tyil':1441,
           'vyil':1501,
           'tjoy':"Xirot"
           }

shaxslar = [buxoriy, qodiriy, vohidov, navoiy]

for shaxs in shaxslar:
    ism=shaxs['ism']
    tyil=shaxs['tyil']
    vyil=shaxs['vyil']
    tjoy=shaxs['tjoy']
    print(f'{ism} {tyil}-yilda {tjoy}da tavallud topgan.'
          f'{vyil-tyil} yil umr ko\'rgan .')
    
print("hello world")
























