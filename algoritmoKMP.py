def calcular_arreglo_prefijos(pat):
    m = len(pat)
    lps = [0] * m
    i = 1
    len_pat = 0

    while i < m:
        if pat[i] == pat[len_pat]:
            len_pat += 1
            lps[i] = len_pat
            i += 1
        else:
            if len_pat != 0:
                len_pat = lps[len_pat - 1]
            else:
                lps[i] = 0
                i += 1

    return lps

def buscar_patron(texto, patron):
    n = len(texto)
    m = len(patron)
    lps = calcular_arreglo_prefijos(patron)
    i = 0
    j = 0

    while i < n:
        if texto[i] == patron[j]:
            i += 1
            j += 1

        if j == m:
            print("Patrón encontrado en el índice " + str(i - j))
            j = lps[j - 1]

        elif i < n and patron[j] != texto[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

texto = "ytyytyttutuiiuyiuyiouytyt"
patron = "ytyt"
buscar_patron(texto, patron)
