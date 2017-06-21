def desorden(lista):
i = 0
for character in lista:
    letra = list(lista[0])
    word = list(letra[0])
    contar = 0
    indice = 0
    for li in word:
        print word[i]
        if [word[indice]] <= [word[indice + 1]]:
            contar += 1
        indice += 1
    i += 1


if __name__ == "__main__":
    lista = []
    lectura(lista)
    desorden(lista)
