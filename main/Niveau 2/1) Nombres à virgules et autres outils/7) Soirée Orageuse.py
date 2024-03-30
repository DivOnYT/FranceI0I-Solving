from math import floor

nbSeconde = float(input())

vitesse = 340.29  # Vitesse du son en mètres/seconde

if nbSeconde > 0:
    distance = round((vitesse * nbSeconde) / 1000)  # Convertir en kilomètres
    print(distance)
else:
    print(0)  # Si le temps est négatif ou nul, la distance est proche, donc 0 kilomètre