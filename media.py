a = float(input("type a note from the first trimester:"))
b = float(input("type a note from the second trimester:"))
c = float(input("type a note from the third trimester"))
media = (a * 1 + b * 2 + c * 3) / (1 + 2 + 3)

print("note from first trimester:", a)
print("note from second trimester:", b)
print("note from third trimester:", c)
print(f"the average of the year:", media)