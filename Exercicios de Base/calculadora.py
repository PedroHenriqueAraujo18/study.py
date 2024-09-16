

#Funções
def multi(x,num):
    b=x*num
    return b

def soma(x,num):
    s=x+num
    return s
    
def div(x,num):
    z=x/num
    z=x%num
    return z
     
def sub(x,num):
    v=x-num
    return v
    
#menu    
chave=True   
   
#Main


try: 
    
    y=int(input("Digite um valor:"))
    m=int(input("Digite outro valor:"))

except:
    print("Digite valores númericos e valores acima de 0")
    y=int(input("Digite um valor:"))
    m=int(input("Digite outro valor:"))

   
print("{}-Somar".format(1))
print("{}-Divisão".format(2))       
print("{}-Multiplicar".format(3))
print("{}-Sub".format(4))
print("{}-Sair".format(5))


chave=int(input("Digite um do menu:"))
    
if chave == 1:
    s=soma(y,m)
    print("A soma é",s)
        
elif chave == 2:
    z=div(y,m)
    print("a Divisão e seu resto é ",z)
        
elif chave == 3:
    b=multi(y,m)
    print("A Multiplicação é",b)
        
elif chave == 4:
    v=sub(y,m)
    print("A Subtração é = ",v)
    
elif chave == 5:
    chave=False
        

while chave <1 or chave >5:
    print("Inválido")
    chave=int(input("Digite um do menu:")) 
        
    
