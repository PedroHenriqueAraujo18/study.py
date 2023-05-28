'''Desenvolver um algoritmo e efetuar a implementação
em Python, para ler dois números e informar se o
primeiro é divisível pelo segundo.
(NESTE CASO O RESTO DA DIVISÃO DEVE SER ZERO)'''

for x in range (1,2):
    x=int(input("Digite um valor:"))
   
for y in range(1,2):
    y=int(input("Digite outro valor:"))

if x%y==0:
        print("{}/{} da resto zero, ou seja é o primeiro e divisível pelo segundo".format(x,y))
else:
    print("{}/{} não da resto zero,ou seja é o primeiro  não é divisível pelo segundo".format(x,y))
