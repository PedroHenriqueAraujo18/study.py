import random


opcoes = ["pedra", "papel", "tesoura"]


jogada_usuario = input("Digite a sua jogada (pedra, papel ou tesoura): ")


if jogada_usuario not in opcoes:
    print("Jogada inválida. Tente novamente.")
else:
  
    jogada_usuario_num = opcoes.index(jogada_usuario)

  
    jogada_computador_num = random.randint(0, 2)

   
    jogada_computador = opcoes[jogada_computador_num]

   
    print("O computador jogou", jogada_computador)

    
    if jogada_usuario_num == jogada_computador_num:
        print("Empate!")
    elif (jogada_usuario_num - jogada_computador_num) % 3 == 1:
        print("Você ganhou!")
    else:
        print("O computador ganhou!")