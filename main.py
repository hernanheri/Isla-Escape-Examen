from juego import JuegoIsla

def main():
    while True:
        print("\n1. Jugar\n2. Salir")
        opcion = input("Elige una opción: ")
        if opcion == "1":
            juego = JuegoIsla()
            juego.jugar()
        elif opcion == "2":
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()