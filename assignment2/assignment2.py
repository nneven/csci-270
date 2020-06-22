import sys


class Point(object):
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print(self):
        print("(" + str(self.x) + ", " + str(self.y) + ")")


def isLeft(p1, p2, p3):
    return (((p3.x - p1.x) * (p2.y - p1.y)) - ((p3.y - p1.y) * (p2.x - p1.x))) > 0


def area(p1, p2, p3):
    return abs(p1.x * p2.y + p2.x * p3.y + p3.x * p1.y - p2.x * p1.y - p3.x * p2.y - p1.x * p3.y) / 2


N = int(sys.stdin.readline())
V = 6
points = []
OPT = [[[[0 for v in range(V)] for k in range(N)] for j in range(N)] for i in range(N)]
for line in range(0, N):
    data = [int(x) for x in sys.stdin.readline().split()]
    points.append(Point(data[0], data[1]))
points = sorted(points, key=lambda p: [p.x, p.y])

"""
with open("Sample1.txt") as f:
    N = int(f.readline())
    V = 6
    points = []
    OPT = [[[[0 for v in range(V)] for k in range(N)] for j in range(N)] for i in range(N)]
    for line in f:
        data = [int(x) for x in line.split()]
        points.append(Point(data[0], data[1]))
    points = sorted(points, key=lambda p:[p.x, p.y])

    for p in range(0, N):
        points[p].print();
"""

for i in range(0, N):
    pI = points[i]
    for j in range(i, N):
        pJ = points[j]
        for k in range(i, N):
            pK = points[k]
            if pI != pJ and pI != pK and pJ != pK:
                if isLeft(pI, pJ, pK):
                    OPT[i][j][k][2] = area(pI, pJ, pK)
                    """print(OPT[i][j][k][2])"""

result = float("inf")
for v in range(3, V):
    for i in range(0, N):
        pI = points[i]
        for j in range(i, N):
            pJ = points[j]
            for k in range(i, N):
                pK = points[k]
                if pI != pJ and pI != pK and pJ != pK:
                    if isLeft(pI, pJ, pK):
                        min = float("inf")
                        for m in range(i, N):
                            pM = points[m]
                            if pI != pK and pI != pM and pK != pM:
                                if isLeft(pI, pK, pM) and isLeft(pJ, pK, pM):
                                    if OPT[i][k][m][v - 1] < min:
                                        min = OPT[i][k][m][v - 1]
                                        """print(min)"""
                        OPT[i][j][k][v] = min + OPT[i][j][k][2]
                        if v == 5 and OPT[i][j][k][v] < result:
                            result = OPT[i][j][k][v];

print(result)