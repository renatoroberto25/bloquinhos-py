import math
from collections import defaultdict
from random import shuffle


config = defaultdict(lambda: None)
config['LARGURA_DO_TEXTO'] = 70
config['RECUO_DE_PARÁGRAFO'] = 2


def linha():
    """Faz uma linha divisória."""
    return f'{"".join(["=" for each in range(0, config["LARGURA_DO_TEXTO"])])}\n'


def centralizar(texto):
    """Cria texto centralizado."""
    número_de_espaços = int(config["LARGURA_DO_TEXTO"] / 2) - int(math.ceil(len(texto) / 2))
    espaços = "".join([" " for each in range(0, número_de_espaços)])
    texto_centralizado = espaços + texto
    return texto_centralizado


def titulo(texto):
    """Formata um texto como título."""
    return f'{linha()}{centralizar(texto).upper()}\n{linha()}'


def parágrafo(texto):
    """Formata um parágrafo."""
    recuo = "".join(" " for each in range(0, config['RECUO_DE_PARÁGRAFO']))
    palavras = texto.split()

    linha_atual = recuo

    for palavra in palavras:
        nova_linha = f'{linha_atual}{palavra} '
        if len(nova_linha) <= config['LARGURA_DO_TEXTO']:
            linha_atual = nova_linha
        else:
            linhas.append(linha_atual)
            linha_atual = palavra + " "
    
    linhas.append(linha_atual.strip())

    resultado = "\n".join([linha for linha in processar_linhas(texto.split())])

    return resultado


def sim_ou_não(pergunta='', sim="Ss", não="Nn"):
    """Verifica uma resposta sim/não do usuário."""
    resposta = ""

    while not resposta or resposta not in sim + não:
        resposta = input(f"{pergunta} [{sim}/{não}] ")

    return resposta in sim


def receber_valor():
    """Determina valor do amigo secreto."""
    valor = 0
    while not valor:
        try:
            valor = int(input(("Qual é o valor máximo do amigo "
                               "secreto? (insira apenas números) ")))
        except ValueError:
            continue

    return valor


def receber_participantes():
    """Entrevista o usuário e recebe os nomes dos participantes."""
    participantes = []
    todos_os_participantes = False
    while not todos_os_participantes:
        participante = input("Participante(s): ")

        for part in participante.split(','):
            if part:
                participantes.append(part.strip())

        if sim_ou_não(pergunta="Ainda falta algum participante?"):
            continue
        todos_os_participantes = True

    return participantes


def criar_pares(participantes):
    """Cria pares para o Amigo Secreto."""
    participantes2 = list(participantes)

    i = 0
    while i < len(participantes):
        if participantes[i] == participantes2[i]:
            shuffle(participantes2)
            i = 0
        else:
            i += 1

    amigo_secreto = {}
    for part1, part2 in zip(participantes, participantes2):
        amigo_secreto[part1] = part2

    return amigo_secreto


def criar_mensagens(amigo_secreto, valor):
    """Cria as mensagens a serem enviadas para cada participante."""
    mensagens = {}
    for participante, amigo in amigo_secreto.items():
        mensagem = parágrafo(f"""Olá, {participante}!
                                 Seu amigo secreto é o(a) {amigo}. O valor
                                 máximo para gastar é de {valor} reais. Use o
                                 bom senso, e lembre-se: meias são úteis, mas
                                 nem sempre são bons presentes!""")
        mensagens[participante] = mensagem

    return mensagens


def main():
    """Ponto de entrada do programa."""
    print(titulo("Amigo secreto!"))

    print(parágrafo("""Olá! Sou um simples programa que pode te ajudar com a
                       organização de um amigo secreto. Só preciso fazer
                       algumas perguntas para podermos continuar."""))

    valor = receber_valor()

    print(parágrafo("""Certo. Agora, vou precisar saber o nome dos
                       participantes. Coloque todos aí, separados
                       por vírgula."""))

    amigo_secreto = criar_pares(receber_participantes())

    mensagens = criar_mensagens(amigo_secreto, valor)

    for participante, mensagem in mensagens.items():
        with open(f'{participante}.txt', 'w') as f:
            f.write(mensagem)


if __name__ == '__main__':
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        exit()
