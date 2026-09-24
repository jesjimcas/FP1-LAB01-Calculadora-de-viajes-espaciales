distancia_km = 225000000

for vel in range(10000, 60000, 10000):
    tiempo_d = (distancia_km / vel)/24
    print(f"Velocidad: {vel} kmh -> Tiempo: {tiempo_d} días")
