media = 0
cont = 0
n = int(input("Digite um valor para N: "))
while n > 0:
    cont += 1
    media += n
    n = int(input("Digite um valor para N: "))
   
if cont > 0:
    media /= cont
    print("O valor médio dos números digitados foi {:.2f}".format(media))
else:
    print("Nenhum número foi digitado.")