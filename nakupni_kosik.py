zbozi = ["CPU", "GPU", "RAM", "HDD", "SSD", "Motherboard", "Chlazení vodní", "Zdroj", "Case"]

kosik = []

print ("Nabidka")

def vypis_zbozi(zbozi):
    for x in range(len(zbozi)):
        print(f"{x+1}: {zbozi[x]}")

vypis_zbozi(zbozi)

print ("Pro vyber zbozi podle cisla zmackni 1")

print ("Pro vyber zbozi podle nazvu zmackni 2")

Vyber = int(input("Vas vyber: "))

if Vyber == 1:
    for y in range(9):

        kosikplus = int(input("Zadejte cislo zbozi: "))

        kosik.append(zbozi[kosikplus - 1])
        print ("Kosik: ", kosik)

        zbozi.remove(zbozi[kosikplus - 1])
        vypis_zbozi(zbozi)

elif Vyber == 2:
    for y in range(9):

        kosikplus = str(input("Zadejte nazev zbozi: "))

        kosik.append(kosikplus)
        print ("Kosik: ", kosik)

        zbozi.remove(kosikplus)
        vypis_zbozi(zbozi)



word_random = []

for x in range(lenght_str):
   word_random.append(random.choices(string.ascii_uppercase))

print (word_random)

for y in range(len(word_random)):
    print (f"{word_random[y+1]}")


for y in range(lenght_str):
    word_random_promena = (random.choices(string.ascii_uppercase))
    word_random.append(word_random_promena)