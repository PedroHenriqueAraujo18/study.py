import random

numero=random.randint(0,100)

desistir=True

numeroDigitado=-1

tentativas=0

while numeroDigitado!=numero:
    try:
        tentativas+=1
        if tentativas >10:
            desistir=input("Dejesa parar?S/N")
            if desistir =="S":
              numeroDigitado=int(input("Digite um valor:"))  
        numeroDigitado=int(input("Digite um valor:"))
        if numeroDigitado>numero:
            print("Numero maior que o do computador")
        elif numeroDigitado<numero:
            print("Numero menor que o do computador")
        else:
            print("Numero correto")
            print("Tentativas = ",tentativas)
    except:
        print("Utilize somente valores númericos")