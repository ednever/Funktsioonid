def Kolmnurga_pindala(külg:float,kõrgus:float,):
    """Leiab kolmnurga pindalat. On antud kõrgus ja külje pikkus. Tagastab S float formaadis
    :param float külg: Kolmnurga külje pikkus
    :param float kõrgus: Kõrgus vastav küljele
    :rtype: var
    """
    if külg<0 or kõrgus<0:
        S="Valed andmed"
    else:
        S=0.5*külg*kõrgus

    return S