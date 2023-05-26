inicial=int(input("Digite um valor para num :"))
final=int(input("Digite um valor para num_2 :"))
divisiveis = []
for num in range(inicial,final+1):
    if num%3==0:
        divisiveis.append(num)
print("Os números divisíveis por 3 no intervalo de", inicial, "a", final, "são:", divisiveis)