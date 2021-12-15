#funktsioonid
def Kolmnurga_pindala(külg:float,kõrgus:float):
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

#funktsioonide_loomine 1
def arithmetic(a:float,b:float,tehe:str):
    """Liitmine, lahutamine, korrutamine ja jagamine. On antud a, b ja tehe. Tagastab vastus float formaadis
    :param float a: Esimene arv
    :param float a: Teine arv
    :param str c: Aritmeetilise tehe
    :rtype: var
    """
    if c in ["+","-","*","/"]:
        if c=="/" and b==0:
            vastus="Div/0"
        else:
            vastus=eval(str(a)+c+str(b))
    else:
        vastus="Tundmatu tehe!"
    return vastus

#funktsioonide_loomine 2
def is_year_leap(aasta:int)->bool:
    """Sisetame aasta number ja tagastame True, kui aasta on liigaasta ja False, kui ei ole
    :param int aasta: Aasta järjekordne number
    :rtype: bool
    """
    if aasta%4==0:
        tulemus=True
    else:
        tulemus=False
    return tulemus