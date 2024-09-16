#MENU
import sys
menu=[2,3,4,5]
print(menu,end="")
mem=int(input("Digite uma opção :"))
for calc in range(1,2):
    num_1=float(input("Digite um valor:"))
    num_2=float(input("Digite um valor:"))


while mem  not in [2,3,4,5]:
    print("OPÇÃO INVÁLIDA")
    print("Digite uma opção do menu:",menu,end="")
    mem=input("Digite uma opção :")
else:
    if mem == 2:
        c=num_1*num_2
        print(c)
    
    elif mem == 3:
        d=num_1+num_2
        print(d)
    
    elif mem == 4:
    
        if num_1<num_2:
            print("o maior é o segundo")
        else:
            print("O maior é o primeiro")
    
    elif mem == 5:
       sys.exit("Saindo")
    
