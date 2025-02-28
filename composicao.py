class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []

    def inserirEndereco(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero))

    def listarEnderecos(self):
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero)
            
    def __del__(self):
        print('APAGANDO', self.nome, self.numero)

            

class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero

    def __del__(self):
        print('APAGANDO', self.rua, self.numero)

cliente1 = Cliente('Pedro')
cliente1.inserirEndereco('Av. brasil', 54)
cliente1.inserirEndereco('Av. Paraguai', 12)

print(cliente1.enderecos[0].rua)
cliente1.listarEnderecos()