"""Para definir uma seqüência a partir de um número inteiro o positivo, temos as seguintes regras:
n → n/2 (n é par)
n → 3n + 1 (n é ímpar)
Usando a regra acima e iniciando com o número 13, geramos a seguinte seqüência:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
Podemos ver que esta seqüência (iniciando em 13 e terminando em 1) contém 10 termos. Embora ainda não tenha sido
provado (este problema é conhecido como Problema de Collatz), sabemos que com qualquer número que você começar, a
seqüência resultante chega no número 1 em algum momento.
Desenvolva um programa que descubra qual o número inicial entre 1 e 1 milhão que produz a maior seqüência.
"""

def collatz(numero, contador):
    while numero != 1:
        contador += 1
        if numero % 2 == 0:
            numero /= 2
        else:
            numero = 3 * numero + 1
    return contador + 1

maximo = 0
numero = 0

for i in range(1, 1000001):
    contador = 0
    contador = collatz(i, contador)
    if maximo < contador:
        maximo = contador
        numero = i

print('El numero que produce la mayor sequencia es: {}, con una cantidad de {} elementos.'.format(numero, maximo))