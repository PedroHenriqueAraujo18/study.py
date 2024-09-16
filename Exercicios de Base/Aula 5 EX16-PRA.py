import random

# Definindo as opções de jogada
opcoes = ["pedra", "papel", "tesoura"]

# Inicializando a pontuação do jogador e do computador
pontuacao_jogador = 0
pontuacao_computador = 0

# Loop principal do jogo
while True:
    # Lendo a jogada do usuário
    jogada_usuario = input("Digite a sua jogada (pedra, papel ou tesoura): ")

    # Verificando se a jogada do usuário é válida
    if jogada_usuario not in opcoes:
        print("Jogada inválida. Tente novamente.")
        continue

    # Convertendo a jogada do usuário para um número
    jogada_usuario_num = opcoes.index(jogada_usuario)

    # Gerando a jogada do computador aleatoriamente
    jogada_computador_num = random.randint(0, 2)

    # Convertendo a jogada do computador para uma string
    jogada_computador = opcoes[jogada_computador_num]

    # Exibindo a jogada do computador
    print("O computador jogou", jogada_computador)

    # Verificando quem ganhou
    if jogada_usuario_num == jogada_computador_num:
        print("Empate!")
    elif (jogada_usuario_num - jogada_computador_num) % 3 == 1:
        print("Você ganhou!")
        pontuacao_jogador += 1
    else:
        print("O computador ganhou!")
        pontuacao_computador += 1