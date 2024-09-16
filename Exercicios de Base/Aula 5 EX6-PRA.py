
dia=int(input("Digite o dia:"))
maior=menor=dia
while dia >1 and dia <31:
    dia=int(input("Digite o dia:"))
    if dia >1 and dia <31:
        T=0.011*(dia**3) - 0.3*(dia**2) + 0.04*dia
        if dia > maior:
            maior=dia
        if dia < maior:
            menor=dia
print("Menor=",menor)        
    
    
