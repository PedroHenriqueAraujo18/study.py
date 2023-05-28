n=0
cont_idade=0
soma_media=0
while True:
    idade=int(input("Digite seu numero, digite 0 para parar"))
    
    if idade == 0:
        break
    n+=1    
    cont_idade+=idade
    soma_media+=idade

if n>0:
    media=cont_idade/n
    print("Média",media)
    
else:
    print("Nada foi digitado")
