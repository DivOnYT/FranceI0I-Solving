nbGrenouilles = int(input())
nbTours = int(input())

grenouilles = [[0, 0] for _ in range(nbGrenouilles)]


def prochain_tour(nbGrenouille, distance):
    grenouilles[nbGrenouille - 1][0] = grenouilles[nbGrenouille - 1][0] + distance
    indexGr = 0
    indexGr2 = 0
    for index, grenouille in enumerate(grenouilles):
        if (grenouilles[indexGr][0] < grenouille[0]):
            indexGr2 = indexGr
            indexGr = index

    if grenouilles[indexGr2][0] != grenouilles[indexGr][0]:
        grenouilles[indexGr][1] += 1


def find_winner():
    max_index = []
    max = 0
    for index, x in enumerate(grenouilles):
        if grenouilles[index][1] > grenouilles[max][1]:
            max = index
            if max_index:
                max_index = []
        elif grenouilles[index][1] == grenouilles[max][1]:
            max_index.append(index)
            max_index.append(max)
    if max_index:
        return max_index[0] + 1
    else:
        return max + 1


count = 0
while count < nbTours:
    inp = input().split(" ")

    gren = int(inp[0])
    dist = int(inp[1])
    prochain_tour(gren, dist)
    count += 1

print(find_winner())