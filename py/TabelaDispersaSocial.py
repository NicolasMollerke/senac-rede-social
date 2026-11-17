# padrão aedlib 2.6

class TabelaDispersaSocial:
    def __init__(self, x: int):
        self.tam  = x
        self.listas = [[] for i in range(x)]

    def social_funcao_hash(self, chave):
        return hash(chave) % self.tam

    def social_inserir(self, chave, objeto):
        indice = self.social_funcao_hash(chave)
        self.listas[indice].append(objeto)
