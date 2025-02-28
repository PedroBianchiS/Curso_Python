#coleção ordenada mutável, permite membros duplicados
lista = ["carro", 2, True, 2.5]
print('-'*30)
print(lista)
print(lista[2])

#coleção ordenada imutável, permite membros duplicados
tupla = ('carro', 2, True, 2.5)
print('-'*30)
print(tupla)
print(tupla[1])

#coleção ordenada imutável, NÃO permite membros duplicados
dicionario = {'nome': 'Pedro', 'idade': '25'}
print('-'*30)
print(dicionario)
print(dicionario['nome'])

#coleção NÃO ordenada e NÃO indexável, NÃO permite membros duplicados
conjunto = {'Carro', True, 2, 2.5}
print('-'*30)
print(conjunto)