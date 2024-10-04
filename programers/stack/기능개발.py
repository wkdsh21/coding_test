def solution(progresses, speeds):
    answer = []
    while progresses:
        count = len(progresses)
        for i in range(count):
            progresses[i] += speeds[i]
        for i in progresses:
            if i >= 100:
                speeds = speeds[1:]
                progresses = progresses[1:]
                # count+=1
            else:
                break
        if count != len(progresses):  # count!=0
            answer.append(count - len(progresses))  # answer.append(count)
    return answer
