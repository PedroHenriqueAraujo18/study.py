avaliacao1 = float(input("Digite a nota da Avaliação 1: "))
avaliacao2 = float(input("Digite a nota da Avaliação 2: "))
frequencia = float(input("Digite a porcentagem de presença do aluno nas atividades acadêmicas: "))

media = (avaliacao1 + avaliacao2) / 2

if frequencia < 75:
    print("Status de frequência: Reprovado")
    print("Status acadêmico: Reprovado")
elif media < 4:
    print("Status de frequência: Aprovado")
    print("Status acadêmico: Reprovado")
elif media < 6:
    print("Status de frequência: Aprovado")
    print("Status acadêmico: Exame")
elif media <= 10:
    print("Status de frequência: Aprovado")
    print("Status acadêmico: Aprovado")
else:
    print("Nota inválida.")