import random
import logging

class Juego:
    def __init__(self):
        self.rango = 10
        self.numero_secreto = random.randint(1, self.rango)
        self.intentos = 0
        self.intentos_para_cambio = 5  # Cambia el número después de 5 intentos
        self.limite_intentos = None  # Para el modo experto

    def seleccionar_dificultad(self, dificultad):
        if dificultad == "Fácil":
            self.rango = 10
            self.limite_intentos = None
        elif dificultad == "Medio":
            self.rango = 50
            self.limite_intentos = None
        elif dificultad == "Difícil":
            self.rango = 100
            self.limite_intentos = None
        elif dificultad == "Experto":
            self.rango = 100
            self.limite_intentos = 3  # Solo 3 intentos

        self.numero_secreto = random.randint(1, self.rango)
        self.intentos = 0

        logging.info(f"Dificultad seleccionada: {dificultad}. Número secreto generado entre 1 y {self.rango}.")

    def verificar_numero(self, num):
        self.intentos += 1
        if self.intentos % self.intentos_para_cambio == 0:
            self.numero_secreto = random.randint(1, self.rango)  # Número cambia dinámicamente

        if num < self.numero_secreto:
            resultado = "🔽 El número es mayor."
        elif num > self.numero_secreto:
            resultado = "🔼 El número es menor."
        else:
            resultado = f"🎉 ¡Correcto! Adivinaste en {self.intentos} intentos."

        logging.info(f"Intento {self.intentos}: Usuario ingresó {num}. Resultado: {resultado}")

        if self.limite_intentos and self.intentos >= self.limite_intentos and num != self.numero_secreto:
            resultado += " ❌ Has alcanzado el límite de intentos. El juego se reiniciará."
            self.reiniciar_juego()
        
        return resultado

    def reiniciar_juego(self):
        self.numero_secreto = random.randint(1, self.rango)
        self.intentos = 0
        logging.info("El juego ha sido reiniciado.")
