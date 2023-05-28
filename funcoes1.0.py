def lerValores(L, D):
    D = {}
    L = []
    N = int(input("Digite um valor para número de iterações: "))
    for i in range(N):
        ra = int(input("Digite o RA: "))
        nome = input("Digite o nome do estudante: ")
        aluno = [ra, nome]
        L.append(aluno)
        D[ra] = aluno
    return D

def inserçãoMaisElementos(L, D):
    ra = int(input("Digite o RA do aluno: "))
    nome = input("Digite o nome do aluno: ")
    aluno = [ra, nome]
    L.append(aluno)
    D[ra] = aluno

def removerAluno(L, D):
    ra = int(input("Digite o RA do aluno a ser removido: "))
    if ra in D:
        L.remove(D[ra])
        del D[ra]
    else:
        print("RA não encontrado!")

def main():
    L = []
    D = {}
    D = lerValores(L, D)
    while True:
        op = input("Deseja realizar outro cadastro? (s/n): ").upper()
        if op == 'S':
            inserçãoMaisElementos(L, D)
        else:
            print('Dicionário:', D)
            break

# Chamando a função principal
main()