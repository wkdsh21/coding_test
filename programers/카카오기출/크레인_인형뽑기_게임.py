def solution(board, moves):
    answer = 0
    stack = []
    for i in moves:
        for j in range(len(board)):
            if board[j][i - 1] != 0:
                if stack and stack[-1] == board[j][i - 1]:
                    stack.pop()
                    answer += 1
                else:
                    stack.append(board[j][i - 1])
                board[j][i - 1] = 0
                break
    return answer * 2
