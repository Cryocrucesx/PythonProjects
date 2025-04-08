a = int(input("digite o primeiro valor:"))
b = int(input("digite o segundo valor:"))
if a > b:
    print("maior valor:", a, "\tem ordem decrescente:", b,"e",a)
elif b > a:
    print("maior valor", b, "\tem ordem decrescente:", a,"e",b)
else:
    print("os valores são igauis", "primeiro valor:", a, "segundo valor:", b)

