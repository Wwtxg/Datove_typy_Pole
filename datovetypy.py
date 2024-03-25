cars = ["Ford", "Volvo", "BMW", "AUDI"]

print (cars)

def vypis_pole(prvek):
    for x in range(len(prvek)):
        print(f"Auto {x+1}: {cars[x]}")

carplus = input("Zadejte auto: ")

cars.append(carplus)
vypis_pole(cars)

print ("   ")

carminusstr = str(input("Co odebrat str "))
cars.remove(carminusstr)
vypis_pole(cars)

carminus = int(input("Co odebrat "))
cars.pop(carminus)
vypis_pole(cars)

