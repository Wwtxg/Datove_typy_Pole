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
    for y in range(100):

        kosikplus = int(input("Zadejte cislo zbozi: "))

        kosik.append(zbozi[kosikplus - 1])
        print ("Kosik: ", kosik)

        zbozi.remove(zbozi[kosikplus - 1])
        vypis_zbozi(zbozi)

elif Vyber == 2:
    for y in range(100):

        kosikplus = str(input("Zadejte nazev zbozi: "))

        kosik.append(kosikplus)
        print ("Kosik: ", kosik)

        zbozi.remove(kosikplus)
        vypis_zbozi(zbozi)



