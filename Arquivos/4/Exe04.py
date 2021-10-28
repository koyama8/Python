# Exercício 4 - Crie duas funções, uma para elevar um número ao quadrado e outra para elevar ao cubo. 
# Aplique as duas funções aos elementos da lista abaixo. 
# Obs: as duas funções devem ser aplicadas simultaneamente.
lista = [0, 1, 2, 3, 4,5,6,7,8,9,10]

def square(x):
    return (x**2)

def cub(x):
    return (x**3)

func = [square,cub]
for i in lista:
    valor = map(lambda x: x(i), func)
    print(list(valor))
