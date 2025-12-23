class Personaje:
    def __init__(self, nombre, vida, ataque, defensa):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa

    def atacar (self, objetivo):
        daño = self.ataque - objetivo.defensa
        return max(0, daño)

    def Recibir_Daño (self, daño):
        self.vida -= daño
        if self.vida < 0:
            vida = 'Esta muerto'
        else:
            vida = self.vida
        return vida




