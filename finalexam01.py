import math

def mi(i):
    pi = 0
    for j in range(i):
        pi += math.pow(-1, j) / (2 * j + 1)

    return 4 * pi


print('{0:<10}{1:}'.format('i', 'm(i)'))

for j in range(10):
    i = 1 + j * 100
    print('{0:<10d}{1:.4f}'.format(i, mi(i)))
