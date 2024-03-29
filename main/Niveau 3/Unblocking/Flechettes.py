#First Try
def flechettes(nb):
    liste = [["0"] * nb * 2] * nb * 2
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    count = 0
    x1 = 0
    y2 = nb * 2 - 1
    while count < nb:
        for xy in range(nb*2 - 1 - count * 2 ):
            liste[x1][xy+count] = alphabet[count] #bon
            liste[xy+count][x1] = alphabet[count]

            liste[y2][xy+count] = alphabet[count] # bon
            liste[xy+count][y2] = alphabet[count]
        count += 1

        x1 += 1
        y2 -= 1

    return liste

#Second Try #running
def flechettes2(nb):

    liste = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for x in range(2 * nb - 1):
        for y in range(2 * nb - 1):
            distance = max(abs(x - nb +1), abs(y - nb +1))
            letter = alphabet[nb - distance -1]
            liste += letter
        liste += "\n"
    print(liste)
    return liste

def afficher(liste ):
    string = ""
    for y in liste:
        for x in y:
            string += x
        string += "\n"
    print(string)

flechettes2(int(input()))