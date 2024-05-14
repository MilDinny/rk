import random


def sozdanie_massiva(N, M):
    return [['+' if random.random() < 0.5 else '.' for _ in range(M)] for _ in range(N)]


def real(m_osnov):
    N, M = len(m_osnov), len(m_osnov[0])
    exits = [(0, random.randint(0, M - 1)), (N - 1, random.randint(0, M - 1)),
             (random.randint(0, N - 1), 0), (random.randint(0, N - 1), M - 1)]
    exit_x, exit_y = random.choice(exits)
    m_osnov[exit_x][exit_y] = '.'

    start_x, start_y = random.randint(0, N - 1), random.randint(0, M - 1)
    m_osnov[start_x][start_y] = 'O'
    return m_osnov, (start_x, start_y)


def poisk_vihoda_luchego(maze, start):
    N, M = len(maze), len(maze[0])
    queue = [(start[0], start[1], 0)]
    uzhe_bil_tam = set()
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while queue:
        x, y, dist = queue.pop(0)
        if (x, y) in uzhe_bil_tam:
            continue
        uzhe_bil_tam.add((x, y))

        if x == 0 or x == N - 1 or y == 0 or y == M - 1:
            if (x, y) != start:
                return True, dist, (x, y)

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and maze[nx][ny] == '.' and (nx, ny) not in uzhe_bil_tam:
                queue.append((nx, ny, dist + 1))

    return False, None, None


def dostupnie_vihodi(mt):
    N, M = len(mt), len(mt[0])
    exits = []
    for x in range(N):
        if mt[x][0] == '.':
            exits.append((x, 0))
        if mt[x][M - 1] == '.':
            exits.append((x, M - 1))
    for y in range(M):
        if mt[0][y] == '.':
            exits.append((0, y))
        if mt[N - 1][y] == '.':
            exits.append((N - 1, y))
    return exits


N, M = 8, 8
m = sozdanie_massiva(N, M)
m, start = real(m)

exits = dostupnie_vihodi(m)

result = poisk_vihoda_luchego(m, start)
for row in m:
    print(' '.join(row))
print("\nВозможные выходы:", exits)
print("Откуда старт:", start)
print("Итоговый результат: Сущ-ет ли выход | Количество выходов | Ближайший выход:", result)