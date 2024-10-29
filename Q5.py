def greatestNumber(array): 
    maior = array[0]

    for valor in array[1:]: 
        if maior < valor:
            maior = valor

    return maior
            

print(greatestNumber([1, 4, 2, 7, 12, 6, 9, 0]))