def solution(phoneBook):
    phonebook_set = set(phoneBook)
    len_set = set()
    for i in phoneBook:
        len_set.add(len(i))
    for num in len_set:
        for phone in phonebook_set:
            if num < len(phone) and phone[:num] in phonebook_set:
                return False
    return True
