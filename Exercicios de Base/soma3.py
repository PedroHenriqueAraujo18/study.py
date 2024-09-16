c=0
cont=0
for soma in range(1,501,2):
    if soma%3==0:
        cont+=1
        c+=soma
       
        
        
print("soma de todos os {} valores é {}".format(c,cont))