print("Control de Flota")
camion= (input("Ingrese su Patente: "))
cantidadviajes=(input("Ingrese la cantidad de Viajes: "))
km=int(input("Cantidad de Kilometros transcurridos: "))
litgas=int(input("Cantidad de Gasoil usado: "))
costogasoil=int(input("Costo de Gasoil: $"))
costomant=int(input("Adicionales: $"))

kmxlitr= (km/litgas)
total= (costogasoil+costomant)
costoxkm= (total/km)

print("__Gastos__")
print("camion: ",camion, "viajes: ", cantidadviajes)
print("Km transcurridos x litros: ",kmxlitr)
print("Total del viaje: $",total)
print("Costo x Kilometros: $",costoxkm)
