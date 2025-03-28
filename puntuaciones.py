import json
import os

class Puntuaciones:
    def __init__(self):
        self.archivo_puntuaciones = "puntuaciones.json"
        self.datos = {"jugador": {"ganadas": 0, "perdidas": 0, "intentos": []},
                      "ia": {"ganadas": 0, "perdidas": 0, "intentos": []}}
        self.cargar_puntuaciones()

    def cargar_puntuaciones(self):
        if os.path.exists(self.archivo_puntuaciones):
            with open(self.archivo_puntuaciones, "r") as f:
                self.datos = json.load(f)

    def guardar_puntuaciones(self):
        with open(self.archivo_puntuaciones, "w") as f:
            json.dump(self.datos, f, indent=4)

    def registrar_partida(self, jugador, intentos, ganado):
        self.datos[jugador]["intentos"].append(intentos)
        if ganado:
            self.datos[jugador]["ganadas"] += 1
        else:
            self.datos[jugador]["perdidas"] += 1
        self.guardar_puntuaciones()

    def obtener_estadisticas(self):
        return self.datos
