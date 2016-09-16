"""
Este problema foi utilizado em 106 Dojo(s).
Escreva um programa em que dado uma frase e a quantidade de colunas que podem ser exibidas na tela, faça a quebra de
linhas sem quebrar as palavras.
Por exemplo, se passarmos a frase "Um pequeno jabuti xereta viu dez cegonhas felizes." e pedirmos para ela ser exibida
em 20 colunas, teremos como resposta:
Um pequeno jabuti
xereta viu dez
cegonhas felizes.
"""
import textwrap

text = 'Um pequeno jabuti xereta viu dez cegonhas felizes.'
result = textwrap.fill(text, 20)

assert result == 'Um pequeno jabuti\nxereta viu dez\ncegonhas felizes.'

print(result)