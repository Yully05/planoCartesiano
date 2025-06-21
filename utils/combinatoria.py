def combinaciones(puntos, cantidadComb):
    resultado = []

    def construirCombinacion(indiceActual, combinacion, posicion):
        # caso base combinacion completa
        if posicion == cantidadComb: #posicion lleva el control de cuntos elementos se han llenado
            nueva = [None] * cantidadComb
            for i in range(cantidadComb):
                nueva[i] = combinacion[i]
            resultado.append(nueva)
            return

        # termina si ya no hay suficientes elementos
        if indiceActual >= len(puntos):
            return

        # tomar el punto actual
        combinacion[posicion] = puntos[indiceActual]
        construirCombinacion(indiceActual + 1, combinacion, posicion + 1)

        # no tomar el punto actual
        construirCombinacion(indiceActual + 1, combinacion, posicion)

    combinacion_inicial = [None] * cantidadComb
    construirCombinacion(0, combinacion_inicial, 0)
    return resultado
