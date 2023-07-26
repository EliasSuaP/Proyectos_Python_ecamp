nombres = ['Harry Houdini', 'Newton', 'David Blaine', 'Hawking', 'Messi', 'Teller', 'Einstein', 'Pele', 'Juanes']

magos = [] # [i for i in nombres if i in ['Harry Houdini','David Blaine','Teller']]
cientificos = []
otros = []


def separa_nombres(nombres:list)->list:
    """_summary_
    Recibe una lista de strings y los separa según magos, científicos y otros.
    Args:
        nombres (list): _lista de nombres con string_

    Returns:
        list: _devuelve los elementos separados en su respectiva lista_
    """
    for nombre in nombres:
        if nombre == 'Harry Houdini' or nombre =='David Blaine' or nombre == 'Teller':
            magos.append(nombre)
        elif nombre == 'Newton' or nombre == 'Hawking' or nombre == 'Einstein':
            cientificos.append(nombre)
        else:
            otros.append(nombre)


def separador()->str:
    """_summary_
    Permite agregar una cadena de caracteres para separar el contenido en la terminal
    Returns:
        str: _cadena de caracteres: #*30_
    """
    print('#'*30)


def hacer_grandioso(l:list)->str:
    """_summary_
    Crea una nueva lista y agrega los elementos añadiendo 'El gran: ' a cada uno.
    finalmente imprime cada uno de los elementos con un salto de línea
    Args:
        l (list): _lista de strings_

    Returns:
        list: _lista modificada e impresa_
    """
    grandiosos = []
    for gran in l:
        grandiosos.append(f'El gran: {gran}')
    return "\n".join(grandiosos)


def imprimir_nombres(l:list)->str:
    """_summary_
    Imprime los datos de la lista ingresada separados por un salto de línea
    Args:
        l (list): _lista de str_

    Returns:
        str: _lista impresa_
    """
    return "\n".join(l)



separador()
separa_nombres(nombres)
print(imprimir_nombres(nombres))
separador()
print(f'    MAGOS GRANDIOSOS\n{hacer_grandioso(magos)}')
separador()
print(f'    CIENTIFICOS\n{imprimir_nombres(cientificos)}')
separador()
print(f'    Y COMPAÑIA\n{imprimir_nombres(otros)}')
