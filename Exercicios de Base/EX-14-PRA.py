'''O Prof. Arcaxerxes Panturrilha deseja verificar se os seus alunos estão
escrevendo as datas de forma correta. Assim, solicitou a você que
desenvolva um algoritmo e efetue a implementação em Python para ler o
dia, mês e ano verificando a consistência dos dados, por exemplo, se o
mês está entre 1 e 12, se os dias estão entre 1 e 28, 30 ou 31 dias, de
acordo com o mês correspondente e verifique se o ano é bissexto.'''

# Função para verificar se o ano é bissexto
def bissexto(ano):
    if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
        return True
    else:
        return False

# Entrada do usuário
dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano: "))

# Verificação da consistência dos dados
if mes < 1 or mes > 12:
    print("Mês inválido!")
elif mes == 2:
     if bissexto(ano):
        if dia < 1 or dia > 29:
            print("Dia inválido!")
        elif dia < 1 or dia > 28:
            print("Dia inválido!")
        elif mes in [4, 6, 9, 11]:
            if dia < 1 or dia > 30:
                print("Dia inválido!")
        elif dia < 1 or dia > 31:
            print("Dia inválido!")
else:
    print("Data válida!")