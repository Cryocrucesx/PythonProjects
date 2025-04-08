ct = 0
list = 0
print("digite [-1] para sair:")
while True:
    a = int(input("digite um valor:"))
    if a == -1:
        break
    ct = ct + 1
    list = list + a
    mediaa = list / ct
print("quantidade de números digitados:", ct)
print("números somados:", list)
print("a média é:", mediaa)
