from af import AFN #Importamos la clase AFN desde el archivo af.py

def configurar_afn():
    """
    Configura un Autómata Finito No Determinista (AFN) para reconocer:
    - Palabras reservadas del lenguaje C: "if", "int", "else", "while".
    - Operadores válidos: "i", "i++".

    Los estados se identifican con cadenas en el formato "q{numero}".

    Retorna:
        Una instancia de la clase AFN configurada con los estados y transiciones.
    """
    afn = AFN() #Creamos una nueva instancia del AFN

    #===========================
    # Definicion de estados
    #===========================

      # Estados para palabras reservadas y operadores
    afn.agregar_estado("q0", es_inicial=True)  # Estado inicial

    # "if"
    afn.agregar_estado("q1", es_aceptacion=True)
    afn.agregar_estado("q2", es_aceptacion=True)  # Estado final para "if"

    # "int"
    afn.agregar_estado("q3")
    afn.agregar_estado("q4", es_aceptacion=True)  # Estado final para "int"
    afn.agregar_estado("q5")

    # "else"
    afn.agregar_estado("q6")
    afn.agregar_estado("q7")
    afn.agregar_estado("q8")
    afn.agregar_estado("q9", es_aceptacion=True)  # Estado final para "else"

    # "while"
    afn.agregar_estado("q10")
    afn.agregar_estado("q11")
    afn.agregar_estado("q12")
    afn.agregar_estado("q13")
    afn.agregar_estado("q14", es_aceptacion=True)  # Estado final para "while"

    # Operadores: "i", "i+", "i++"
    afn.agregar_estado("q15")  # Estado final para "i+"
    afn.agregar_estado("q16", es_aceptacion=True)  # Estado final para "i++"
  

    # ====================
    # Definición de Transiciones
    # ====================

    # Transiciones para palabras reservadas
    afn.agregar_transicion("q0", "q1", 'i')  # "if" y "int"
    afn.agregar_transicion("q1", "q2", 'f')  # "if"
    afn.agregar_transicion("q1", "q3", 'n')  # "int"
    afn.agregar_transicion("q3", "q4", 't')
    afn.agregar_transicion("q4", "q5", '')

    afn.agregar_transicion("q0", "q6", 'e')  # "else"
    afn.agregar_transicion("q6", "q7", 'l')
    afn.agregar_transicion("q7", "q8", 's')
    afn.agregar_transicion("q8", "q9", 'e')

    afn.agregar_transicion("q0", "q10", 'w')  # "while"
    afn.agregar_transicion("q10", "q11", 'h')
    afn.agregar_transicion("q11", "q12", 'i')
    afn.agregar_transicion("q12", "q13", 'l')
    afn.agregar_transicion("q13", "q14", 'e')

    # Transiciones para operadores
    afn.agregar_transicion("q1", "q15", '+')  # "i+"
    afn.agregar_transicion("q15", "q16", '+')  # "i++"

    return afn

if __name__ == "__main__":
    """
    Programa principal para probar el AFN configurado.
    Se crean varias cadenas de prueba y se evalúa si son aceptadas por el autómata.
    """
    afn = configurar_afn() #Configuramos el AFN
    print("=== Configuración del AFN ===")
    print(afn) # Imprimimos la configuracion del AFN (estados y transiciones)

    # Pruebas
    cadenas = ["if", "int", "else", "while","def", "elif", "intt", " ", "i", "i+", "i++"]
    print("\n=== Resultados de las pruebas ===")
    for cadena in cadenas:
        aceptado, palabra = afn.simular(cadena) #Simular la cadena en el AFN
        if aceptado:
            print(f"'{cadena}' -> Aceptado")
        else:
            print(f"'{cadena}' -> No aceptado")
