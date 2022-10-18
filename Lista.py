lista = [4, 1, 3, 5, 2]
n = len(lista)
for i in range(n):
    for j in range(n - i - 1):
        if lista [j] > lista[j + 1] :
            aux = lista[j]
            lista[j] = lista[j + 1]
            lista[j + 1] = aux
print(lista)
