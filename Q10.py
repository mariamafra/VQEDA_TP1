def bubble_sort(lista):
    for i in range(len(lista)):
        for j in range(0, len(lista)-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

lista = ['a', 't', 'f', 'w', 'b']
print(bubble_sort(lista))
lista = ["banana", "laranja", "uva", "abacaxi", "maçã"]
print(bubble_sort(lista))