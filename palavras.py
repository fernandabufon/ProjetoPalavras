import numpy as np
import string
from random import choice
def main():
    p, arr, o, g, a, c, m = variaveis()
    arr = palavras(p, arr, o, g, a, c, m)
    resp = np.array(arr)
    imprimir(arr)
    resposta(resp)


def variaveis():
    p = "programacao"
    arr = np.array([['-'] * 8] * 11)  # criando uma matriz com 8 colunas e 11 linhas
    o = "oracle"
    g = "google"
    a = "apache"
    c = "cisco"
    m = "meta"
    return p, arr, o, g, a, c, m

def palavras(p, arr, o, g, a, c, m):
    for pos, char in enumerate(p):
        arr[pos, 1] = char
    for pos, char in enumerate(o):
        arr[10, (pos + 1)] = char
    for pos, char in enumerate(g):
        arr[3, (pos + 1)] = char
    for pos, char in enumerate(a):
        arr[5, (pos + 1)] = char
    for pos, char in enumerate(m):
        arr[6, (pos + 1)] = char
    for pos, char in enumerate(c):
        arr[8, (pos + 1)] = char
    return arr

def gerar_letras(arr):
    for l in range(0, 11):
        for c in range(0, 8):
            if arr[l, c] == '-':
                arr[l, c] = choice(string.ascii_letters).lower()
    return arr

def imprimir(arr):
    print(gerar_letras(arr))

def resposta(resp):
    while True:
        r = str(input("\nDigite R para obter a resposta: ")).upper()
        if r=='R':
            print(resp)
            break

if __name__ == '__main__':
    main()
