print("\n **********  Pthon Calculadora **********")

def Soma(x,y):
    return x + y

def Sub(x,y):
    return x - y

def Mult(x,y):
    return x * y

def Div(x,y):
    return x / y



    
print("\n Escolha uma das opcoes:\n")
print(" 1 - Soma         ")
print(" 2 - Subtração    ")
print(" 3 - Multiplicação")
print(" 4 - Divisão      ")


    
escolha = input("\n Digite uma das opcoes:")

num  = int(input("\n Digite o primeiro numero:"))
num1 = int(input("\n Digite o segundo numero:"))

if escolha == '1':
    print("\n")
    print(num, "+",num1, " = ",Soma(num,num1))
    print("\n")

elif escolha == '2':
    print("\n")
    print(num, "-",num1, " = ",Sub(num,num1))
    print("\n")

elif escolha == '3':
    print("\n")
    print(num, "*",num1, " = ",Mult(num,num1))
    print("\n")


elif escolha == '4':
    print("\n")
    print(num, "/",num1, " = ",Div(num,num1))
    print("\n")

else:
    print("\n")
    print("Opcao invalida !")
    print("\n")
    
