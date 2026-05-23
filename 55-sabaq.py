 #tekstegi dawisli haripler sanin aniqlan

text = input("Gap jazin: ")
vowels = "auie"
count = 0
for char in text:
    if char in vowels:
        count += 1
print("dawisli haripler sani:", count)   