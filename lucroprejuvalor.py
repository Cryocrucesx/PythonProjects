a = float(input("digite o valor da compra:"))
c = str(input("digite o nome do produto:"))
b = float(input("digite o valor da venda:"))
if a < b:
    print(f"se obteve um lucro de:, {b - a:.2f}", "reais", "\tvalor da compra:", a, "\tvalor da venda:", b,
    "\nproduto:", c)
elif b < a:
    print("se obteve um prejuizo de:", a - b, "reais", "\tvalor da compra:", a, "\tvalor da venda:", b,
          "\nproduto:",c)
else:
    print("não obteve lucro nem prejuizos")
