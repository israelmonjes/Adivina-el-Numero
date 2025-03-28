import flet as ft

class Interfaz:
    def __init__(self, page, juego, ia_adivinadora, puntuaciones, multijugador):
        self.page = page
        self.juego = juego
        self.ia_adivinadora = ia_adivinadora
        self.puntuaciones = puntuaciones
        self.multijugador = multijugador

        self.mensaje = ft.Text("Selecciona un modo y adivina el número.", color=ft.colors.WHITE)
        self.input_numero = ft.TextField(label="Tu número", keyboard_type=ft.KeyboardType.NUMBER, on_submit=self.verificar_numero)
        self.boton_verificar = ft.ElevatedButton("Adivinar", on_click=self.verificar_numero)
        self.boton_reiniciar = ft.OutlinedButton("Reiniciar Juego", on_click=self.reiniciar_juego)

        # UI para IA
        self.ia_mensaje = ft.Text("Modo IA: Piensa en un número y deja que la IA lo adivine.")
        self.boton_ia_intentar = ft.ElevatedButton("IA Intenta", on_click=self.ia_intento)
        self.boton_ia_mayor = ft.ElevatedButton("Mayor", on_click=self.ia_feedback, data="mayor")
        self.boton_ia_menor = ft.ElevatedButton("Menor", on_click=self.ia_feedback, data="menor")
        self.boton_ia_correcto = ft.ElevatedButton("Correcto", on_click=self.ia_feedback, data="correcto")
        self.boton_ia_reiniciar = ft.OutlinedButton("Reiniciar IA", on_click=self.reiniciar_ia)

        # UI para Multijugador
        self.multi_mensaje = ft.Text("Modo Multijugador: Cada jugador ingresa un número secreto.")
        self.input_jugador1 = ft.TextField(label="Número Jugador 1", keyboard_type=ft.KeyboardType.NUMBER)
        self.input_jugador2 = ft.TextField(label="Número Jugador 2", keyboard_type=ft.KeyboardType.NUMBER)
        self.boton_set_jugadores = ft.ElevatedButton("Configurar Números", on_click=self.configurar_multijugador)
        self.boton_multi_intentar = ft.ElevatedButton("Intentar", on_click=self.verificar_multijugador)

        self.contenedor = ft.Column(
            [
                self.mensaje,
                ft.Row([
                    ft.ElevatedButton("Fácil", on_click=self.seleccionar_dificultad, data="Fácil"),
                    ft.ElevatedButton("Medio", on_click=self.seleccionar_dificultad, data="Medio"),
                    ft.ElevatedButton("Difícil", on_click=self.seleccionar_dificultad, data="Difícil"),
                    ft.ElevatedButton("Experto", on_click=self.seleccionar_dificultad, data="Experto"),
                ], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([self.input_numero, self.boton_verificar], alignment=ft.MainAxisAlignment.CENTER),
                self.boton_reiniciar,

                # Sección para la IA
                ft.Divider(),
                self.ia_mensaje,
                self.boton_ia_intentar,
                ft.Row([self.boton_ia_mayor, self.boton_ia_menor, self.boton_ia_correcto], alignment=ft.MainAxisAlignment.CENTER),
                self.boton_ia_reiniciar,

                # Sección para Multijugador
                ft.Divider(),
                self.multi_mensaje,
                ft.Row([self.input_jugador1, self.input_jugador2], alignment=ft.MainAxisAlignment.CENTER),
                self.boton_set_jugadores,
                self.boton_multi_intentar
            ], alignment=ft.MainAxisAlignment.CENTER
        )

    def seleccionar_dificultad(self, e):
        self.juego.seleccionar_dificultad(e.control.data)
        self.mensaje.value = f"Modo {e.control.data} seleccionado. Adivina el número entre 1 y {self.juego.rango}"
        self.mensaje.color = ft.colors.BLUE
        self.page.update()

    def verificar_numero(self, e):
        try:
            num = int(self.input_numero.value)
            resultado = self.juego.verificar_numero(num)
            self.mensaje.value = resultado

            if "🎉" in resultado:
                self.puntuaciones.registrar_partida("jugador", self.juego.intentos, True)
                self.mensaje.color = ft.colors.GREEN
            elif "🔽" in resultado or "🔼" in resultado:
                self.mensaje.color = ft.colors.YELLOW
            else:
                self.mensaje.color = ft.colors.RED

            self.input_numero.value = ""
        except ValueError:
            self.mensaje.value = "❌ Ingresa un número válido."
            self.mensaje.color = ft.colors.RED

        self.page.update()

    def reiniciar_juego(self, e):
        self.juego.reiniciar_juego()
        self.mensaje.value = f"Nuevo juego iniciado. Adivina el número entre 1 y {self.juego.rango}"
        self.mensaje.color = ft.colors.BLUE
        self.input_numero.value = ""
        self.page.update()

    # --- Métodos para la IA ---
    def ia_intento(self, e):
        intento = self.ia_adivinadora.hacer_intento()
        self.ia_mensaje.value = f"¿Es {intento} tu número?"
        self.page.update()

    def ia_feedback(self, e):
        feedback = e.control.data
        resultado = self.ia_adivinadora.recibir_feedback(feedback)
        self.ia_mensaje.value = resultado
        self.page.update()

    def reiniciar_ia(self, e):
        self.ia_adivinadora.reiniciar()
        self.ia_mensaje.value = "Modo IA reiniciado. Piensa en un nuevo número."
        self.page.update()

    # --- Métodos para Multijugador ---
    def configurar_multijugador(self, e):
        try:
            num1 = int(self.input_jugador1.value)
            num2 = int(self.input_jugador2.value)
            self.multijugador.establecer_numero(1, num1)
            self.multijugador.establecer_numero(2, num2)
            self.multi_mensaje.value = "Números configurados. ¡Empieza el juego!"
        except ValueError:
            self.multi_mensaje.value = "❌ Ingresa valores válidos para ambos jugadores."
        self.page.update()

    def verificar_multijugador(self, e):
        try:
            intento1 = int(self.input_jugador1.value)
            intento2 = int(self.input_jugador2.value)

            resultado1 = self.multijugador.verificar_intento(1, intento1)
            resultado2 = self.multijugador.verificar_intento(2, intento2)

            self.multi_mensaje.value = f"Jugador 1: {resultado1} | Jugador 2: {resultado2}"
        except ValueError:
            self.multi_mensaje.value = "❌ Ingresa valores válidos para ambos jugadores."
        self.page.update()
