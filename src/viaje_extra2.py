distancia_km = 225000000

for vel in range(10000, 60000, 10000):
    tiempo_td = (distancia_km / vel)/24
    tiempo_s = tiempo_td // 7
    tiempo_d = tiempo_td % 7
    print(f"Velocidad: {vel} kmh -> Tiempo: {tiempo_s} semanas y {int(tiempo_d)} días")
