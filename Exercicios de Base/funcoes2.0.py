def inserirDict(D):
    while True:
        N = int(input("Digite quantos valores são necessários: "))
        if N > 0:
            break
        else:
            print("Quantidade inválida! Digite novamente.")
    for _ in range(N):
        codigo = int(input("Digite o código do livro: "))
        titulo = input("Digite o título: ")
        autores = AutoresInsere()
        preco = float(input("Digite o preço: "))
        D[codigo] = [titulo, autores, preco]
    return D

def AutoresInsere():
    autores = []
    while True:
        qtd = int(input("Digite quantos autores possui: "))
        if qtd > 0:
            break
        else:
            print("Quantidade inválida! Digite novamente.")
    for _ in range(qtd):
        autor = input("Digite o nome do autor: ")
        autores.append(autor)
    return autores

def main():
    D = {}
    D = inserirDict(D)
    for chave,valor in D.items():
        print(f"codigo = {chave}, titulo={valor[0]}, autores={valor[1]}, preço={valor[2]}")

main()
 