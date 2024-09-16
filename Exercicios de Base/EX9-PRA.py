peso = float(input("Digite o seu peso em kg: "))
altura = float(input("Digite a sua altura em metros: "))

imc = peso / (altura ** 2)

if imc < 18.5:
    classificacao = "Abaixo do peso"
elif imc < 25:
    classificacao = "Peso normal"
elif imc < 30:
    classificacao = "Sobrepeso"
elif imc < 35:
    classificacao = "Obesidade grau 1"
elif imc < 40:
    classificacao = "Obesidade grau 2"
else:
    classificacao = "Obesidade grau 3"

print("Seu IMC é %.2f e sua classificação é: %s" % (imc, classificacao))