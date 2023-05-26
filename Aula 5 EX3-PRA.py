n = int(input("Digite um valor n: "))
k = 1
x = int(input("Digite um valor: "))
M = m = x

while k < n:
    k += 1
    x = int(input("Digite um valor: "))
    if x > M:
        M = x
    if x < m:
        m = x

print("Maior {} e o menor {}".format(M, m))