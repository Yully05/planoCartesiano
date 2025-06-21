from graphics.graficos import (
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

