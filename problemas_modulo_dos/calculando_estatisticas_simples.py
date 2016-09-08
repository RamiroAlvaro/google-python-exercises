"""Sua tarefa é processar uma seqüência de números inteiros para determinar as seguintes estatísticas:
Valor mínimo
Valor máximo
Número de elementos na seqüência
Valor médio
Por exemplo para uma seqüência de números "6, 9, 15, -2, 92, 11", temos como saída:
Valor mínimo: -2
Valor máximo: 92
Número de elementos na seqüência: 6
Valor médio: 21.83333"""


def estadistica(lista):
    minimo = min(lista)
    maximo = max(lista)
    elementos = len(lista)
    valor_medio = float(format(sum(lista) / len(lista), '0.5f'))
    return [minimo, maximo, elementos, valor_medio]


lista_1 = [6, 9, 15, -2, 92, 11]
lista_2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
lista_3 = [1]
lista_4 = [-3, -4, -70, 66, -99999, 1.03, 42, 40, 0.123]

assert estadistica(lista_1) == [-2, 92, 6, 21.83333]
assert estadistica(lista_2) == [0, 0, 10, 0.00000]
assert estadistica(lista_3) == [1, 1, 1, 1.00000]
assert estadistica(lista_4) == [-99999, 66, 9, -11102.98300]
