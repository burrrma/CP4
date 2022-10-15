A = []
B = []

a_s = int(input("Введите размерность массива А: "))
if a_s < 0:
  print("Недопустимое значение размерности массива")
  
while len(A) < a_s:
 A.append(input("Введите элемент массива А: : "))
  
b_s = int(input("Введите размерность массива В: "))
if b_s < 0:
  print("Недопустимое значение размерности массива")
while len(B) < b_s:
  B.append(input("Введите элемент массива В: "))

Com = []
for i in A:
  for k in B:
    if i == k:
      Com.append(i)
      
if len(Com) > 0:   
 print("Общие элементы двух массивов: ", Com)
else:
  print("Общих элементов в массивах нет.")