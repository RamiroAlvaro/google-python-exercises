"""
Este problema foi utilizado em 111 Dojo(s).
Definimos dois vetores A e B de dimensão n em termos de componentes como:
A = (a1, a2, a3, ..., an) e B = (b1, b2, b3, ..., bn)
O produto escalar entre esses vetores é descrito como:
A . B = a1 * b1 + a2 * b2 + a3 * b3 + ... + an * bn
Desenvolva um programa que, dado dois vetores de dimensão n, retorne o produto escalar entre eles.

"""

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
c = [3, 5, 7, 9]
d = [2, 4, 6, 8]
f = [40, 41, 42, 43, 44]
g = [1.5, 1.6, 1.7, 1.8, 1.9]


def produto_escalar(vetor_a, vetor_b):
    result = 0
    for x, y in zip(vetor_a, vetor_b):
        result += x * y
    return result


assert produto_escalar(a, b) == 935
assert produto_escalar(c, d) == 140
assert produto_escalar(f, g) == 358
