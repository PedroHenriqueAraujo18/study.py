print("="*100)


nome=input("Digite seu nome:")

iniciais=nome[0]

for index in range(1,len(nome)):
    if nome[index-1] == " " and nome[index].isupper():
        iniciais+=nome[index]
        

if iniciais.isupper():       
    print("Seu nome completo é {} e suas iniciais {}".format(nome,iniciais))
else:
    print("Nome sem inicial maiuscula")
print("="*100)