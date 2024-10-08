from collections import deque


def solution(maps):
    # 초기화
    answer = -1
    max_y, max_x = len(maps), len(maps[0])
    visit = [[0] * max_x for _ in range(max_y)]
    dxy = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    visit[0][0] = 1
    x, y = 0, 0
    que = deque([(y, x, 1)])
    # BFS 진행 거리도 같이 데크에 넣어줌
    while que:
        y, x, d = que.popleft()
        for dy, dx in dxy:
            if (
                0 <= dy + y < max_y
                and 0 <= dx + x < max_x
                and maps[dy + y][dx + x] == 1
                and visit[dy + y][dx + x] == 0
            ):
                if dy + y == max_y - 1 and dx + x == max_x - 1:
                    return d + 1
                que.append((dy + y, dx + x, d + 1))
                visit[dy + y][dx + x] = 1
    return answer
