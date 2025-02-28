# LAMBDA

soma = lambda x, y: x + y
print(soma(3, 5))

print('EQUIVALE A...')

def soma(x, y):
    return x + y

print(soma(3, 5))

# Map()

numeros = [1, 2, 3, 4, 5]
resultado = map(lambda x: x ** 2, numeros)

print(list(resultado))

print('EQUIVALE A...')

def quadrado(x):
    return x ** 2

numeros = [1, 2, 3, 4, 5]
resultado = map(quadrado, numeros)

print(list(resultado)) 

# filter()

def eh_par(x):
    return x % 2 == 0

numeros = [1, 2, 3, 4, 5, 6]
pares = filter(eh_par, numeros)

print(list(pares))

print('EQUIVALE A...')

numeros = [1, 2, 3, 4, 5, 6]
pares = filter(lambda x: x % 2 == 0, numeros)

print(list(pares))