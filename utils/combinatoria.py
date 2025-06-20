def combinaciones(puntos, longitudDeseada):
    resultado = []

    def construirCombinacion(indiceActual, combinacion, posicion):
        # caso base combinacion completa
        if posicion == longitudDeseada: #posicion lleva el control de cuántos elementos se han llenado
            nueva = [None] * longitudDeseada
            for i in range(longitudDeseada):
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

    combinacion_inicial = [None] * longitudDeseada
    construirCombinacion(0, combinacion_inicial, 0)
    return resultado
