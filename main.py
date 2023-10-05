
class Cachorro:
    def __init__(self,nome,raca,peso):
        self.nome = nome
        self.raca=raca
        self.peso=peso


    def comerRacao(self):
        print(f'--Informação do Cachorro--')
        print(f'Nome: {self.nome}')
        print(f'Raça: {self.raca}')
        print(f'Peso: {self.peso}')
        return print("croc, croc, croc")


cachorro1 = Cachorro('Arlequina','PitDalmata','20')
cachorro2 = Cachorro('Cintia','loba','10')

cachorro1.comerRacao()
cachorro2.comerRacao()