import matplotlib.pyplot as plt # type: ignore

def dibujarPuntos(listaPuntos):
    for punto in listaPuntos:
        plt.scatter(punto.x, punto.y, color='red')
        plt.text(punto.x + 0.1, punto.y + 0.1, f'({punto.x},{punto.y})')

    plt.title("Plano Cartesiano - Puntos")
#<<<<<<< HEAD
    plt.show()  
#=======
    plt.xlabel('Eje x')
    plt.ylabel('Eje y')
    plt.axhline(0, color='blue')  #eje x
    plt.axvline(0, color='blue')  #eje y
    plt.grid(True)
    plt.show()
#>>>>>>> 9db5f56897128f2fe38e4226e8fd616d806d2632
