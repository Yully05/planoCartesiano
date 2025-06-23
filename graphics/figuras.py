from graphics.graficos import (
    dibujarRectangulos,
    dibujarTriangulosRectangulos,
    dibujarCuadrados,
    dibujarTriangulosAcutangulos
)

def menu(lista):
    while True:
        try:
            print("\n======== Menu de figuras ========\n")
            print("1. Dibujar cuadrados")
            print("2. Dibujar rectangulos")
            print("3. Dibujar triangulos rectangulos")
            print("4. Dibujar triangulos acutangulos")
            print("5. Salir")
            
            opcion = input("Seleccione una opcion: ").strip()

            if opcion == "1":
                dibujarCuadrados(lista)
            elif opcion == "2":
                dibujarRectangulos(lista)
            elif opcion == "3":
                dibujarTriangulosRectangulos(lista)
            elif opcion == "4":
                dibujarTriangulosAcutangulos(lista)
            elif opcion == "5":
                print("Saliendo del programa...")
                break
            else:
                print("\nOpcion no valida.")

        except Exception as e:
            print(f"Error: {e}")