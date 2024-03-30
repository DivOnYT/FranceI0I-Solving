damier = ""
for x in range(40):
    for y in range(20):
        if x % 2 == 0:
            damier += "OX"
        else:
            damier += "XO"
    damier += "\n"

print(damier)