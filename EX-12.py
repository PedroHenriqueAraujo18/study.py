x = float(input("Digite o valor de x: "))

if x == 0:
    print("Erro: não é permitida a divisão por zero.")
else:
    resultado = 4 * x ** 2 - 3 * x + 9 / x
    print("O valor de f(x) é:", resultado)