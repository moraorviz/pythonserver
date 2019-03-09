
def closest(origin, groups, num):
    return 'hi'


orig = [0, 2, -3]
orig_var = [[0, 2, -3]]
sample_1 = [[190, 10, 8], [293, 4, 2], [321, 6, 19], [192, 8, -7]]
sample_2 = [[190, 10, 8], [293, 4, 2], [321, 6, 19], [192, 8, -7]]


def offset(origin, groups):

    for i in range(len(groups)):
        groups[i][1] -= origin[1]
        groups[i][2] -= origin[2]

    return groups


def offset_variant(origin_var, groups):

    for i in range(len(groups)):
        groups[i][1] -= origin_var[0][1]
        groups[i][2] -= origin_var[0][2]

    return groups


print(offset(orig, sample_1))
print(offset_variant(orig_var, sample_2))


