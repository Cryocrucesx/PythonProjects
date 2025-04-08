ct = 0
b = 0
print("digite [-1] para sair:")
while True:
    number = int(input("digite um número:"))
    if number == -1:
        break
    ct = ct + 1
    b = b + number
print("quantidade de números digitados:", ct)
print("soma dos número digitados", b)