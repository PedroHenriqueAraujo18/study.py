'''No IRCIRC – IInstituto RRapodopolense de CComputação o cálculo da nota final
de uma disciplina é efetuado com a ponderação das notas bimestrais
parciais. No semestre o aluno realiza duas provas (Prova1 e Prova2). A
média final é calculada ponderando os valores com os pesos Peso1 para a
prova 1 e Peso2 para a prova 2:'''

for pesos in range (1,2):
    peso1=float(input("Digite o valor para o peso da prova 1:"))
    peso2=float(input("Digite o valor para o peso da prova 2:"))
    prova1=float(input("Digite o quanto o aluno tirou na primeira prova:"))
    prova2=float(input("Digite o quanto o aluno tirou na segunda prova:"))

while peso1 <0:
    print("Valores inválidos")
    peso1=float(input("Digite o valor para o peso da prova 1"))

while peso2<0:
    print("Valores inválidos")
    peso2=float(input("Digite o valor para o peso da prova 2"))

while prova1<0:
    print("Valores inválidos")
    prova1=float(input("Digite o quanto o aluno tirou na primeira prova"))

while prova2<0:
    print("Valores inválidos")
    prova2=float(input("Digite o quanto o aluno tirou na segunda prova"))

else:
    print("BOLETIM DO ALUNO")
    media=(prova1*peso1)+(prova2*peso2)
    if media <5:
        print("REPROVADO")
    if media >=5:
        print("APROVADO")
    if media >=8 and media<9:
        print("PARABÉNS O DESEMPENHO FOI MUITO BOM")
    if media >=9:
        print("PARABÉNS, VOCÊ FOI APROVADO COM LOUVOR")
