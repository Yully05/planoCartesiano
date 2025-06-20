class Combinatoria:

    def combinaciones_de_3(puntos):
        n = len(puntos)
        resultado = []
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    resultado += [[puntos[i], puntos[j], puntos[k]]]
        return resultado


    def combinaciones_de_4(puntos):
        n = len(puntos)
        resultado = []
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    for l in range(k+1, n):
                        resultado += [[puntos[i], puntos[j], puntos[k], puntos[l]]]
        return resultado
