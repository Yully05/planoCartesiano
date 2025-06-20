import matplotlib.pyplot as plt

def dibujarPuntos(listaPuntos):
    for punto in listaPuntos:
        plt.scatter(punto.x, punto.y, color='red')
        plt.text(punto.x + 0.1, punto.y + 0.1, f'({punto.x},{punto.y})')

    plt.title("Plano Cartesiano - Puntos")
    plt.xlabel('Eje x')
    plt.ylabel('Eje y')
    plt.axhline(0, color='blue')  #eje x
    plt.axvline(0, color='blue')  #eje y
    plt.grid(True)
    plt.show()