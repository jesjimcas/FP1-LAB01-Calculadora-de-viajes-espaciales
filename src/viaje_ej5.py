distancia_km = int(input("Cuanto es la distancia en km?"))  # distancia Tierra - Luna
velocidad_kmh = int(input("Cuanto es la velocidad en kmh?"))
tiempo_horas = distancia_km // velocidad_kmh
tiempo_dias = tiempo_horas // 24
print(f"Tardarías {tiempo_dias} días en llegar.")

respuesta = input("Quieres hacer otra simulación?")

if respuesta == "s":
    distancia_km = int(input("Cuanto es la distancia en km?"))  # distancia Tierra - Luna
    velocidad_kmh = int(input("Cuanto es la velocidad en kmh?"))
    tiempo_horas = distancia_km // velocidad_kmh
    tiempo_dias = tiempo_horas // 24
    print(f"Tardarías {tiempo_dias} días en llegar.")

    respuesta = input("Quieres hacer otra simulación?")
elif respuesta == "n":
    print("El programa ha terminado")
