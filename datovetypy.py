cars = ["Ford", "Volvo", "BMW", "AUDI"]

print (cars)

for x in range(len(cars)):
    print(f"Auto {x+1}: {cars[x]}")

carplus = input("Zadejte auto: ")

cars.append(carplus)

for x in range(len(cars)):
    print(f"Auto {x+1}: {cars[x]}")