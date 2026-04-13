import time 
def juego_adivinanza_blanca():
    # --- Identificación de la Autora ---
    autor = "Blanca Segovia"
    
    print("========================================")
    print("MAESTRO DE LA ADIVINANZA BINARIA")
    print(f"       Creado por: {autor}          ")
    print("========================================")
    
    print(f"\n¡Hola! {autor} me ha programado para leer tu mente.")
    input("Piensa en un número del 1 al 100 y presiona ENTER cuando estés listo...")

    # --- Bucle FOR (Conteo regresivo) ---
    print("\nIniciando escaneo cerebral...")
    for i in range(3, 0, -1):
        print(f"{i}...")
        time.sleep(0.6)

    # --- Inicialización de variables (Lógica del Diagrama) ---
    bajo = 1
    alto = 100
    intentos_realizados = [] 
    gane = False

    # --- Bucle WHILE (Estructura principal del juego) ---
    while not gane:
        # Cálculo del punto medio (Búsqueda Binaria)
        adivinanza = (bajo + alto) // 2
        intentos_realizados.append(adivinanza)
        
        print(f"\n[Intento #{len(intentos_realizados)}]: ¿Es el {adivinanza}?")
        print("Responde: 'm' (si tu número es mayor), 'p' (si es pequeño/menor) o 'i' (si es igual)")
        respuesta = input("Respuesta: ").lower().strip()

        if respuesta == 'i':
            print(f"\n¡LOGRADO! He vencido a la mente humana en {len(intentos_realizados)} intentos.")
            gane = True
        elif respuesta == 'm':
            bajo = adivinanza + 1
        elif respuesta == 'p':
            alto = adivinanza - 1
        else:
            print("Entrada no válida. Por favor usa 'm', 'p' o 'i'.")

        # Validación por si el usuario da pistas contradictorias
        if bajo > alto:
            print("\n¡Espera! Tus respuestas se contradicen. ¿Estás haciendo trampa? 🤨")
            break

    # --- Imprimir resultados usando bucle FOR ---
    if gane:
        print("\n--- RESUMEN DE LA PARTIDA ---")
        print("Números que intenté para adivinar:")
        
        for n in intentos_realizados:
            print(f"Intenté el: {n}")
    print(f"\nGracias por jugar el programa de {autor}. ¡Hasta la próxima!")