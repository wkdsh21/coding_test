from collections import defaultdict
def solution(genres, plays):
    answer = []
    album_dict = defaultdict(list)
    # 딕셔너리에 장르별로 추가
    for i,(genre,play) in enumerate(zip(genres,plays)):
        album_dict[genre].append((i,play))
    # 정렬을 위한 list화
    album_dict_items = list(album_dict.items())
    # 재생순 내림차순, 인덱스 오름차순 정렬
    for genre,al_list in album_dict_items:
        al_list.sort(key=lambda x:(-x[1],x[0]))
    # 장르별 총 재생수 합 내림차순 정렬
    album_dict_items.sort(key=lambda x:-sum([i[1] for i in x[1]]))
    # 장르별 최대 2개까지 answer에 추가   
    for genre, al_list in album_dict_items:
        answer.extend([i[0] for i in al_list[:2]])
    return answer
