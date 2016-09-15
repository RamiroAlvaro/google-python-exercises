"""
Este problema foi utilizado em 401 Dojo(s).
A cada 4 anos, a diferença de horas entre o ano solar e o do calendário convencional completa cerca de 24 horas
(mais exatamente: 23 horas, 15 minutos e 864 milésimos de segundo). Para compensar essa diferença e evitar um
descompasso em relação às estações do ano, insere-se um dia extra no calendário e o mês de fevereiro fica com 29 dias.
Essa correção é especialmente importante para atividades atreladas às estações, como a agricultura e até mesmo as
festas religiosas.
Um determinado ano é bissexto se:
O ano for divisível por 4, mas não divisível por 100, exceto se ele for também divisível por 400.
Exemplos:
São bissextos por exemplo:
1600
1732
1888
1944
2008
Não são bissextos por exemplo:
1742
1889
1951
2011
Escreva uma função que determina se um determinado ano informado é bissexto ou não.

"""


def bissexto(ano):
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        text = 'bissexto'
    else:
        text = 'não bissexto'
    return text


assert bissexto(1600) == 'bissexto'
assert bissexto(1732) == 'bissexto'
assert bissexto(1888) == 'bissexto'
assert bissexto(1944) == 'bissexto'
assert bissexto(2008) == 'bissexto'

assert bissexto(1742) == 'não bissexto'
assert bissexto(1882) == 'não bissexto'
assert bissexto(1951) == 'não bissexto'
assert bissexto(2011) == 'não bissexto'
