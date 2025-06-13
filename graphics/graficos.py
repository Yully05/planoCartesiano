import matplotlib.pyplot as plt

def dibujar_puntos(lista_puntos):
    for punto in lista_puntos:
        plt.plot(punto.x, punto.y, 'bo')  # blue dot
        plt.text(punto.x + 0.1, punto.y + 0.1, f'({punto.x},{punto.y})')

    plt.axhline(0, color='gray')  # eje x
    plt.axvline(0, color='gray')  # eje y
    plt.grid(True)
    plt.title("Plano Cartesiano - Puntos")
    plt.show()