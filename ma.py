class Ma:
    def __init__(self):
        self.cartas = []
        self.valor = 0

    def añadir_carta(self,carta):
        self.cartas.append(carta)

        if carta.valor in ["J","Q","K"]:
            self.valor = 10
        elif carta.valor == "As":
            self.valor += 11
        else:
            self.valor += int(carta.valor)


    def mostrar_cartas(self):
        for carta in self.cartas:
            print(carta)
    def calcular_valor(self):
        
        return self.valor
class Mano:
    def __init__(self):
        self.cartas = []
        self.valor = 0

    def añadir_carta(self,carta):
        self.cartas.append(carta)

        if carta.valor in ["J","Q","K"]:
            self.valor = 10
        elif carta.valor == "As":
            self.valor += 11
        else:
            self.valor += int(carta.valor)


    def mostrar_cartas(self):
        for carta in self.cartas:
            print(carta)
    def calcular_valor(self):
        
        return self.valor
