from carta import Carta
import random
class Baralla:
    palos = ["Corazones", "Diamantes","Tréboles","Picas"]
    valores = ["As", "2", "3","4","5","6","7","8","9","10","J","Q","K" ]
    def __init__(self):
        self.cartas =[]
        for palo in self.palos:
            for valor in self.valores:
                cartacreada = Carta(palo,valor)
                self.cartas.append(cartacreada)
    def mostrar(self):
        for carta in self.cartas:
            print(carta)     
    def sacar_carta(self):
        return self.cartas.pop()
    def barallar(self):
        random.shuffle(self.cartas)
# Clase Carta
class Carta:
    def __init__(self, palo,valor):
        self.palo = palo
        self.valor = valor
    def __repr__(self):
        return f"{self.valor} de {self.palo}"
