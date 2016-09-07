"""Um vulcão acaba de entrar em erupção, provocando uma nuvem de cinzas que se alastra impedindo a circulação aérea.
O governo está muito preocupado e deseja saber quando que a nuvem de cinzas irá atingir todos os aeroportos do país.
Está disponível um mapa detalhando a situação atual. O mapa é retangular, dividido em pequenos quadrados.
Neste mapa existem três tipos de quadrados: nuvem (indicando que esta região do mapa já está coberto por nuvens),
aeroportos (indicando a localização de um aeroporto) e todas as outras (indicando locais onde a nuvem ainda não chegou).
A cada dia, a nuvem expande-se um quadrado na horizontal e um quadrado na vertical. Ou seja, ao fim de cada dia,
todos os quadrados adjacentes (vertical ou horizontalmente) a uma nuvem, também passam a conter nuvens. Por exemplo:

. . * . . . * *      . * * * . * * *     * * * * * * * *
. * * . . . . .      * * * * . . * *     * * * * * * * *
* * * . A . . A      * * * * A . . A     * * * * * . * *
. * . . . . . .  ->  * * * . . . . .  -> * * * * . . . .
. * . . . . A .      * * * . . . A .     * * * * . . A .
. . . A . . . .      . * . A . . . .     * * * A . . . .
. . . . . . . .      . . . . . . . .     . * . . . . . .
     Dia 0                Dia 1               Dia 2

Para preparar os planos de contingência, o governo necessita saber: quantos dias demorará para ao menos um aeroporto
ficar coberto pelas nuvens e daqui quantos dias todos os aeroportos estarão cobertos pelas nuvens.
Dados um quadriculado com L linhas e C colunas, além da indicação inicial das nuvens e dos aeroportos, desenvolva
uma programa que informe o número de dias até um primeiro aeroporto ficar debaixo da nuvem de cinzas e o número de dias
até que todos os aeroportos ficarem cobertos pelas cinzas."""

import copy


def nubecita(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])
    aeropuertos = cant_aeropuertos(matriz, linhas, colunas, 0)
    dias_total = 0
    dias_primer_aeropuerto = 1
    matriz_aux = copy.deepcopy(matriz)
    while aeropuertos > 0:
        matriz_aux = copy.deepcopy(avance(matriz_aux, linhas, colunas))
        if aeropuertos == cant_aeropuertos(matriz_aux, linhas, colunas, 0):
            dias_primer_aeropuerto += 1
        aeropuertos = cant_aeropuertos(matriz_aux, linhas, colunas, 0)
        dias_total += 1
    respuesta = [dias_primer_aeropuerto, dias_total]
    return respuesta


def cant_aeropuertos(matriz, linhas, colunas, aeropuertos):
    for l in range(0, linhas):
        for c in range(0, colunas):
            if matriz[l][c] == 'A':
                aeropuertos += 1
    return aeropuertos


def avance(matriz, linhas, colunas):
    matriz_aux = copy.deepcopy(matriz)
    for l in range(0, linhas):
        for c in range(0, colunas):

            if matriz[l][c] == '*':
                try:
                    matriz_aux[l][c + 1] = '*'
                except IndexError:
                    pass
                try:
                    if c > 0:
                        matriz_aux[l][c - 1] = '*'
                except IndexError:
                    pass
                try:
                    matriz_aux[l + 1][c] = '*'
                except IndexError:
                    pass
                try:
                    if l > 0:
                        matriz_aux[l - 1][c] = '*'
                except IndexError:
                    pass
    return matriz_aux


if __name__ == '__main__':
    matriz = [['.', '.', '*', '.', '.', '.', '*', '*'],
              ['.', '*', '*', '.', '.', '.', '.', '.'],
              ['*', '*', '*', '.', 'A', '.', '.', 'A'],
              ['.', '*', '.', '.', '.', '.', '.', '.'],
              ['.', '*', '.', '.', '.', '.', 'A', '.'],
              ['.', '.', '.', 'A', '.', '.', '.', '.'],
              ['.', '.', '.', '.', '.', '.', '.', '.']]

    assert nubecita(matriz) == [2, 4]
