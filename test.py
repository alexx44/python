def lectura(lista):
   entrada = open("entrada.txt")
   cantidad = entrada.readline()
   cantidad = int(cantidad)
   i = 0
   while i <= cantidad:
      linea = entrada.readline()
      linea = linea.split("\n")
      lista.append(linea)
#      print(lista[i])
      i = i + 1
   entrada.close()
   
def desorden(lista):
   i = 0
   for character in lista:
      letra = list(lista[i])
      word = list(letra[0])
      print word
      i = i + 1
      

   
   

if __name__ == "__main__":
   lista = []
   lectura(lista)
   desorden(lista)
   