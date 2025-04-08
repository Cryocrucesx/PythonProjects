ct =0
lnumber = []
print("digite [-1] para acabar com o loop:")
while True:
    x = int(input("digite um valor:"))
    if x == -1:
        break
    ct = ct + 1
    lnumber.append(x)
    qtd = len(lnumber)
print("quantidade de números:", qtd)
