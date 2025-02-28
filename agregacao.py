class Carrinho:
    def __init__(self):
        self._produtos = []

    def total(self):
        return print(sum([p.preco for p in self._produtos]))
    
    def inserirProdutos(self, *produtos):
        self._produtos += produtos
    
    def listar_produtos(self):
        for produto in self._produtos:
            print(produto.nome, produto.preco)

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

carrinho = Carrinho()

p1, p2 = Produto('Caneta', 1.20), Produto('Camiseta', 20)

carrinho.inserirProdutos(p1, p2)
carrinho.listar_produtos()
carrinho.total()