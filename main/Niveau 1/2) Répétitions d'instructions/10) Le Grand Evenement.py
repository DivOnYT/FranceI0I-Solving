from robot import *

for x in range(9):
    haut()

droite()
for y in range(5):
    for x in range(8):
        droite()
    bas()
    for x in range(8):
        gauche()
    if y != 4:
        bas()
gauche()