soma=0
cont=0
for c in range(1,7,1):
    numero=float(input("Digite um valor:"))
    if numero%2==0:
        cont+=1
        soma+=numero
        
print("A soma de todos os {} pares é {}".format(cont,soma))        