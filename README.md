# AFN (Autómata Finito No Determinista)

Este proyecto implementa un **Autómata Finito No Determinista (AFN)** en Python, diseñado para reconocer palabras reservadas y operadores básicos del lenguaje de programación **C**. El AFN está configurado para aceptar las palabras reservadas `if`, `int`, `else`, `while` y los operadores `i` y `i++`.

## Tabla de Contenidos

- [Descripción del Proyecto](#descripción-del-proyecto)
- [Características](#características)
- [Requisitos](#requisitos)
- [Instalación y Ejecución](#instalación-y-ejecución)
- [Cómo Funciona](#cómo-funciona)
- [Ejemplos de Uso](#ejemplos-de-uso)
- [Contribuciones](#contribuciones)
- [Licencia](#licencia)

## Descripción del Proyecto

Este proyecto implementa un AFN que reconoce:
- Palabras reservadas: `if`, `int`, `else`, `while`.
- Operadores básicos: `i` y `i++`.

El autómata procesa cadenas de entrada y determina si son aceptadas, devolviendo también la palabra más larga reconocida.

## Características

- **Estados y Transiciones:**
  - Los estados están identificados en el formato `"q{numero}"`.
  - Las transiciones son definidas explícitamente para cada palabra reservada y operador.

- **Reconocimiento de Palabras Más Largas:**
  - Si una palabra es un prefijo válido de otra palabra no aceptada, el AFN retrocede para aceptar solo la palabra más larga válida.

- **Palabras Reservadas Reconocidas:**
  - `if`, `int`, `else`, `while`.

- **Operadores Reconocidos:**
  - `i`, `i++`.

## Requisitos

Para ejecutar este proyecto, necesitas:
- **Python 3.8 o superior.**
- Un editor de texto o entorno de desarrollo, como Visual Studio Code.

## Instalación y Ejecución

1. **Clona el repositorio:**
   ```bash
2. **Ejecuta el programa**

    ```bash
    python main.py

Cómo Funciona
Estructura del Proyecto
af.py: Contiene la clase AFN que implementa toda la lógica del autómata. Proporciona métodos para:

Agregar estados y transiciones.
Simular la aceptación de una cadena y encontrar la palabra más larga válida.
main.py: Configura el AFN con estados y transiciones específicas para reconocer las palabras y operadores descritos. Incluye pruebas con cadenas de ejemplo.

Configuración del AFN
Los estados están definidos en el formato "q{numero}", como q0 (estado inicial).
Cada palabra reservada tiene transiciones que conectan los estados.
Ejemplo: Para if:
plaintext
Copiar código
q0 --'i'--> q1
q1 --'f'--> q2
Donde q2 es un estado de aceptación.

Operadores como i++ también tienen estados y transiciones específicos:
plaintext
Copiar código
q1 --'+'--> q15
q15 --'+'--> q16
# Reconcoer-tokens-por-automatas
