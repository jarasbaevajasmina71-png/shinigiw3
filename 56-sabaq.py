#tapsirma

'''Random 3 dana random san oylaydi
ham paydalaniwishiga soni tabiwin buyiradi 
paydalaniwshi inputqa random 3 sandi jazadi ham sol 3 sannin ishinen neshewi sol oylagan
sanina tuwri keletugin bolsa soni shigariwi kerek '''


import random

random_sanlar = [random.randint(1, 9) for _ in range(3)]

print("Kompyuter 3 san oyladi.")

tabilgan = []

while len(tabilgan) < len(random_sanlar):

    user_input = input("3 dana san jazin: ")
    user_sanlar = list(map(int, user_input.split()))

    for san in user_sanlar:

        if san in random_sanlar and san not in tabilgan:
            print(san, "- duris san!")
            tabilgan.append(san)

    print("Hazirge tabilgan sanlar:", tabilgan)

print("Barliq sanlar tabildi!")
print("Kompyuter oylagan sanlar:", random_sanlar)
  