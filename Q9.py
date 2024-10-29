def bubble_sort(lista):
    for i in range(len(lista)):
        for j in range(0, len(lista)-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    
    return lista

lista = [6, 3, 8, 2, 5, 8]
print(bubble_sort(lista))
lista = [43.6, 34.9, 12.7, 98.0, 43.9]
print(bubble_sort(lista))
lista = [-1, -50, -23, -54, -3]
print(bubble_sort(lista))
lista = [4.9, 2, 87, -1, 4.8, -76]
print(bubble_sort(lista))