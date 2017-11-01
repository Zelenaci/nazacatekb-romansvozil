# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 17:12:18 2017

@author: Roman Svozil
"""

import random

print("Vyberte program který chcete spustit")
print("1. Obrázky")
print("2. Řady čísel")
print("3. Fibonacciho posloupnost")
print("4. Pascalův trojúhelník")
vybrany_program = int(input())
trojuhelnik = [0,0,0]
a = 1
b = 0
pocet_sudych = 0
seznam_cisel_11_19 = []
seznam_cisel_delitelnych_3_4 = []
soucet_kladnych_cisel = 0
soucet_zapornych_cisel = 0
soucet_druhych_mocnin = 0
pocet_kladnych_cisel = 0
aritmetický_prumer = 0
pocet_clenu_fibonacciho_posloupnosti = 0
seznam_fibonacciho_poslouponosti = [0 , 1]
pocet_seznamu_pascalova_trojuhelniku = 0
seznam_pascalova_trojuhelniku = [1]
if vybrany_program == 1:
    trojuhelnik[0] = trojuhelnik[1] = trojuhelnik[2] = int(input("Napište počet řádků trojúhelníku\n"))
    while trojuhelnik[0] > 0:
        print(trojuhelnik[0] * "*")
        trojuhelnik[0] -=1
    print("\n" , (trojuhelnik[1] - 1) * " " , "*" )
    while trojuhelnik[1] > 1:
        print((trojuhelnik[1] - 1) * " " , ((a * 2) + 1) * "*")
        a += 1
        trojuhelnik[1] -= 1
    print("\n")
    while trojuhelnik[2] > 0:    
        if b < trojuhelnik[2]: b += 1
        elif b == trojuhelnik[2]: pass
        else: b -= 1
        print(b * "*")
        trojuhelnik[2] -= 1
if vybrany_program == 2:
    seznam = [random.randint(1,50) for i in range(20)] 
    print("Seznam náhodných čísel: " , seznam)
    for a in seznam:
        if(a % 2 == 0):
            pocet_sudych += 1
        if((a > 11) and (a < 19)):
            seznam_cisel_11_19.append(a)
        if(((a % 3) == 0) and ((a % 4) == 0) and (a >= 0)):
            seznam_cisel_delitelnych_3_4.append(a)
        if(a >= 0):
            soucet_kladnych_cisel += a
            pocet_kladnych_cisel += 1
        if(a < 0):
            soucet_zapornych_cisel += a
        else:pass
        soucet_druhych_mocnin += a ** 2
    aritmeticky_prumer = soucet_kladnych_cisel / pocet_kladnych_cisel
    print("Sudých čísel je: " , pocet_sudych)
    print("Čísla menší než 19 a větší než 11 jsou: " , seznam_cisel_11_19)
    print("Čísla, která jsou dělitelná 3 a 4 jsou: " , seznam_cisel_delitelnych_3_4)    
    print("Součet kladných čísel je: " , soucet_kladnych_cisel)
    print("Součet záporných čísel je: " , soucet_zapornych_cisel)
    print("Součet druhých mocnin kladných čísel je: " , soucet_druhych_mocnin)
    print("Aritmetický průměr kladných čísel je: " , aritmeticky_prumer)
if vybrany_program == 3:
    pocet_clenu_fibonacciho_posloupnosti = int(input("Kolik členů Fibonacciho posloupnosti chcete vypsat?"))
    while ((pocet_clenu_fibonacciho_posloupnosti - 2) != 0):
        seznam_fibonacciho_poslouponosti.append(seznam_fibonacciho_poslouponosti[-1] + seznam_fibonacciho_poslouponosti[-2])
        pocet_clenu_fibonacciho_posloupnosti -= 1
    print(seznam_fibonacciho_poslouponosti)
if vybrany_program == 4:
    pocet_seznamu_pascalova_trojuhelniku = int(input("Kolik řádků pascalova trojúhelníku si přejete?\n"))
    while pocet_seznamu_pascalova_trojuhelniku > 0:
        print(seznam_pascalova_trojuhelniku)
        seznam_pascalova_trojuhelniku[-1] = []
        seznam_pascalova_trojuhelniku[-1][0] = 1
        seznam_pascalova_trojuhelniku[-1].append(1)
        print(seznam_pascalova_trojuhelniku)
        pocet_seznamu_pascalova_trojuhelniku -= 1