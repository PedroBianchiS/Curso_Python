class Caneta():
    def __init__(self, cor):
        self.cor_tinta = cor

    @property
    def cor(self):
        print('property')
        return self.cor_tinta
    

caneta = Caneta('azul')

print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
