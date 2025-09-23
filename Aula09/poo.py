#Classe - Espaçõ onde vou descrever um objeto
#Atributos - caraterísticas do objeto
#métodos - que são as ações desse objeto

# nome e vida - atacar
# self - quando quero me referir a algum atributo da classe
# construtor - quando quero criar um novo objeto, chamo o construtor para acessar os atribtos

class Personagem:
    # construtor
    def __init__(self, nome, vida):
        self.__nome = nome
        self.__vida = vida
    #definindo GET e SET
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @property
    def vida(self):
        return self.__vida

    @vida.setter
    def vida(self, vida):
        self.__vida = vida
    
    def atacar(self, personagem):
        personagem.vida -= 20
        print(f'{self.nome} atacou {personagem.nome} e tirou 20 pontos de vida.')
        print(f' Agora está com {personagem.vida}')


    

class Guerreiro(Personagem):
# construtor
    def __init__(self, nome, vida, escudo=False):
        super().__init__(nome, vida)
    
        self.__escudo = escudo
    #definindo GET e SET
    @property
    def escudo(self):
        return self.__escudo

    @escudo.setter
    def vida(self, escudo):
        self.__escudo = escudo

    # sobrescrevendo o metodo da classe Pai
    def atacar(self, Personagem):
        Personagem.vida -= 40
        print(f'{self.nome} atacou {Personagem.nome} e tirou 40 pontos de vida.')
        print(f' Agora está com {Personagem.vida}')
    
    def protecao(self):
        self.__vida += 10

personagemfav = Guerreiro('MegaCavaleiro' , 500)
print(f'Personagem: {personagemfav.nome}')
print(f'Vida: {personagemfav.vida}')



class Mago(Personagem):
   # construtor
   def __init__(self, nome, vida):
        super().__init__(nome, vida)

   def curar(self, personagem):
       personagem.vida += 15
       print(f'{self.__nome} usou poder de cura em {self.__nome}')
       print(f'A vida de {personagem.nome} agora é de {personagem.vida}')
   def atacar(self, Personagem):
        Personagem.vida -= 30
        print(f'{self.nome} atacou {Personagem.nome} e tirou 30 pontos de vida.')
        print(f' Agora está com {Personagem.vida}')
    

frodo = Personagem('Frodo' , 100)
gandof = Mago('Gandof' , 100)
aragorn = Guerreiro('Aragorn', 100)

aragorn.atacar(frodo)
gandof.curar(frodo)
gandof.atacar(aragorn)
aragorn.atacar(gandof)
gandof.curar(gandof)
frodo.atacar(aragorn)

    
