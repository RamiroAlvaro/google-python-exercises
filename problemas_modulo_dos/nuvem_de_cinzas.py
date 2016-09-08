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


def nuvem(mapa):
    linhas = len(mapa)
    colunas = len(mapa[0])
    aeroportos = aeroportos_cant(mapa, linhas, colunas, 0)
    dias_total = 0
    dias_primero_aeroporto = 1
    while aeroportos > 0:
        mapa, cant_aeroportos_act = (expande_se(mapa, linhas, colunas, aeroportos))
        if aeroportos == cant_aeroportos_act:
            dias_primero_aeroporto += 1
        if aeroportos > cant_aeroportos_act:
            aeroportos = cant_aeroportos_act
        dias_total += 1
    return str(dias_primero_aeroporto) + ' ' + str(dias_total)


def aeroportos_cant(mapa, linhas, colunas, aeroportos):
    for l in range(0, linhas):
        for c in range(0, colunas):
            if mapa[l][c] == 'A':
                aeroportos += 1
    return aeroportos


def expande_se(mapa, linhas, colunas, aeroportos):
    mapa_copy = copy.deepcopy(mapa)
    for l in range(0, linhas):
        for c in range(0, colunas):
            if mapa[l][c] == '*':
                try:
                    if mapa_copy[l][c + 1] == 'A':
                        aeroportos -= 1
                    mapa_copy[l][c + 1] = '*'
                except IndexError:
                    pass
                try:
                    if c > 0:
                        if mapa_copy[l][c - 1] == 'A':
                            aeroportos -= 1
                        mapa_copy[l][c - 1] = '*'
                except IndexError:
                    pass
                try:
                    if mapa_copy[l + 1][c] == 'A':
                        aeroportos -= 1
                    mapa_copy[l + 1][c] = '*'
                except IndexError:
                    pass
                try:
                    if l > 0:
                        if mapa_copy[l - 1][c] == 'A':
                            aeroportos -= 1
                        mapa_copy[l - 1][c] = '*'
                except IndexError:
                    pass
    return [mapa_copy, aeroportos]


if __name__ == '__main__':
    mapa = [['.', '.', '*', '.', '.', '.', '*', '*'],
              ['.', '*', '*', '.', '.', '.', '.', '.'],
              ['*', '*', '*', '.', 'A', '.', '.', 'A'],
              ['.', '*', '.', '.', '.', '.', '.', '.'],
              ['.', '*', '.', '.', '.', '.', 'A', '.'],
              ['.', '.', '.', 'A', '.', '.', '.', '.'],
              ['.', '.', '.', '.', '.', '.', '.', '.']]

    assert nuvem(mapa) == '2 4'
