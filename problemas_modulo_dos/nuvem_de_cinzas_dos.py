"""La solucion de Henrique Bastos
 Curti d+ esse puzzle! Meu primeiro impulso também foi fazer um "simulador" que atualiza cada mapa.
 O enunciado do problema induz a esse pensamento ao mostrar a evolução do mapa.

No entanto, lendo atentamente eu vi que o objetivo é descobrir:

1.Quantos dias leva para o 1º aeroporto ser atingido.
2.Quantos dias leva para todos os aeroportos serem atingidos.
Isso muda completamente a abordagem e aí eu parei pra rabiscar.
O papel e lápis me mostraram o que eu já imaginava: Eu estava complicando o problema. :smiley:

Até que notei que esse era um problema de distância entre pontos, mas com a restrição de não existir diagonal. Então em vez de calcular a hipotenusa eu vi que bastava somar o cumprimento dos catetos.

Validei uns 3 casos na mão e vi que funcionava. Então parti pro código que contém 3 partes:

1.Montagem do mapa a partir do texto;
2.A identificação dos aeroportos e as nuvens;
3.O calculo da distância de cada aeroporto até cada nuvem;
4.A montagem de um relatório para o governo;


"""

from textwrap import dedent

# Text map representation for Day 0
D0 = """
     . . * . . . * *
     . * * . . . . .
     * * * . A . . A
     . * . . . . . .
     . * . . . . A .
     . . . A . . . .
     . . . . . . . .
     """


def grid(textmap):
    '''
    Build a grid from text map representation.
    Returns list of lists.
    '''
    textmap = dedent(textmap)
    textmap = textmap.strip()

    return [line.split(' ') for line in textmap.split('\n')]


def find(grid, item):
    '''Find coordinates (row, col) for all ocurrences of item on the grid.'''
    found = []

    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell == item:
                found.append((r, c))

    return found


def orthogonal_distance(a, b):
    '''Return the orthogonal distance between 2 (row, col) coordinates.'''
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def day_for_impact(airport, clouds):
    '''How many days for impact an airport?'''
    return min(orthogonal_distance(airport, cloud) for cloud in clouds)


def prediction(airports, clouds):
    '''Returns the first and last day of impact for all airports.'''
    first_day, *_, last_day = sorted(day_for_impact(ap, clouds) for ap in airports)

    return first_day, last_day


# Tests
assert grid(D0)[0] == ['.', '.', '*', '.', '.', '.', '*', '*']

assert find(grid(D0), 'A') == [(2, 4), (2, 7), (4, 6), (5, 3)]

assert orthogonal_distance((2, 4), (2, 2)) == 2
assert orthogonal_distance((2, 4), (0, 6)) == 4
assert orthogonal_distance((4, 6), (2, 2)) == 6


# Main
def report(textmap):
    '''Run the report for the President.'''

    map_ = grid(textmap)
    airports = find(map_, 'A')
    clouds = find(map_, '*')

    letter = dedent("""
             Mr. President,
             Our first airport will be hit in {0} days.
             In {1} days will have no more airports available.
             We are doomed!""")
    return letter.format(*prediction(airports, clouds))


print(report(D0))