def lectura(lista):
    archivo = open("entrada.txt")
    cantidad = archivo.readline()
    cantidad = int(cantidad)
    i = 0
    while i < cantidad:
        linea = archivo.readline()
        linea = linea.rsplit("\n")
        lista.append(linea)
        i = i + 1
    archivo.close()
    return archivo


def desorden(cadena):
    valor = 5
    return valor

def proceso(lista):
    return nueva


def ordena(nueva):
    pass


if __name__ == "__main__":
    lista = []
    lectura(lista)
    #n = desorden(lista[])
    #print n, lista[]



