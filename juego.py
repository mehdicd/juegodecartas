from baralla import Baralla
from ma import Ma

class Juego:
    def __init__(self):
        self.baralla = Baralla()
        self.baralla.barallar()

    def jugar(self):
        majugador = Ma()

        carta = self.baralla.sacar_carta()
        majugador.añadir_carta(carta)
        majugador.mostrar_cartas()
        print("Punts:", majugador.valor)

        while majugador.valor < 21:
            accio = input("vols una altra carta? (s/n): ")
            if accio == "s":
                        carta = self.baralla.sacar_carta()
                        majugador.añadir_carta(carta)
                        majugador.mostrar_cartas()
                        print("Punts:", majugador.valor)
            else:
                break
        
        if majugador == 21:
            print("¡Has ganado!")
            print("Punts:", majugador.valor)
        else:
            print("Has perdido")
            print("Punts:", majugador.valor)
