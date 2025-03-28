class Multijugador:
    def __init__(self):
        self.turno = 1
        self.numeros_secretos = {1: None, 2: None}
        self.intentos = {1: 0, 2: 0}

    def establecer_numero(self, jugador, numero):
        self.numeros_secretos[jugador] = numero

    def verificar_intento(self, jugador, intento):
        self.intentos[jugador] += 1
        if intento < self.numeros_secretos[jugador]:
            return "🔽 El número es mayor."
        elif intento > self.numeros_secretos[jugador]:
            return "🔼 El número es menor."
        else:
            return f"🎉 ¡Jugador {jugador} ganó en {self.intentos[jugador]} intentos!"
