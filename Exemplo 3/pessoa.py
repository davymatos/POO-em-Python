class Pessoa(object):
    def __init__(self, nome, idade, comendo=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo

    def comer(self, alimento):
        #Condição pra ver se esta comendo
        if self.comendo:
            print(f'{self.nome} já está comendo')
            return

        #Comer
        print(f'{self.nome} está comendo {alimento}')
        self.comendo = True

    def pararComer(self):
        #Condição pra ver se esta comendo
        if not self.comendo:
            print(f'{self.nome} não está comendo')
            return

        #parar de comer
        print(f'{self.nome} parou de comer')
        self.comendo = False

