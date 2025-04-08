a = int(input("digite um número:"))
if a > 0:
    print("número é positivo")
    print("valor:", a, "seu dobro:", a * 2)
elif a < 0:
    print("número negativo")
    print("valor:", a, "seu triplo:", a * 3)
else:
    print("número nulo")
    print("número digitado:", a)

