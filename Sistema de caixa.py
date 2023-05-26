# Define a senha de acesso ao sistema
senha = '1234'

# Solicita a senha para o usuário
senha_digitada = input('Digite a senha para acessar o sistema: ')

# Verifica se a senha está correta
while senha_digitada != senha:
    print('Senha incorreta.')
    senha_digitada = input('Digite a senha para acessar o sistema: ')
else:
    # Solicita o saldo inicial
    saldo_inicial = float(input('Digite o saldo inicial disponível no caixa: '))

    # Inicializa as variáveis de contagem
    num_vendas = 0
    num_itens = 0
    valor_total_vendas = 0
    saldo_atual = saldo_inicial

    # Loop principal do programa
    while True:
        # Exibe o menu de opções
        print('----------------------------------')
        print('MENU DE OPÇÕES:')
        print('1 - Registrar venda')
        print('2 - Adicionar dinheiro ao caixa')
        print('0 - Encerrar o programa')

        # Solicita a opção desejada
        opcao = input('Digite a opção desejada: ')
        while opcao != '1' or '2' or '0':
            print("Opção invalida")
            opcao = input('Digite a opção desejada: ')
        # Verifica a opção escolhida
        if opcao == '1':
            # Inicializa as variáveis de contagem para cada venda
            valor_venda = 0
            num_itens_venda = 0

            # Loop interno para registrar os produtos da venda
            while True:
                # Solicita as informações do produto
                preco_unitario = float(input('Digite o preço unitário do produto (0 para encerrar a venda): '))
                if preco_unitario == 0:
                    break
                quantidade = int(input('Digite a quantidade do produto: '))

                # Verifica se as informações são válidas
                if preco_unitario < 0 or quantidade <= 0:
                    print('Valor inválido. Tente novamente.')
                    continue

                # Atualiza o valor da venda e o número de itens
                valor_item = preco_unitario * quantidade
                valor_venda += valor_item
                num_itens_venda += quantidade
                num_itens += quantidade

            # Encerra a venda se nenhum produto foi registrado
            if num_itens_venda == 0:
                continue

            # Solicita o valor recebido
            valor_recebido = float(input('Digite o valor recebido: '))

            # Verifica se o valor recebido é válido
            if valor_recebido < valor_venda:
                print('Valor recebido insuficiente. Tente novamente.')
                continue

            # Calcula o troco e atualiza o saldo
            troco = valor_recebido - valor_venda
            saldo_atual += valor_venda

            # Atualiza as variáveis de contagem
            num_vendas += 1
            valor_total_vendas += valor_venda

            # Informa o troco ao usuário
            print('Troco: R$ {:.2f}'.format(troco))

        elif opcao == '2':
            # Solicita a quantia a ser adicionada ao caixa
            quantia = float(input('Digite a quantia a ser adicionada ao caixa: '))

            # Verifica se a quantia é válida
            while quantia <= 0:
                print('Valor inválido.A quantia deve ser maior que zero.')
                quantia = float(input('Digite a quantia a ser adicionada ao caixa: '))
            else:
                saldo_atual += quantia
                print('Saldo atualizado: R$ {:.2f}'.format(saldo_atual))