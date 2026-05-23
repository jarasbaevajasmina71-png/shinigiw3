#----------------------------------------------------------------- Ramdom  ------------------------------------------------------------------------------------------------------
#------------------------------------------------------- Randomnin funikciyalari ------------------------------------------------------------------------------------------------
import random
# random.random()-------------------------------------------------------------------------------------------random.random  funkciyasi
# san = random.random()
# print(san)
#san = random.randint(1,11)--------------------------------------------------------------------------------random.randint funikciyasi
#miyweler = ['alma', 'shabdal', 'almurt', 'juzim', 'shabdal', 'banan']
#random_miyweler = random.choice(miyweler)-----------------------------------------------------------------random.choice funkciyasi
#print(random_miyweler)
#sanlar = [1,2,3,4,5,6,7,8,9]
#random.shuffle(sanlar)------------------------------------------------------------------------------------random.chorffle funkciyasi
#print(sanlar)
#san = random.uniform(1.5 , 10.6)-------------------------------------------------------------------------random.uniform funkciyasi
#print(san)
#atlar = ['Begdiyar', 'Sultan','Nurlan', 'Erlan', 'Aqilbek', 'Sardar']
#b = random.sample(atlar, 2)------------------------------------------------------------------------------random.sample funkciyasi
#print(b)

#seed
'''random.seed(5)

print(random.randint(1,100))

kopyupa = (500, 1000, 10000)

for i in range(5):
    print(random.choice(kopyupa)) '''

#randrange

'''san = random.randrange(10,101,10)
print(san)'''

'''
atlar = ['Shaxsanem', 'Gulsanem', 'Jasmin', 'Araylim', 'Aqilbek', 'Asadbek', 'Nurdawlet', 'Qudaybergen', 'Rasul', 'Abdiraxim']
for at in atlar:
    ball = random.randint(1, 100)
    print(f"{at} -> {ball} ball")'''


'''atlar = ['Begdiyar', 'Sultan','Nurlan', 'Erlan', 'Aqilbek', 'Sardar']
b = random.sample(atlar, 2)
print(b)
'''

'''random.random()
san = random.random()
print(san)'''


'''san = random.randint(1,11)
miyweler = ['alma', 'shabdal', 'almurt', 'juzim', 'shabdal', 'banan']
random_miyweler = random.choice(miyweler)
print(random_miyweler)'''


'''sanlar = [1,2,3,4,5,6,7,8,9]
random.shuffle(sanlar)
print(sanlar)'''


'''san = random.uniform(1.5 , 10.6)
print(san)'''

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Random ham onin funkcyalari
import random


#randint
'''
san = random.randint(1,10)

print(san)

'''


#randrange
'''
print(random.randrange(1,10))

'''

#Choice
'''
miyweler =['alma','anar','juzim','banan']

print(random.choice(miyweler))

'''


#shuffle
'''
miyweler =['alma','anar','juzim','banan']

random.shuffle(miyweler)

print(miyweler)

'''

#sample
'''
sanlar= [1,2,3,4,5,6,7,8,9]

print(random.sample(sanlar,3))

'''

#random
'''
print(random.random())
'''



#uniform
'''
print(random.uniform(1,10))

'''


#choice
'''
miyweler =['alma','anar','juzim','banan']

print(random.choices(miyweler,k=5))

'''


#seed
'''
random.seed(2)

print(random.randint(1,100))
print(random.randint(1,100))
print(random.randint(1,100))
print(random.randint(1,100))

'''

#randrange
'''
san = random.randrange(10,101,5)

print(san)

'''

#choice
'''
print(random.choice([30,50,70]))

'''



'''
a = str(input("Atiniz kim? "))
print( f'{a} sizdin baliniz {random.randint(10,100,5)}')
'''


a = [random.randrange(1,101),
    random.randrange(1,101),
    random.randrange(1,101),
    random.randrange(1,101),
    random.randrange(1,101),
    random.randrange(1,101),
    random.randrange(1,101),
    random.randrange(1,101),
    random.randrange(1,101),
    random.randrange(1,101)]

print(
    a,
    '\n',sorted(a),
    '\n', max(a),
    '\n',min(a),

)