<<<<<<< HEAD
class Ordenamiento:

    @staticmethod
    def ordenar_por_sentido_horario(puntos):
        if len(puntos) != 4:
            return puntos  # No se puede ordenar

        # Calcular centroide manualmente
        x_total = 0
        y_total = 0
        for p in puntos:
            x_total = x_total + p.x
            y_total = y_total + p.y
        cx = x_total / 4
        cy = y_total / 4

        # Clasificar puntos por posición relativa al centroide
        ordenados = [None, None, None, None]  # [inf izq, inf der, sup der, sup izq]

        for p in puntos:
            if p.x <= cx and p.y <= cy:
                if ordenados[0] is None:
                    ordenados[0] = p  # inferior izquierda
            elif p.x > cx and p.y <= cy:
                if ordenados[1] is None:
                    ordenados[1] = p  # inferior derecha
            elif p.x > cx and p.y > cy:
                if ordenados[2] is None:
                    ordenados[2] = p  # superior derecha
            elif p.x <= cx and p.y > cy:
                if ordenados[3] is None:
                    ordenados[3] = p  # superior izquierda

        # Validar que todos fueron clasificados
        incompleto = False
        for i in range(4):
            if ordenados[i] is None:
                incompleto = True

        if incompleto:
            return puntos  # No se puede garantizar orden correcto

        return ordenados
    

    def ordenar3(a, b, c):
        if a <= b and a <= c:
            if b <= c:
                return a, b, c
            else:
                return a, c, b
        elif b <= a and b <= c:
            if a <= c:
                return b, a, c
            else:
                return b, c, a
        else:
            if a <= b:
                return c, a, b
            else:
                return c, b, a
=======
def ordenar_por_area(figuras): # ordena por clave area
    n = len(figuras)
    for i in range(n):
        for j in range(0, n - i - 1):
            if figuras[j]['area'] > figuras[j + 1]['area']:
                figuras[j], figuras[j + 1] = figuras[j + 1], figuras[j]
    return figuras
>>>>>>> 9db5f56897128f2fe38e4226e8fd616d806d2632
