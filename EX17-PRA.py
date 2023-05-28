'''O Departamento de Trânsito de Rapidópolis
está realizando uma campanha para orientar
os proprietários de veículos quanto à data de
pagamento do IPVA. Você foi contratado
para desenvolver um algoritmo e efetuar a
implementação em Python, para ler o último
dígito da placa do veículo, o mês corrente e
escrever o mês de pagamento do imposto,
mas se o mês corrente for superior ao m6es
de pagamento, deve-se emitir uma
mensagem informando que o pagamento
PLACA MÊS PAGAMENTO IPVAPLACA MÊS PAGAMENTO IPVA
Final 1 – mês (1) – Janeiro
Final 2 – mês (2) – Fevereiro
Final 3 – mês (3) – Março
Final 4 – mês (4) – Abril
Final 5 – mês (5) – Maio
Final 6 – mês (6) – Junho
Final 7 – mês (7) – Julho
Final 8 – mês (8) – Agosto
Final 9 – mês (9) – Setembro
Final 0 – mês (10) – Outubro
mensagem informando que o pagamento
está em atraso.'''

for  placa in range(1,2):
    placa=int(input("Digite sua placa:"))
    mes=int(input("Digite o mês corrente "))
    mes_pag=int(input("Digite o mes de pagamento:"))
    

    print("MES DE PAGAMENTO")    
    if  placa == 1:
        print("Janeiro")
    elif  placa == 2:
        print("Fevereiro")
    elif  placa == 3:
        print("Março")    
    elif  placa == 4:
        print("Abril")    
    elif  placa == 5:
        print("Maio")    
    elif  placa == 6:
        print("Junho")    
    elif  placa == 7:
        print("Julho")    
    elif  placa == 8:
        print("Agosto")
    elif  placa == 9:
        print("Setembro")  
    else:
        print("Outubro")          
        
        
if mes > mes_pag:
    print("Seu pagamento de IPVA está atrasado")