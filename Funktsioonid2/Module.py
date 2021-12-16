#Funktsioonid
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


#funktsioonide_loomine 3
def square(a:float)->float:
    """Sisetame ruudu külg ja tagastame ruudu float läbimõõt, float pindala ja float diagonaal
    :param float a: Ruudu külg
    :rtype: float, float, float
    """
    return P,S,d


#funktsioonide_loomine 4
def season(kuu:int)->str:
    """Võtame kuu number ja tagastame tekst: Talv, Kevad, Suvi või Sügis.
    :param int kuu: kuu number
    :rtype: str
    """
    if kuu in [1,2,12]:
        vastus="Talv"
    elif kuu in [3,4,5]:
        vastus="Kevad"
    elif kuu in [6,7,8]:
        vastus="Suvi"
    elif kuu in [9,10,11]:
        vastus="Sügis"
    return kuu


#funktsioonide_loomine 5
def bank(a:int,years:int)->float:
    """Sisetame aastade arv, ning raha panus ja tagastame raha, mis on suurenenud
    :param int a: Raha panus
    :param int years: Aastade arv
    :rtype: float
    """
    for i in range(years):
        a*=1.1
    return a


#funktsioonide_loomine 6
def is_prime(arv:int)->bool:
    """Kontrollime, kas 
    :param int arv: Arv
    :rtype: bool
    """
    t=0
    for i in range(1,arv+1):
        if arv%i==0: t+=1
    if t==2:
        t=True
    else:
        t=False
    return t