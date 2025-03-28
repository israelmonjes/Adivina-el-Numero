# 🎮 Adivina el Número

> Un juego interactivo en Python con **Flet**, donde puedes jugar solo, contra una IA o en modo multijugador. Con estadísticas, sonidos y un modo desafiante con un número misterioso. 🔥

## 🚀 Características
✅ **Modos de Juego:** 
- 🧑 **Clásico**: Adivina el número secreto.
- 🤖 **Modo IA**: La IA intenta adivinar el número que piensas.
- 👥 **Multijugador**: Dos jugadores compiten por adivinar el número del otro.
- 🎭 **Número Misterioso**: ¡El número cambia después de ciertos intentos!

✅ **IA Mejorada:**
- Ahora la IA usa **búsqueda binaria** en lugar de intentos aleatorios.

✅ **Sonidos y Animaciones:**
- 🎵 Sonido al ganar (`win.mp3`) y perder (`lose.mp3`).
- 🎨 Colores dinámicos según el progreso.

✅ **Puntuaciones y Estadísticas:**
- 📊 Guarda victorias, derrotas e intentos en `puntuaciones.json`.

## 🛠 Instalación y Ejecución
### 1️⃣ Requisitos
- **Python 3.10+**
- Librerías necesarias: `flet`, `playsound`

Instálalas con:
```sh
pip install flet playsound
```

### 2️⃣ Clona este repositorio
```sh
git clone https://github.com/israelmonjes/Adivina-el-Numero.git
cd adivina-el-numero
```

### 3️⃣ Ejecuta el juego
```sh
python main.py
```

## 🎮 Cómo Jugar
### 🧑 Modo Clásico
1. Selecciona una **dificultad** (Fácil, Medio, Difícil, Experto).
2. Introduce un número.
3. Recibe pistas: 🔽 **Mayor** | 🔼 **Menor**.
4. ¡Gana cuando aciertes! 🎉

### 🤖 Modo IA
1. Piensa en un número.
2. La IA intentará adivinarlo.
3. Usa los botones: `Mayor`, `Menor`, `Correcto` para guiarla.
4. ¡La IA aprende y mejora con cada intento! 🤯

### 👥 Modo Multijugador
1. Cada jugador introduce un número secreto.
2. Turnos alternos para adivinar el número del oponente.
3. ¡Gana el jugador con menos intentos! 🏆

### 🎭 Modo Número Misterioso
- Después de **5 intentos**, el número cambia automáticamente. 🤯

## 📂 Estructura del Proyecto
```
📦 adivina-el-numero
├── 📄 main.py            # Punto de entrada del juego
├── 📄 juego.py           # Lógica del juego
├── 📄 ia_adivinadora.py  # IA con búsqueda binaria
├── 📄 interfaz.py        # Interfaz con Flet
├── 📄 puntuaciones.py    # Sistema de puntuaciones
├── 📄 multijugador.py    # Modo multijugador
├── 📄 game_logs.txt      # Registros del juego
├── 📄 puntuaciones.json  # Datos de puntuaciones
├── 🎵 win.mp3            # Sonido de victoria
├── 🎵 lose.mp3           # Sonido de derrota
└── 📄 README.md          # Documentación
```

## 🚀 Mejoras Futuras
- 🌎 **Integración con base de datos en la nube.**
- 📱 **Versión móvil con interfaz táctil.**
- 🔥 **Nuevos modos de juego personalizados.**
--**Descarga la demo aca:** https://drive.google.com/file/d/1aNuV9A0EmNT0qcz0CEW1ZLTW-B_ACDu4/view?usp=drive_link

---
🎯 **Desarrollado con pasión por [Eliseo Monjes](https://github.com/israelmonjes).** 💡✨
