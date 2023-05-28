inicio = int(input("Digite o valor inicial do intervalo: "))
fim = int(input("Digite o valor final do intervalo: "))
divisor = int(input("Digite o número para indicar a divisibilidade: "))


for i in range(inicio, fim+1):
    if i % divisor == 0:
        print(i, "é divisível por", divisor)