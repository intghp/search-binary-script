def busca_binaria(lista, item):
    indice_baixo = 0
    indice_alto = len(lista) - 1
    tentativas = 0

    while indice_baixo <= indice_alto:
        indice_meio = (indice_baixo + indice_alto) // 2
        valor_meio = lista[indice_meio]
        tentativas += 1

        if valor_meio == item:
            return indice_meio, tentativas
        elif valor_meio < item:
            indice_baixo = indice_meio + 1
        else:
            indice_alto = indice_meio - 1
    return -1, tentativas

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
item = 7
indice, tentativas = busca_binaria(lista, item)

print(f"O item {item} está no índice {indice} com {tentativas} tentativas")
