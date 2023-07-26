# Importar super clase Vehiculo de la cuál heredan todas las clases de este archivo.
from super_clase import Vehiculo

# Clase hereda de Vehiculo y super clase de Particular, Carga
class Automovil(Vehiculo):

    # Funcion incilializadora
    def __init__(self, marca:str, modelo:str, numero_de_ruedas:int, velocidad:int, cilindrada:int) -> None:
        super().__init__(marca, modelo, numero_de_ruedas)
        # Atributos de instancia
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    # Sobrecarga de método mágico
    def __str__(self) -> str:
        return super().__str__() + ", {} km/h, {} cc".format(self.velocidad,self.cilindrada)


# Clase hereda de Automovil
class Particular(Automovil):

    # Funcion inicializadora
    def __init__(self, marca:str, modelo:str, numero_de_ruedas:int, velocidad:int, cilindrada:int, nro_puestos:int) -> None:
        super().__init__(marca, modelo, numero_de_ruedas, velocidad, cilindrada)
        # Atributos de instancia
        self.nro_puestos = nro_puestos

    # Sobrecarga de método mágico
    def __str__(self) -> str:
        return super().__str__() + ", {} Puestos".format(self.nro_puestos)


# Clase Hereda de Automovil
class Carga(Automovil):

    # Funcion inicializadora
    def __init__(self, marca:str, modelo:str, numero_de_ruedas:int, velocidad:int, cilindrada:int, carga_kg:int) -> None:
        super().__init__(marca, modelo, numero_de_ruedas, velocidad, cilindrada)
        # Atributos de instancia
        self.carga_kg = carga_kg

    # Sobrecarga de método mágico
    def __str__(self) -> str:
        return super().__str__() + ", Carga : {} kg".format(self.carga_kg)


# Clase hereda de Vehiculo, Super clase de Motocicleta
class Bicicleta(Vehiculo):

    # Funcion inicializadora
    def __init__(self, marca:str, modelo:str, numero_de_ruedas:int, tipo:str) -> None:
        super().__init__(marca, modelo, numero_de_ruedas)
        # Atributo de instancia
        self.__tipo = tipo

    # Método getter / Accesador de tipo
    @property
    def tipo(self)->str:
        return self.__tipo

    # Métodos setter / Mutadores de marca y modelo
    @tipo.setter
    def tipo(self, valor)->str:
        self.__tipo = valor

    # Sobrecarga de método mágico
    def __str__(self) -> str:
        return super().__str__() + ", Tipo : {}".format(self.tipo)


# Clase hereda de Bicicleta
class Motocicleta(Bicicleta):

    # Funcion inicalizadora
    def __init__(self, marca:str, modelo:str, numero_de_ruedas:int, tipo:str, nro_radio:str, cuadro:str, motor:str) -> None:
        super().__init__(marca, modelo, numero_de_ruedas, tipo)
        # Atributos de instancia
        self.nro_radio = nro_radio
        self.cuadro = cuadro
        self.motor = motor

    # Sobrecarga de método mágico
    def __str__(self) -> str:
        return super().__str__() + ", Tipo : {}, Motor : {}, Cuadro : {}, Nro Radios : {}".format(self.tipo, self.motor, self.cuadro, self.nro_radio)


#######################
# Probando instancias #
#######################
if __name__ == "__main__":
    # Instancias de objetos
    particular = Particular("Ford", "Fiesta", 4, "180", "500", 5)
    carga = Carga("Daft Trucks", "G 38", 10, 120, "1000", "20000")
    bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
    motocicleta = Motocicleta("BMW", "F800s",2,"Deportiva","2T","DobleViga", 21)

    # Imprimir caracteristicas del objeto
    print(particular)
    print(carga)
    print(bicicleta)
    print(motocicleta)

    # Verificar si Motocicleta tiene relación con las clases
    clases = [Vehiculo, Automovil, Particular, Carga, Bicicleta, Motocicleta]
    for clase in clases:
        print(f"Motocicleta es instancia con relación a {clase.__name__}: {isinstance(motocicleta,clase)}")
        

    # print(f"Motocicleta es instancia con relación a Automovil: {isinstance(motocicleta,Automovil)}")
    # print(f"Motocicleta es instancia con relación a Vehiculo Particular: {isinstance(motocicleta,Particular)}")
    # print(f"Motocicleta es instancia con relación a Vehiculo de Carga: {isinstance(motocicleta,Carga)}")
    # print(f"Motocicleta es instancia con relación a Vehiculo Bicicleta: {isinstance(motocicleta,Bicicleta)}")
    # print(f"Motocicleta es instancia con relación a Vehiculo Motocicleta: {isinstance(motocicleta,Motocicleta)}")

    # Prueba
    print(type(particular))
    print(particular.__class__)

    bicicleta.guardar_datos_csv()
    particular.guardar_datos_csv()
    carga.guardar_datos_csv()
    motocicleta.guardar_datos_csv()
    print(particular.leer_datos_csv())
