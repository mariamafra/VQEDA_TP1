import math

def posicao_tabuleiro(quantidade):
    posicao = math.log(quantidade, 2) + 1
    return posicao

print(posicao_tabuleiro(1))
print(posicao_tabuleiro(2))
print(posicao_tabuleiro(4))
print(posicao_tabuleiro(8))
print(posicao_tabuleiro(16))
print(posicao_tabuleiro(32))