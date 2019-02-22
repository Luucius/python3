class Pessoa:
    def __init__(self, nome, cor_olhos,cor_cabelo,cor_pele,altura):
        self.nome = nome
        self.cor_olhos = cor_olhos
        self.cor_cabelo = cor_cabelo
        self.cor_pele = cor_pele
        self.altura = altura

fulano = Pessoa('João','castanhos','azul','amarelo',1.97)

print(fulano.nome)


class Crianca(Pessoa):
    def __init__(self, desenho_favorito,brinquedo_favorito,*kwargs):
        self.desenho_favorito=desenho_favorito
        self.brinquedo_favorito=brinquedo_favorito

b