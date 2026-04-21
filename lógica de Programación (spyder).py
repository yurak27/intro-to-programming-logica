#ADIVINA EL JUEGO (números m)
import time

def mostrar_bienvenida(datos_juego):
    """Muestra la interfaz inicial usando un diccionario."""
    print("="*50)
    print(f"--- {datos_juego['titulo']} ---")
    print(f"Versión: {datos_juego['version']}")
    print(f"Desarrollado para: {datos_juego['objetivo']}")
    print("="*50)
    print("\nInstrucciones:")
    print(f"1. Piensa un número entre {datos_juego['rango'][0]} y {datos_juego['rango'][1]}.")
    print("2. Yo intentaré adivinarlo.")
    print("3. Dime si mi intento es mayor, menor o igual.\n")

def obtener_feedback():
    """Gestiona la entrada del usuario con validación."""
    opciones_validas = ('m', 'n', 'i', 's') # Tupla de constantes
    while True:
        print("\n¿Cómo es mi intento?")
        print("[M] Mi número es Mayor | [N] Mi número es Menor | [I] ¡Igual! | [S] Salir")
        feedback = input(">> ").lower()
        #feedback actua como entrada de datos  para que el algortimo tome decsiones en tiempo real
        if feedback in opciones_validas:
            return feedback
        else:
            print("Entrada no válida. Por favor, usa M, N, I o S.")

def procesar_logica_adivinanza(limite_inferior, limite_superior, historial):
    """
    Función principal de adivinación usando búsqueda binaria.
    Retorna el estado del juego y los límites actualizados.
    """
    # Cálculo del punto medio (Búsqueda Binaria)
    intento = (limite_inferior + limite_superior) // 2
    historial.append(intento) # Uso de lista para seguimiento
    
    print("\n[Analizando posibilidades...]")
    time.sleep(1)
    print(f"¿Es tu número el {intento}?")
    
    feedback = obtener_feedback()
    
    if feedback == 'i':
        print(f"\n¡Victoria! He adivinado el número en {len(historial)} intentos.")
        return False, limite_inferior, limite_superior
    
    elif feedback == 's':
        print("Juego abortado por el usuario.")
        return False, limite_inferior, limite_superior

    elif feedback == 'm':
        # Si el número del usuario es mayor, el nuevo piso es el intento + 1
        if intento >= limite_superior:
            print("¡Un momento! Me estás dando pistas contradictorias.")
            return True, limite_inferior, limite_superior
        return True, intento + 1, limite_superior

    elif feedback == 'n':
        # Si el número del usuario es menor, el nuevo techo es el intento - 1
        if intento <= limite_inferior:
            print("¡Error detectado! Tus pistas no coinciden con intentos previos.")
            return True, limite_inferior, limite_superior
        return True, limite_inferior, intento - 1

def ejecutar_juego():
    """Estructura repetitiva principal del programa."""
    configuracion = {
        "titulo": "NÚMEROS MÁGICOS",
        "version": "3.O",
        "objetivo": "Práctica de Lógica De programacion",
        "rango": (1, 100) # Tupla dentro de diccionario
    }

    while True:
        mostrar_bienvenida(configuracion)
        
        # Inicialización de variables para el bucle de adivinación
        bajo, alto = configuracion["rango"]
        intentos_realizados = []
        jugando = True
        
        # Bucle for de ejemplo para "calentar" el procesador (estético)
        print("Inicializando algoritmos", end="")
        for i in range(3):
            print(".", end="", flush=True)
            time.sleep(0.3)
        print("\n")

        # Bucle While con lógica de control
        while jugando:
            if bajo > alto:
                print("¡Algo salió mal! Has cambiado las reglas o tu número no existe.")
                break # Rompe el ciclo si hay contradicción lógica
            
            continuar, bajo, alto = procesar_logica_adivinanza(bajo, alto, intentos_realizados)
            
            if not continuar:
                jugando = False
                continue # Salta al final del ciclo para evaluar el estado
        
        # Resumen final usando la lista de historial
        print("\n" + "-"*30)
        print("RESUMEN DE LA PARTIDA:")
        print(f"Intentos totales: {len(intentos_realizados)}")
        print(f"Secuencia de búsqueda: {intentos_realizados}")
        print("-"*30)
        
        reintentar = input("\n¿Quieres jugar otra vez? (S/N): ").lower()
        if reintentar != 's':
            print("Gracias por jugar. Cerrando sistemas...")
            break

# Punto de entrada del script
if "_name_" == "_main_":
  ejecutar_juego()
