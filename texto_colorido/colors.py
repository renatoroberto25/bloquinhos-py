"""Closures e decorators no Python: uma função que cria funções"""


def term_text(color):
    """
    Cria função que retorna texto com instruções de formatação
    """

    def print_term(fn):
        """Decorador que gera texto colorido para Unix"""

        def preprocess_text(text):
            """Decorador para função"""
            return color + fn(text) + '\033[0m'

        return preprocess_text

    return print_term


# O terminal Unix usa caracteres especiais para determinar as cores
# da saída de texto.
#
# Aqui vamos definir algumas funções usando os caracteres de cor ANSI
# e nossa função geradora de decoradores
print_blue = term_text('\033[94m')
print_green = term_text('\033[92m')
print_yellow = term_text('\033[93m')
print_red = term_text('\033[91m')
print_bold = term_text('\033[1m')


def examples():
    """Coloca na tela alguns exemplos dos decoradores em uso."""

    programmer = input('Qual é o seu nome? ')

    # Aqui podemos ver como os decoradores funcionam.
    # É como passar para o print_blue, print_yellow etc as funções
    # Que definimos abaixo dos decoradores.
    @print_blue
    def say_hi_blue(name):
        return f'Oi em azul, {name}!'

    print(say_hi_blue(programmer))

    @print_yellow
    def say_hi_yellow(name):
        return f'Oi em amarelo, {name}!'

    print(say_hi_yellow(programmer))

    # Podemos usar mais de um decorador na mesma função.
    # No entanto, note que usar duas cores diferentes fará com que
    # apenas a primeira cor declarada tenha efeito.
    @print_bold
    @print_red
    def say_hi_bold_red(name):
        return f'Oi em vermelho negrito, {name}!'

    print(say_hi_bold_red(programmer))

    # Como usamos sintaxe de decorador, passar texto diretamente
    # é impossível. Para isso, podemos passar um lambda, como abaixo:
    colored_text_inline = print_green(lambda t: t)('Texto verde')
    print(colored_text_inline)

if __name__ == '__main__':
    examples()
