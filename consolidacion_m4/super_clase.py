# Importar módulo para trabajar archivo csv
import csv

# Super Clase
class Vehiculo:

    # Funcion inicializadora / Método constructor
    def __init__(self, marca:str, modelo:str, numero_de_ruedas:int) -> None:
        # Atributos de instancia
        self.marca = marca
        self.modelo = modelo
        self.numero_de_ruedas = numero_de_ruedas


    # Método mágico para imprimir el contenido
    def __str__(self) -> str:
        return "Marca {}, Modelo {}, {} ruedas".format(self.marca,self.modelo,self.numero_de_ruedas)
    

    # Funcion de escritura de csv
    def guardar_datos_csv(self, prefijo:str="_Bicicleta__", root:str="vehiculos.csv", sep:str=",")->None:
        """Escribe en un csv el objeto y sus atributos.
        Crea un archivo csv, si el archivo ya existe lo abre y escribe el contenido desde la última línea.

        Args:
            prefijo (str, optional): Prefijo que se desea eliminar de clases privadas. Defaults to "_Bicicleta__".
            root (str, optional): Ruta del archivo. Defaults to "vehiculos.csv".
            sep (str, optional): tipo de separador. Defaults to ",".
        """
        with open(root, "a", newline='', encoding="utf-8") as archivo:
            data = [type(self).__name__]  # data guarda una lista con el nombre de la clase de la cual se ha instanciado es igual a self.__class__.__name__ (Nombre de la clase)
            atributos = vars(self) # Guarda un diccionario de los atributos del objeto
            nuevos_atributos = {} # Diccionario vacío para guardar los atributos sin prefijo

            for llave, valor in atributos.items(): # Bucle para iterar sobre la llave y el valor del diccionario y remover el prefijo
                llave = llave.removeprefix(prefijo) # Prefijo de atributo privado a eliminar con la función
                nuevos_atributos[llave] = valor # Se guarda la llave sin prefijo con su valor en el diccionario vacío
            data.append(nuevos_atributos) # Se agregan el nuevo diccionario a la lista data. Ahora contiene nombre de la clase y diccionario con los atributos

            archivo = csv.writer(archivo, delimiter=sep)
            archivo.writerow(data)

    
    # Funcion de lectura de csv e impresión del contenido en terminal
    def leer_datos_csv(self, root:str="vehiculos.csv", sep:str=",")->str:
        """Busca el archivo entregado en la ruta para leerlo y separar en una lista independiente a cada objeto por su tipo.

        Args:
            root (str, optional): Ruta del archivo. Defaults to "vehiculos.csv".
            sep (str, optional): tipo de separador. Defaults to ",".

        Returns:
            str: Regresa un string que muestra en pantalla los objetos que contiene cada lista
        """
        # Listas independientes para cada clase
        lista_particular = []
        lista_carga = []
        lista_bicicleta = []
        lista_motocicleta = []

        with open(root, newline='', encoding="utf-8") as archivo:
            archivo = csv.reader(archivo, delimiter=sep)

            for objeto, atributos in archivo: # Bucle para iterar sobre el archivo y mediante un condicional verificar a que clase pertenece y agregarlo a la lista correspondiente
                if objeto == "Particular":
                    lista_particular.append(atributos)
                elif objeto == "Carga":
                    lista_carga.append(atributos)
                elif objeto == "Bicicleta":
                    lista_bicicleta.append(atributos)
                elif objeto == "Motocicleta":
                    lista_motocicleta.append(atributos)

        return "Lista de Vehiculos particular\n{}\n\nLista de Vehiculos carga\n{}\n\nLista de Vehiculos bicicleta\n{}\n\nLista de Vehiculos motocicleta\n{}\n\n".format(lista_particular, lista_carga, lista_bicicleta, lista_motocicleta)



