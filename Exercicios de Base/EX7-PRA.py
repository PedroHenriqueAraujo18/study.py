'''No Brasil a unidade para aferição de temperatura é o grau Celsius oC, mas
pode-se utilizar outras escalas, como o Fahrenheit (utilizada em países de
língua inglesa), Kelvin, Rankine (em algumas áreas da Engenharia nos
Estados Unidos) e Réaumur e muitas outras que estão em desuso (como
Rφmer, Newton e Delisle)'''



while True:
    print("Escolha uma unidade de temperatura: Kelvin, Réaumur, Rankine, Fahrenheit")
    escolha = input().lower()

    if escolha == "kelvin":
        print("TABELA DO KELVIN")
        kelvin=float(input("Digite o valor para kelvin: "))
        C_1=kelvin-273.15
        print("{} Kelvin em Celsius é {}".format(kelvin,C_1))
    

    elif escolha == "rankine":
        print("TABELA DO RANKINE")
        rankine=float(input("Digite o valor para Rankine:"))
        C_2=5*rankine - 273.15/9
        print("{} Rankines em Celsius é {}".format(rankine,C_2))

    elif escolha == "réaumur":
        print("TABELA DO RÉAUMUR")
        réaumur=float(input("Digite o valor para Réaumur:"))
        C_3=5*réaumur/4
        print("{} Réaumures em Celsius é {}".format(réaumur,C_3))

    elif escolha == "fahrenheit":
        print("TABELA DO FAHRENHEIT")
        fahrenheit=float(input("Digite o valor para Fahrenheit:"))
        C_4=5*(fahrenheit-32)/9
        print("{} Fahrenheit em Celsius é {}".format(fahrenheit,C_4))
    else:
        print("Escolha inválida. Por favor, tente novamente.")