alunos={}

while True:
    try:
        aluno=int(input("Adicione a quantidade de alunos= "))
        if aluno > 0:
            break
    except ValueError:
        print("Valor menor que zero, ou valor não inteiro")
        
for i in range(aluno):
    try:
        matricula=int(input("Digite o número da marícula do aluno = "))
        nome=input("Digite o nome do aluno = ")
        if matricula in alunos.keys():
            print("Matricula ja existente")
        else:
            alunos[matricula]=[nome]
    except ValueError:
        print("Valor inválido")

pesquisa=int(input("Digite um número de matrícula"))
for matricula,nome in alunos.items():
    if pesquisa == matricula:
        print(f'matricula = {matricula}: nome={nome}')
    if pesquisa != matricula:
        print("Não encontrado")