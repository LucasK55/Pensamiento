
  
def valoresRepetidos(lista):
    """devuelve lista con valores que aparecen mas de una vez"""
    repetidos = []
    i = 0
    while i < len(lista):
        j = i
        encontrado = False
        while j < len(lista):
            if lista[i] == lista[j] and i != j:
                encontrado = True
            j = j + 1
        if encontrado and lista[i] not in repetidos:
            repetidos.append(lista[i])
        i = i + 1
    return repetidos

def main():
    numeros = [4, 7, 2, 7, 5, 4, 9, 2, 1]
    resultado = valoresRepetidos(numeros)
    print(resultado)

main()