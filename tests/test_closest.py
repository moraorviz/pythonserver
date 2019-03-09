
def closest(origin, groups, num):
    return 'hi'


orig = [0, 2, -3]
sample = [[190, 10, 8], [293, 4, 2], [321, 6, 19], [192, 8, -7]]


def offset(origin, groups):

    for i in range(len(groups)):
        groups[i][1] -= origin[1]
        groups[i][2] -= origin[2]

    return groups


print(offset(orig, sample))


