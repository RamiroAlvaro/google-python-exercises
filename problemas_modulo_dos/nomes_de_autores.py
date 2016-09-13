"""
Quando se lista o nome de autores de livros, artigos e outras publicações é comum que se apresente o nome do autor
ou dos autores da seguinte forma: sobrenome do autor em letras maiúsculas, seguido de uma vírgula e da primeira parte
do nome apenas com as iniciais maiúsculas.
Por exemplo:
SILVA, Joao
COELHO, Paulo
ARAUJO, Celso de
Seu desafio é fazer um programa que leia um número inteiro correspondendo ao número de nomes que será fornecido, e,
a seguir, leia estes nomes (que podem estar em qualquer tipo de letra) e imprima a versão formatada no estilo
exemplificado acima.
As seguintes regras devem ser seguidas nesta formatação:
o sobrenome será igual a última parte do nome e deve ser apresentado em letras maiúsculas;
se houver apenas uma parte no nome, ela deve ser apresentada em letras maiúsculas (sem vírgula): se a entrada
for “ Guimaraes” , a saída deve ser “ GUIMARAES”;
se a última parte do nome for igual a "FILHO", "FILHA", "NETO", "NETA", "SOBRINHO", "SOBRINHA" ou "JUNIOR" e houver
duas ou mais partes antes, a penúltima parte fará parte do sobrenome. Assim: se a entrada for "Joao Silva Neto",
a saída deve ser "SILVA NETO, Joao" ; se a entrada for "Joao Neto" , a saída deve ser "NETO, Joao";
as partes do nome que não fazem parte do sobrenome devem ser impressas com a inicial maiúscula e com as
demais letras minúsculas;
"da", "de", "do", "das", "dos" não fazem parte do sobrenome e não iniciam por letra maiúscula.
"""
import re

ultima_parte = {'Filho', 'Filha', 'Neto', 'Neta', 'Sobrinho', 'Sobrinha', 'Junior'}
extra = {'da', 'de', 'do', 'das', 'dos'}


def autores(numero_de_nomes, nome, ultima_parte, extra):
    nomes = re.split(r'[\s]\s*', nome.lower())
    for i, nome in enumerate(nomes):
        if nome not in extra:
            nomes[i] = nome.capitalize()
    if numero_de_nomes == 1:
        nomes[0] = nomes[0].upper()
        nombre_formateado = nomes[0]
    elif nomes[-1] in ultima_parte and numero_de_nomes > 2:
        nomes[-1] = nomes[-1].upper()
        nomes[-2] = nomes[-2].upper()
        nombre_formateado = nomes[-2] + ' ' + nomes[-1] + ', ' + ' '.join(nomes[:-2])
    else:
        nomes[-1] = nomes[-1].upper()
        nombre_formateado = nomes[-1] + ', ' + ' '.join(nomes[:-1])
    return nombre_formateado

assert autores(1, 'Guimaraes', ultima_parte, extra) == 'GUIMARAES'
assert autores(3, 'Joao Silva Neto', ultima_parte, extra) == 'SILVA NETO, Joao'
assert autores(2, 'Joao Neto', ultima_parte, extra) == 'NETO, Joao'
assert autores(2, 'Joao Silva', ultima_parte, extra) == 'SILVA, Joao'
assert autores(2, 'Paulo Coelho', ultima_parte, extra) == 'COELHO, Paulo'
assert autores(3, 'Celso de Araujo', ultima_parte, extra) == 'ARAUJO, Celso de'
assert autores(4, 'Celso Paulo de Araujo', ultima_parte, extra) == 'ARAUJO, Celso Paulo de'
assert autores(5, 'Celso Paulo de Araujo Junior', ultima_parte, extra) == 'ARAUJO JUNIOR, Celso Paulo de'
