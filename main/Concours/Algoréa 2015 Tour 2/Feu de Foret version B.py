from lib import *
taille = tailleCote()
lig = ligDepart()
col = colDepart()
date = 0
print("On peut afficher du texte pour aider à débugguer " + str(lig) + " " + str(col))
while not estObstacle(lig, col):
   ecrireDate(lig, col, date)
   col -=1
   date += 1