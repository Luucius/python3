class Bolo:
    tamanho = 'grande'
    
    def __init__(self, sabor,cobertura):
        self.sabor = sabor
        self.cobertura_bolo = cobertura

        
bolo1 = Bolo('chocolate', 'morango')
bolo2 = Bolo('laranja','leite condensado')

print(bolo1.sabor)
#<3  *
print(bolo1.tamanho)
print(bolo2.sabor)
print(bolo2.tamanho)




if bolo1.sabor == bolo2.sabor:
    print('Você tem dois bolos com sabores iguais!')
else:
    print('Os bolos tem sabores diferentes!')