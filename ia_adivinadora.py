class IA_Adivinadora:
    def __init__(self):
        self.rango_min = 1
        self.rango_max = 100
        self.intento_actual = None
        self.historial_intentos = []

    def hacer_intento(self):
        self.intento_actual = (self.rango_min + self.rango_max) // 2  # Búsqueda binaria
        return self.intento_actual

    def recibir_feedback(self, feedback):
        if feedback == "mayor":
            self.rango_min = self.intento_actual + 1
        elif feedback == "menor":
            self.rango_max = self.intento_actual - 1
        elif feedback == "correcto":
            return "¡La IA adivinó correctamente!"

        self.historial_intentos.append((self.intento_actual, feedback))
        return f"La IA intentará nuevamente entre {self.rango_min} y {self.rango_max}."

    def reiniciar(self):
        self.rango_min = 1
        self.rango_max = 100
        self.intento_actual = None
        self.historial_intentos = []
