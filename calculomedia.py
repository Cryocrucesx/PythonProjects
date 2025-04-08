a = float(input("digite a nota da primeira avaliaçõa:"))
b = float(input("digite a nota da segunda avaliação:"))
media = (a + b) / 2
if media >= 5:
    print("aluno aprovadissimo")
else:
    print("aluno foi reprovado")
print(f"a média do aluno foi de: {media:.2f}\t" ,"O aluno foi aprovado")
