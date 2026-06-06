a = int(input("First digit: "))
b = int(input("Second digit: "))
c = input("What to do? (+, -, *, /): ")
if c == "+":
  print(a + b)
elif c == "-":
  print(a - b)
elif c == "*":
  print(a * b)
elif c == "/":
  print(a / b)
else:
  print("Error: ivalid operation sign!")
