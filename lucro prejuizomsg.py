a = float(input("preço de compra:"))
preco_produto = str(input("digite o nome do produto:"))
b = float(input("preço de venda:"))
if a < b:
    print("obteve o lucro hehe")
    print("preço compra:", a, "\tpreço venda", b, "\tproduto:",preco_produto)
elif b > a:
    print("obteve o tal do prejuizo")
    print("preço venda:", b, "\tpreço compra", a, "\tproduto:", preco_produto)
else:
    print("os valores são iguais")
