a = int(input("Введите первое число >>> "))
b = int(input("Введите второе число >>> "))
while a != 0 and b != 0:
  if abs(a) > abs(b):
    a = a % b
  else:
    b = b % a
print(a + b)