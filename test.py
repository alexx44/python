def lectura(lista):
   entrada = open("entrada.txt")
   cantidad = entrada.readline()
   cantidad = int(cantidad)
   i = 0
   while i <= cantidad:
      linea = entrada.readline()
      linea = linea.rsplit("\n")
      lista.append(linea)
      print(linea)
      i = i + 1
   entrada.close()
   

if __name__ == "__main__":
   lista = []
   lectura(lista)
   