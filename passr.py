calculator = ('''
| ________ |
||12345678||
|""""""""""|
|[M|#|C][-]|
|[7|8|9][+]|
|[4|5|6][x]|
|[1|2|3][%]|
|[.|O|:][=]|
"----------"''')
print(calculator)
def add(n1,n2):
  return n1+n2
def mynus(n1,n2):
  return n1 - n2
def intu(n1,n2):
  return n1*n2
def devide(n1,n2):
  return n1/n2
oporation = {
  "+":add,
  "-":mynus,
  "*":intu,
  "/":devide,
}
def user():
  num1 =int(input("Enter your number: "))
  num2 =int(input("Enter your number: "))
  for symbols in oporation:
    print(symbols)
  oporation_symbol = input("Enter your symbol: ")
  calculation = oporation[oporation_symbol]
  Ans = calculation(num1,num2)
  print(f"{num1}{oporation_symbol}{num2}={Ans}") 
user()
ask = 0
while ask != True:
  ask = input("Do you want to do more? y/n: ")
  if ask =="y":
    user()
  elif ask =="n":
    ask == False
    break