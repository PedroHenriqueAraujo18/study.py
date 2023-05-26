ano_construcao = int(input("Digite o ano de construção do imóvel: "))
ano_atual = int(input("Digite o ano atual: "))

idade_imovel = ano_atual - ano_construcao

if idade_imovel < 5:
    percentual_desconto = 0
elif idade_imovel >= 5 and idade_imovel < 20:
    percentual_desconto = 15
elif idade_imovel >= 20 and idade_imovel < 40:
    percentual_desconto = 25
else:
    percentual_desconto = 30

valor_iptu = float(input("Digite o valor do iptu:"))
while valor_iptu <0:
    valor_iptu = float(input("Digite o valor do iptu:"))

valor_com_desconto = valor_iptu - (valor_iptu * percentual_desconto / 100)

print("O valor do IPTU com desconto é R$ %.2f" % valor_com_desconto)