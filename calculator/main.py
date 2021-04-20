from art import logo
print(logo)

def add (n1, n2):
  return n1 + n2
def subtract (n1, n2):
  return n1 - n2
def multiply (n1, n2):
  return n1 * n2
def divide (n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}
def calculator():
  num1 = float(input("What's the first number: "))
  for symbol in operations:
    print(symbol)
  end = False

  while not end:
    op_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number: "))
    answer = operations[op_symbol](num1, num2)
    print(f"{num1} {op_symbol} {num2} = {answer}")
    again = input(f"Type \"yes\" to calculate again with {answer}, or \"no\" to restart: ")
    if again == "yes":
      num1 = answer
    else:
      end = True
  
  calculator()    

calculator() 
