import math

#funções
def calc_Imc(peso,altura):
    imc=peso/math.pow(altura,2)
    return imc

def error(msg):
    print(msg)

def mensagem(msg):
    print("="*30)
    print(msg)
    print("="*30)

#programa principal   
mensagem("Calculadora de IMC")

nome=input("Digite seu nome: ")
altura=float(input("Digite sua altura: "))
peso=float(input("Digite seu peso: "))

while peso<0 or altura <0:
    error("Inválido,digite novamente")
    peso=float(input("Digite seu peso: "))
    altura=float(input("Digite sua altura: ")) 


mensagem("Escolha um para continuar")

escolha=input("Tem certeza dos valores digitados? S/N")

if escolha =="s":
    imc=calc_Imc(peso,altura)
    mensagem("{}. ,seu imc é {:.2f}".format(nome,imc))
    
elif escolha =="n":
    
    nome=input("Digite seu nome: ")
    peso=float(input("Digite seu peso: "))
    altura=float(input("Digite sua altura: "))  
    imc=calc_Imc(peso,altura)
    mensagem("{}. ,seu imc é {:.2f}".format(nome,imc))
    
while escolha not in "sn":
    error("Escolha inválida")
    escolha=input("Tem certeza dos valores digitados? S/N")
else:
    imc=calc_Imc(peso,altura)
    mensagem("{} ,seu imc é {:.2f}".format(nome,imc))
