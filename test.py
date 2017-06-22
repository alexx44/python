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
      letra = list(lista[0])
      word = list(letra[0])
      contar = 0
      indice = 0
      indice2 = 0
      for li in word:
         print word[indice]
         if indice2 < (len(word) - 1):
            indice2 += 1
         print word[indice2]
         if [word[indice]] < [word[indice2]]:
            contar += 1
         indice += 1
         print contar
      i += 1   
     
  
   

if __name__ == "__main__":
   lista = []
   lectura(lista)
   desorden(lista)
   