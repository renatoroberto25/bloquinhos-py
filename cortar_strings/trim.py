# Conforme a dúvida que vimos hoje no grupo, vamos criar uma função
# que corta os espaços e newlines em excesso de uma string.
#
# Vamos usar a string abaixo como objeto de estudo:

teststr = """
        esta     string

        tem   espaços


    e 



newlines em        excesso"""

# Os newlines são representados pelo metachar '\n'. Temos dois
# objetivos: remover as sequências infinitamente longas de ' ' e de
# '\n', substituindo-as por uma única repetição de ' ' ou '\n'.

# O método str.split corta uma string e retorna uma lista com as
# sequências de caracteres contidas entre os caracteres fornecidos.

# Cada item da lista é uma sequência de caracteres
# entre o argumento do split (que foi um espaço) contida na nossa
# string de estudo.

# As sequências vazias indicam onde havia espaços desnecessários, já
# que uma string vazia siginifica que não havia nada entre dois espaços
# e portanto havia um espaço em excesso.

# Para reconstruir a string sem espaços em excesso, precisamos retirar
# as strings vazias dessa lista. Isso será feito com uma comprehension:

no_spaces = [word for word in teststr.split(' ') if len(word) > 0]
#            ^                ^                  ^
#   crie um item para cada    |                  |
#                        nesta lista             |
#                             mas só se a palavra for mais longa que 0

# Agora precisamos transformar essa lista de volta em string,
# e colocar um espaço entre cada sequência que extraímos.

# Vamos ver como fazer isso com str.join:

nospacestr = ' '.join(no_spaces)
#           ^
#  junte com " " (um espaço) cada item em no_spaces

# Agora a string tem apenas um espaço entre cada palavra.
# Vamos repetir o processo sem muita explicação, com '\n' em vez de ' '

no_newlines = [line for line in nospacestr.split('\n') if line]
#                                                         ^
#                             em vez de testar o cumprimento da string,
#                               podemos testar a string diretamente, já
#                                   que uma string vazia retorna falso.

result = '\n'.join(no_newlines)

# Agora nossa string tem apenas o necessário em espaços e newlines.
# No entanto, tratamos os newlines como palavras, e separamos eles com
# espaços. Por isso, tem um espaço no começo de cada linha.

# Vamos voltar para a etapa no_newlines. Quando criamos a lista sem
# as "palavras vazias", podemos remover os espaços no começo e no final
# com str.strip:

no_newlines = [line.strip() for line in nospacestr.split('\n') if line]

result = '\n'.join(no_newlines)

print(result)

# Vamos construir uma função que não nos obrigue a repetirmos as
# instruções (afinal, somos programadores ou professores?)

def fix_string(string):
    rm_spaces = [word for word in string.split(' ') if word]
    only_one_space = " ".join(rm_spaces)
    rm_newlines = [ln.strip() for ln in only_one_space.split('\n') if ln]
    only_one_newline = "\n".join(rm_newlines)
    return only_one_newline

# Vamos testar com a string "bugada", lá do começo
print(fix_string(teststr))  

# Deu certo! Yay!
