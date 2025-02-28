nums = [54, 22, 46, 55, 13, 28, 19, 10]

# SEM LIST COMPREHENSION
""" pares = []

for num in nums:
    if num % 2 == 0:
        pares.append(num)

print(pares) """

# COM LIST COMPREHENSION

pares = [num for num in nums if num % 2 == 0]

print(pares)

# OPERANDO COM LIST COMPREHENSION

divididos = [num / 2 for num in nums]
mult = [num * 2 for num in nums]
quadrado = [num ** 2 for num in nums]
print(divididos)
print(mult)
print(quadrado)

# FUNÇÕES EM LIST COMPREHENSION

def divisão(x, y):
    return x / y

divididos = [divisão(num, 2) for num in nums]
print(divididos)

# FUNÇÕES ANINHADAS E MATRIZ

linha_e_coluna = [
    (x, y)
    if y == 2 else 'não é 2' # filtro antes
    for x in range(1, 7)
    for y in range(1, 7) # for aninhado
    if x != 2 # filtro depois
]

print(linha_e_coluna)

