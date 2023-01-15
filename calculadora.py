import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def raiz(x):
    return pow(x, 1/2)

def exponente(x,y):
    return x ** y


print("Seleccionar la operación a realizar.")
print("1.Suma")
print("2.Resta")
print("3.Multiplicar")
print("4.Dividir")
print("5.Raiz")
print("6.Exponente")
print("7.Seno")
print("8.Coseno")

while True:
    #Listado de operaciones a realizar
    choice = input("Elige el calculo a realizar (1/2/3/4/5/6/7/8): ")

    if choice in ('1', '2', '3', '4', '5', '6', '7','8'):
        
        if choice == '1':
            num1 = float(input("Captura 1 numero: "))
            num2 = float(input("Captura 2 numero: "))
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            num1 = float(input("Captura 1 numero: "))
            num2 = float(input("Captura 2 numero: "))
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            num1 = float(input("Captura 1 numero: "))
            num2 = float(input("Captura 2 numero: "))
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            num1 = float(input("Captura 1 numero: "))
            num2 = float(input("Captura 2 numero: "))
            print(num1, "/", num2, "=", divide(num1, num2))
        
        elif choice == '5':
            num1 = float(input("Captura 1 numero: "))
            print(num1, "^" "=", raiz(num1))
        
        elif choice == '6':
            num1 = float(input("Captura 1 numero: "))
            print(num1, "**",num2, "=", exponente(num1,num2))
        
        elif choice == '7':
            num1 = float(input("Captura 1 numero: "))
            s1 = float (num1)
            s2 = math.radians(s1)
            print(num1, "Seno", "=",math.sin(s2))
        
        elif choice == '8':
            num1 = float(input("Captura 1 numero: "))
            s1 = float (num1)
            s2 = math.radians(s1)
            print(num1, "Coseno", "=",math.cos(s2))
        
        
        next_calculation = input("Desea continuar con otra operación? (si/no): ")
        if next_calculation == "no":
          break
    #Validación de numero no permitidos
    else:
        print("Numero invalido")