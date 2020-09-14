class Atleta:
    def __init__(self, cod, nome, altura, peso, idade):
        self.cod = cod
        self.nome = nome
        self.altura = altura
        self.peso = peso
        self.idade = idade

    def setCod(self, cod):
        self.cod = cod

    def getCod(self):
        return self.cod

    def setNome(self, nome):
        self.nome = nome

    def getNome(self):
        return self.nome

    def setAltura(self, altura):
        self.altura = altura

    def getAltura(self):
        return self.altura
    
    def setPeso(self, peso):
        self.peso = peso

    def getPeso(self):
        return self.peso

    def setIdade(self, idade):
        self.idade = idade

    def getIdade(self):
        return self.idade