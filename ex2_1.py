numb = []
p = int(input("Задайте размерность массива: "))
if p < 0:
    print("Недопустимая размерность массива.")

while len(numb) < p:
 numb.append(float(input("Введите элемент массива: ")))

B = float(-99999999999)
f=0

for i in range (p):
  if numb[i] > B:
    B=numb[i]
    f=i

for i in range(p):
    if i > f:
      numb[i]=0


print(numb)