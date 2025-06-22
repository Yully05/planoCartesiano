from graphics.graficos import (
<<<<<<< HEAD
    CuadradosYRectangulos,
    rectangulos,
    triangulos,
    cuadrados
)
def menu(lista):
    while True:
        try:
            print("=== Menú de selección de figuras ===")
            print("1. Dibujar solo cuadrados")
            print("2. Dibujar solo rectángulos")
            print("3. Dibujar solo triángulos")
            print("4. Dibujar todas las figuras")
            print("5. Salir")
            
            opcion = input("Seleccione una opción (1-5): ").strip()

            if opcion == "1":
                cuadrados(lista)
            elif opcion == "2":
                rectangulos(lista)
            elif opcion == "3":
                triangulos(lista)
            elif opcion == "4":
                CuadradosYRectangulos(lista)
                triangulos(lista)
            elif opcion == "5":
                print("Saliendo del programa.")
                break
            else:
                print("Opción no válida. Intente de nuevo.\n")

        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")

=======
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
>>>>>>> origin/rama-yully
