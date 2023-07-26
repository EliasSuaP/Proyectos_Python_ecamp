# Importar Super clase con métodos para lectura y escritura csv
from super_clase import Vehiculo
# Importar cada una de las clases
from clases import Automovil, Bicicleta, Carga, Motocicleta, Particular, Vehiculo

#########################################################################
############################ SPRINT 1 ###################################
#########################################################################

vehiculos = [] # Genero una lista vacía para almacenar las instancias
cantidad = int(input("Cuántos vehículos desea insertar: ")) # cantidad de instancias que quiere crear el usuario

for i in range(cantidad):  # Bucle para generar cada instancia
    marca = input("Inserte la marca del automóvil: ")
    modelo = input("Inserte el modelo: ")
    nro_ruedas = int(input("Inserte el número de ruedas: "))
    velocidad = int(input("Inserte la velocidad en km/h: "))
    cilindrada = int(input("Inserte cilindraje en cc: "))

    automovil = Automovil(marca, modelo, nro_ruedas, velocidad, cilindrada) # Se entrega cada input como una instancia de la clase Automovil
    vehiculos.append(automovil) # Se inserta la instancia a la lista vehiculos


print("\nImprimiendo por pantalla los vehículos:\n ")
for vehiculo in vehiculos: # Bucle para imprimir cada vehiculo instanciado 
    i = 1
    print("Datos del automóvil: {} : {}".format(i,vehiculo))
    i += 1

############################################################################
############################ SPRINT 2 ######################################
############################################################################

# Instancias de cada objeto
particular = Particular("Ford", "Fiesta", 4, "180", "500", 5)
carga = Carga("Daft Trucks", "G 38", 10, 120, "1000", "20000")
bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
motocicleta = Motocicleta("BMW", "F800s",2,"Deportiva","2T","DobleViga", 21)


instancias = [particular, carga, bicicleta, motocicleta] # Lista de todas las instancias
for instancia in instancias: # Bucle para imprimir cada objeto instanciado
    print(instancia)

clases = [Vehiculo, Automovil, Particular, Carga, Bicicleta, Motocicleta] # Lista de todas las clases
for clase in clases: # Bucle para verificar relación de la instancia motocicleta con las clases creadas
    print(f"Motocicleta es instancia con relación a {clase.__name__}: {isinstance(motocicleta,clase)}")

############################################################################
############################ SPRINT 3 ######################################
############################################################################

for ins in instancias: # Bucle para aplicar el método guardar_datos_csv a todos los elementos de la lista instancias y escribir en el archivo csv su contenido
    ins.guardar_datos_csv()

print(particular.leer_datos_csv()) # Leer archivo csv y mostrar por terminal una lista de cada grupo de objeto