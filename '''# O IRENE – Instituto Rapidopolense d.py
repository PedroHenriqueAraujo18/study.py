'''# O IRENE – Instituto Rapidopolense de Estudos Naturais e Estatísticos,
# com sede em Rapodópolis, realiza mensalmente pesquisas de preços
# para avaliação mercadológica. Cada pesquisador comparece a 8
# estabelecimentos comerciais (supermercados, mercadinhos, pontos de
# vendas, atacadistas, ... ) e realiza a coleta de preços de um determinado
# produto. Você foi escolhido para desenvolver uma aplicação de software,
# em Python, para efetuar a leitura de dados coletados pelos
# pesquisadores, cadastrá-los em uma lista ou vetor ou matriz ou tupla ou
# dicionário – você deve definir uma opção de armazenamento e justificar
# a escolha, calcular o valor médio e, indicar o valor máximo e mínimo.

# supermercados, mercadinhos, pontos_de_venda, atacadista '''



dados = {}
maior = 0
menor = 999999
soma_preco = 0

while True:
    try:
        nome_mercado = input("Digite o nome do mercado: ")
        produto = input("Digite o nome do produto: ")
        preco = float(input("Digite um preço para o produto: "))
        
        if nome_mercado != "" and produto != "" and preco > 0:
            if produto in dados:
                dados[produto].append((nome_mercado, preco))
            else:
                dados[produto] = [(nome_mercado, preco)]
            
            if preco > maior:
                maior = preco
            if preco < menor:
                menor = preco 
            
            soma_preco += preco
        else:
            print("Valores vazios ou menores que zero")
    except ValueError:
        print("Valores inválidos")

    op = input("Digite 's' para realizar outro cadastro e 'n' para parar: ").upper()
    if op == 'N':
        break          

pesquisa = input("Deseja fazer uma pesquisa de algum produto (s/n)? ").upper()
if pesquisa == "S":
    while True:
        produto_pesquisar = input("Digite o nome do produto (x para sair): ")
        if produto_pesquisar.lower() == "x":
            break
        if produto_pesquisar in dados:
            encontrado = dados[produto_pesquisar] 
            if encontrado:
                menor_preco = float('inf')
                mercado_menor = ''
                maior_preco = float('-inf')
                mercado_maior = ''

                for mercado, preco in encontrado:
                    if preco < menor_preco:
                        menor_preco = preco
                        mercado_menor = mercado
                    if preco > maior_preco:
                        maior_preco = preco
                        mercado_maior = mercado

                print("Maior preço encontrado: R$ {:.2f} (Mercado: {})".format(maior_preco, mercado_maior))
                print("Menor preço encontrado: R$ {:.2f} (Mercado: {})".format(menor_preco, mercado_menor))
                print("Valor médio: R$ {:.2f}".format(soma_preco / len(encontrado)))