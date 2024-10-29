def ordenar_baralho(lista):
    mao_ordenada = []
    for i in lista:
        if i == 1:
            mao_ordenada.append(i)
            ultimo_elemento = mao_ordenada[-1]
        elif len(mao_ordenada) >= 1 and i == ultimo_elemento + 1:
            mao_ordenada.append(i)
            ultimo_elemento = mao_ordenada[-1]
        else:
            lista.append(i)

    return mao_ordenada

    

print(ordenar_baralho([3, 6, 1, 4, 8, 11, 2, 10, 5, 12, 7, 9, 13]))