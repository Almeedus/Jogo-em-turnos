from random import randint
class Personagem:
    def __init__(self, vida, nome, nivel) -> None:
        self.__vida = vida
        self.__nome = nome
        self.__nivel = nivel

    def exibir_detalhes(self):
        return f'Nome: {self.get_nome()}\nVida: {self.get_vida()}\nNível: {self.get_nivel()}'
    
    def receber_ataque(self, dano):
        self.__vida -= dano
        if self.__vida <= 0:
            self.__vida = 0

    def atacar(self, alvo):
        dano = randint(self.get_nivel() * 2, self.get_nivel() * 4)
        alvo.receber_ataque(dano)
        print(f'\n{self.get_nome()} atacou {alvo.get_nome()} e causou {dano} de dano!')

    
    def get_nome(self):
        return self.__nome
    def get_vida(self):
        return self.__vida
    def get_nivel(self):
        return self.__nivel



class Inimigo(Personagem):
    def __init__(self, vida, nome, nivel, tipo) -> None:
        super().__init__(vida, nome, nivel)
        self.__tipo = tipo

    def exibir_detalhes(self):
        return f'{super().exibir_detalhes()}\nTipo: {self.get_tipo()}\n'


    def get_tipo(self):
        return self.__tipo
  


class Heroi(Personagem):
    def __init__(self, vida, nome, nivel, habilidade) -> None:
        super().__init__(vida, nome, nivel)
        self.__habilidade = habilidade

    def exibir_detalhes(self):
        return f'{super().exibir_detalhes()}\nHabilidade: {self.get_habilidade()}\n'
    
    def ataque_especial(self, alvo):
        dano = randint(self.get_nivel() * 5, self.get_nivel() * 8) #Dano aumentado
        alvo.receber_ataque(dano)
        print(f'{self.get_nome()} usou a habilidade especial {self.get_habilidade()} em {alvo.get_nome()} e causou {dano} de dano!')
    

    def get_habilidade(self):
        return self.__habilidade 
    


class Jogo:
    """ Classe orquestradora do jogo """
    def __init__(self) -> None:
        self.heroi = Heroi(nome='Herói', vida=100, nivel= 5, habilidade= 'Super Força')
        self.inimigo = Inimigo(nome='Morcego',vida=80, nivel=5, tipo='Voador')

    def iniciar_batalha(self):
        print('Iniciando batalha.')
        while self.heroi.get_vida() > 0 and self.inimigo.get_vida() > 0:
            print('\nDetalhes dos Personagens:')
            print(self.heroi.exibir_detalhes())
            print(self.inimigo.exibir_detalhes())

            input("Pressione Enter para atacar.")
            escolha = int(input('Escolha 1 - Ataque Normal, 2 - Ataque especial: '))

            if escolha == 1:
                self.heroi.atacar(self.inimigo)
            elif escolha ==2:
                self.heroi.ataque_especial(self.inimigo)
            else:
                print('\nDigite uma opção válida. Escolha novamente')
            
            if self.inimigo.get_vida() > 0:
                #Inimigo ataca o herói
                self.inimigo.atacar(self.heroi)
        
        if self.heroi.get_vida() > 0:
            print('\nParabéns, você venceu a batalha!')
        else:
            print('\nVocê foi derrotado.')



# Criando instancia do jogo e iniciando batalha
jogo = Jogo()
jogo.iniciar_batalha()