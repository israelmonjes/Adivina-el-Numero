import flet as ft
import logging
from juego import Juego
from interfaz import Interfaz
from ia_adivinadora import IA_Adivinadora
from puntuaciones import Puntuaciones
from multijugador import Multijugador  # Asegúrate de incluir este archivo

# Configuración del sistema de logs
logging.basicConfig(
    filename="game_logs.txt", 
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def main(page: ft.Page):
    """
    Inicializa la aplicación de "Adivina el Número" con una interfaz interactiva y dinámica.
    Diseñado para ofrecer una experiencia fluida y profesional con una arquitectura modular.
    """
    page.title = "Adivina el Número"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.DARK
    
    # Inicializar la lógica del juego, IA, puntuaciones y multijugador
    juego = Juego()
    ia_adivinadora = IA_Adivinadora()
    puntuaciones = Puntuaciones()
    multijugador = Multijugador()
    
    interfaz = Interfaz(page, juego, ia_adivinadora, puntuaciones, multijugador)
    
    # Agregar la interfaz a la página
    page.add(interfaz.contenedor)
    page.update()
    
    logging.info("Aplicación iniciada correctamente.")
    print("Aplicación iniciada correctamente.")

if __name__ == "__main__":
    ft.app(target=main)
