'''15) O BaRCoBaRCo - BaBanco de RRapidópolis CoCorp contratou você para desenvolver
um algoritmo e efetue a implementação em Python para preencher os
formulários da Instituição:
• Efetuar a leitura de um número inteiro entre
$$ $$$$$$$$$$$$ • Efetuar a leitura de um número inteiro entre
0 e 9 e escrever o valor por extenso.
• Efetuar a leitura de um número inteiro entre
0 e 99 e escrever o valor por extenso.
• Efetuar a leitura de um número inteiro entre
0 e 999 e escrever o valor por extenso.'''

def numero_por_extenso(num):
    unidades = ['', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove']
    dezenas = ['', 'dez', 'vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa']
    centenas = ['', 'cento', 'duzentos', 'trezentos', 'quatrocentos', 'quinhentos', 'seiscentos', 'setecentos', 'oitocentos', 'novecentos']
    if num == 0:
        return 'zero'
    elif num < 10:
        return unidades[num]
    elif num < 20:
        dez = num % 10
        if dez == 1:
            return 'onze'
        elif dez == 2:
            return 'doze'
        elif dez == 3:
            return 'treze'
        elif dez == 4:
            return 'quatorze'
        elif dez == 5:
            return 'quinze'
        elif dez == 6:
            return 'dezesseis'
        elif dez == 7:
            return 'dezessete'
        elif dez == 8:
            return 'dezoito'
        elif dez == 9:
            return 'dezenove'
    elif num < 100:
        dez = num // 10
        uni = num % 10
        if uni == 0:
            return dezenas[dez]
        else:
            return dezenas[dez] + ' e ' + unidades[uni]
    elif num < 1000:
        cen = num // 100
        dez = (num % 100) // 10
        uni = num % 10
        if dez == 0 and uni == 0:
            return centenas[cen]
        elif dez == 0:
            return centenas[cen] + ' e ' + unidades[uni]
        else:
            return centenas[cen] + ' e ' + dezenas[dez] + ' e ' + unidades[uni]


num = int(input('Digite um número entre 0 e 999: '))
print(numero_por_extenso(num))