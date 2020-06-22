import sys


def distance(c1, c2):
    return abs(data[c1][0] - data[c2][0]) + abs(data[c1][1] - data[c2][1])


def basecase():
    for k in range(1, customers):
        result[k][0] = distance(k - 1, k) + result[k - 1][0]
        result[0][k] = distance(k - 1, k) + result[0][k - 1] + data[k][2]


customers = int(sys.stdin.readline()) + 1
data = [[0, 0, 0]]
for i in range(1, customers):
    line = sys.stdin.readline().split()
    data.append([int(line[0]), int(line[1]),int(line[2])])

result = [[0] * customers for i in range(customers)]

basecase()

for i in range(1, customers):
    for j in range(1, customers):
        if i != j:
            if j < i - 1:
                result[i][j] = result[i-1][j] + distance(i-1, i)
            elif i < j - 1:
                result[i][j] = result[i][j-1] + distance(j-1, j) + data[j][2]
            elif j == i - 1:
                array = [0] * j
                for k in range(j):
                    array[k] = result[k][j] + distance(k, i)
                result[i][j] = min(array)
            elif i == j - 1:
                array = [0] * i
                for k in range(i):
                    array[k] = result[i][k] + distance(k, j) + data[j][2]
                result[i][j] = min(array)

"""
print("\nDATA:")
for row in data:
    print(row)

print("\nRESULT")
for row in result:
    print(row)
"""

answersI = [0] * (customers - 1)
answersJ = [0] * (customers - 1)
for k in range(customers - 1):
    answersI[k] = result[k][customers - 1] + distance(k, 0) + distance(customers - 1, 0)
    answersJ[k] = result[customers - 1][k] + distance(k, 0) + distance(customers - 1, 0)
answer = min(min(answersI), min(answersJ))
print(answer)
