from random import randint
def bezvihod(s1, s2):
    if s1 in range(5) and s2 in range(5):
        x, y = s1, s2
        q = 0
        if m[x+1][y] == 1:
            q += 1
        if m[x][y+1] == 1:
            q += 1
        if m[x-1][y] == 1:
            q += 1
        if m[x][y-1] == 1:
            q += 1
        if q == 4:
            print("Проигрыш в любом случае, безвыходная ситуация")
            return False
        return True
def kraya(s1, s2):
    x, y = s1, s2
    q = 0
    if (m[0][0] == 9 or m[5][5] == 9 or m[0][5] == 9 or m[5][0] == 9):
        q += 1
    if (m[0][1] == 1 or m[0][4] == 1 or m[5][1] == 1 or m[5][4] == 1):
        q += 1
    if (m[1][0] == 1 or m[4][0] == 1 or m[1][5] == 1 or m[4][5] == 1):
        q += 1
    if q == 3:
        print("Проигрыш в любом случае, безвыходная ситуация")
    elif q == 2:
        print("Выигрыш за 1 ход")
        return False
    return True

a, b = 6, 6
m = [[randint(0, 1) for j in range(b)] for i in range(a)]
for i in range(0, 6):
    print(m[i])
print()
for i in range(0,6):
    for j in range(0,6):
        if m[i][j] == 1:
            print("+  ", end="")
        else:
            print(".  ", end="")
        print()
for i in range(0, 100):
    s1 = randint(0,5)
    s2 = randint(0,5)
    if m[s1][s2] == 0:
        print("Коорды входа", s1+1, s2+1)
        m[s1][s2] = 9
        break
for i in range(0,6):
    for j in range(0,6):
        if m[i][j] == 1:
            print("+  ", end="")
        elif m[i][j] == 9:
            print("O  ", end="")
        else:
            print(".  ", end="")
    print()
bezvihod(s1, s2)
kraya(s1, s2)

