distancia = int(input("Dime cuál es la distancia a recorrer"))

print(f"La distancia total en km es {distancia}")
parada = 0
for x in range(0, distancia, 150000):
    print(f"Parada en el kilometro {x}")
    parada +=1

print(f"El total de paradas para repostar es de {parada}")