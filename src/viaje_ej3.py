edad = int(input("Dime la edad:"))
nivel_fisico = int(input("Dime el nivel físico"))

while  not (1 <= nivel_fisico <= 10):
    print("Tu nivel fisico debe estar entre 1 y 10")
    nivel_fisico = int(input("Dime el nivel físico"))

if edad < 18:
      print("Debes ser mayor de edad")
elif nivel_fisico < 5:
        print("Debes estar en mejor forma")
else:
       print("¡Listo para despegar!")
