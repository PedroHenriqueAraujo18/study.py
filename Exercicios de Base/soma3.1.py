x=1
for b in range(1,2):
    if x > 0:
        x=int(input("Digite um valor positivo"))
    else:
        break


soma=1
cont=0
for c in range(1,x,1):
    if c%3 or 4:
        cont+=1
        soma=soma*c
print("O produto de todos os {} valores somado é {}".format(cont,soma))