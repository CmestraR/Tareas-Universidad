#Miembros de la raza benévola
#Ositos, valor en batalla = 1
#Principes, valor en batalla = 2
#Enanos, valor en batalla = 3
#Caris, valor en batalla = 4
#Fulos, valor en batalla = 5

#Miembros de la raza Malvada
#Lolos, valor en batalla = 2
#Fulanos, valor en batalla = 2
#Hoggins, valor en batalla = 2
#Lurcos, valor en batalla = 3
#Trollis, valor en batalla = 5

print("------------------------- INICIO DEL JUEGO -------------------------")
print("""El planeta Centauro está en guerra! 
En este planeta existe una raza de malvados leales a Throm 
que luchan contra otra raza benévola que no quieren que el mal reine en el planeta. Ayudalos a sobrevivir

Miembros de la raza Malvada    | Miembros de la raza benévola   
------------------------------ | ------------------------------
Nombre    Valor en batalla     |  Nombre    Valor en batalla
------------------------------ | ------------------------------
Lolos             2            |  Ositos           1
Fulanos           2            |  Principes        2
Hoggins           2            |  Enanos           3
Lurcos            3            |  Caris            4
Trollis           5            |  Fulos            5
------------------------------ | ------------------------------
""")
print("""
      ------------------------- SELECCIONA LOS GERREROS DE LA RAZA MALVADA -------------------------
      """)
print("Selecciona tus gerreros de la raza Malvada:")
lolos = int(input("Ingresa el número de Lolos que pelearan: "))
fulanos = int(input("Ingresa el número de Fulanos que pelearan: "))
hoggins = int(input("Ingresa el número de Hoggins que pelearan: "))
lurcos = int(input("Ingresa el número de Lurcos que pelearan: "))
trollis = int(input("Ingresa el número de Trollis que pelearan: "))

lolos = lolos * 2
fulanos = fulanos * 2
hoggins = hoggins * 2
lurcos = lurcos * 3
trollis = trollis * 5

suma_puntos_malvados = lolos + fulanos + hoggins + lurcos + trollis


print("""
      ------------------------- SELECCIONA LOS GERREROS DE LA RAZA BENÉVOLA -------------------------
      """)

print("Selecciona tus gerreros de la raza benévola:")
ositos = int(input("Ingresa el número de Osistos que pelearan: "))
principes = int(input("Ingresa el número de principes que pelearan: "))
eneanos = int(input("Ingresa el número de eneanos que pelearan: "))
caris = int(input("Ingresa el número de caris que pelearan: "))
fulos = int(input("Ingresa el número de fulos que pelearan: "))

ositos = ositos * 1
principes = principes * 2
enanos = eneanos * 3
caris = caris * 4
fulos = fulos * 5

suma_puntos_benevolos = ositos + principes + eneanos + caris + fulos

if suma_puntos_benevolos > suma_puntos_malvados:
    print("""
          Ha ganado el ejercito Benévolo, el planeta Centauro se ha salvado!!!
          """)
elif suma_puntos_malvados > suma_puntos_benevolos:
    print("""
          Ha ganado el ejercito Malvado, el planeta Centauro a sido capturado por los leales a Throm!!!
          """)
elif suma_puntos_malvados == suma_puntos_benevolos:
    print("""
          La batalla para salvar a el planeta Centauro ha sido un empate entre los ejercitos!!!
          """)
else:
    print("""
          Ningun ejercito a ganado esta batalla!!!
          """)
    
    
