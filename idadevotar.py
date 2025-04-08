a = int(input("digite o ano de nascimento:"))
pop = str(input("digite seu nome:"))
b =  2025
balls = 16
balis = 18
c = b - a
if c >= balis:
    print("possui idade para tirar a CNH e votar")
elif c >= balls and c < balis:
    print("pode votar, porém não poderá tirar CNH")
else:
    print("não vai votar vagabundo, e nem tirar cnh")
print("o ano em que nasceu foi:", a)
print("sua idade é:", c)
print("seu nome é:", pop)
