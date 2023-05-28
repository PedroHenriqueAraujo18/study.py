livros={}

while True:
    codigo_livro=int(input("Digite o codigo do livro = (0 para parar)"))
    titulo=input("Nome do livro = ")
    if codigo_livro==0:
        break
    
autores=[]    
autores=int(input("Digite quantos autores = "))    


for i in range(autores):
    autor=input("Digite o nome do autor = ")
    autores.append(autor)
   
preço=float(input("Digite o preço do livro = "))  

livros[codigo_livro]=[titulo,autores,preço]  