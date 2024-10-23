def solution(new_id):
    new_id = new_id.lower()
    id = list(new_id)
    index = []
    save = 0
    for i in id:
        if not (
            (ord(i) >= 48 and ord(i) <= 57)
            or (ord(i) >= 97 and ord(i) <= 122)
            or ord(i) == 45
            or ord(i) == 46
            or ord(i) == 95
        ):
            index.append(i)
    for i in index:
        while i in id:
            id.remove(i)
    index = []
    add = 0
    print(id)
    for i in range(len(id)):
        print(i)
        if ord(id[i]) == 46:
            save += 1
        else:
            save = 0
        if save >= 2:
            index.append(i)
    for i in index:
        del id[i - add]
        add += 1
    if len(id) != 0 and ord(id[0]) == 46:
        del id[0]
    if len(id) != 0 and ord(id[-1]) == 46:
        del id[-1]
    if len(id) == 0:
        id.append("a")
    if len(id) >= 16:
        del id[15:]
    if ord(id[-1]) == 46:
        del id[-1]
    if len(id) <= 2:
        while len(id) <= 2:
            id.append(id[-1])
    id = "".join(id)
    answer = id
    return answer
