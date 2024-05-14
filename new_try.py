from random import randint


def check_exit(row, column, maze):
    walls = 0

    if maze[row + 1][column] == "#":
        walls += 1
    if maze[row][column + 1] == "#":
        walls += 1
    if maze[row - 1][column] == "#":
        walls += 1
    if maze[row][column - 1] == "#":
        walls += 1
    if walls == 4:
        print("NOT EXIT FROM THIS PLACE")
        return False
    return True


n, m = 6, 6
num = 0
mas = 0
MAZE = [[0 for i in range(6)] for j in range(6)]

for x in range(n * m):
    cell = randint(1, 2)
    if cell == 1:
        MAZE[mas][num] = "."
    if cell == 2:
        MAZE[mas][num] = "#"
    num += 1
    if num == 6:
        mas += 1
        num = 0

row = randint(1, 4)  # строка начала
column = randint(1, 4)  # столбец начала

while MAZE[row][column] == "#":
    row = randint(1, 4)
    column = randint(1, 4)
MAZE[row][column] = "&"

print("Start: ", row + 1, " : ", column + 1, "\n")

for mas in range(n):
    for num in range(m):
        print(MAZE[mas][num], end="   ")
    print("\n")

if not check_exit(row, column, MAZE):
    exit()

steps = 0

steps_check = [0] * 100

h = 0
row2 = row
column2 = column
t = 0
Q = 0
while h < 100:
    while (row != 0 and row != 5 and column != 0 and column != 5):
        Q = randint(1, 4)
        if Q == 1:
            if MAZE[row + 1][column] == ".":
                MAZE[row][column] = "#"
                row += 1
                t = 1

        if Q == 2:
            if MAZE[row][column + 1] == ".":
                MAZE[row][column + 1] = "#"
                column += 1
                t = 1

        if Q == 3:

            if MAZE[row - 1][column] == ".":
                MAZE[row][column + 1] = "#"
                row -= 1
                t = 1
        if Q == 4:
            if MAZE[row][column - 1] == ".":
                MAZE[row][column + 1] = "#"
                column -= 1
                t = 1

        if steps > 1000:
            print("NOT EXIT")
            break

        if t == 1:
            steps += 1
        t = 0

    row = row2
    column = column2
    steps_check[h] = steps
    steps = 0
    h += 1

steps = min(steps_check)

print("Number of steps: ", steps)