def ordenar_por_area(figuras): # ordena por clave area
    n = len(figuras)
    for i in range(n):
        for j in range(0, n - i - 1):
            if figuras[j]['area'] > figuras[j + 1]['area']:
                figuras[j], figuras[j + 1] = figuras[j + 1], figuras[j]
    return figuras

