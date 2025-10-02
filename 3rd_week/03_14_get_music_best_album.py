def get_melon_best_album(genre_array, play_array):
    # 구현해보세요!
    # 1. dict에 장르별로 얼마나 재생횟수를 가지고 있는가
    # 2. dict에 장르별로 어느 인덱스에 몇 번 재생횟수를 가지고 있는가

    n = len(genre_array)
    genre_total_play_dict = {}
    genre_index_play_array_dict = {}
    # {key : [(index, play), (), () ] dictionary 안 배열 안 튜플 형태

    for i in range(n):
        genre = genre_array[i]
        play = play_array[i]

        if genre in genre_total_play_dict:
            genre_total_play_dict[genre] +=play
            genre_index_play_array_dict[genre].append([i, play])
        else:
            genre_total_play_dict[genre] = play
            genre_index_play_array_dict[genre] = [[i, play]]

    print(genre_total_play_dict)
    print(genre_index_play_array_dict)
    print(genre_total_play_dict.items())

    sorted_genre_play_array = sorted(genre_total_play_dict.items(), key=lambda x: x[1], reverse=True)
    print("-->",sorted(genre_total_play_dict.items(), key=lambda x: x[1], reverse=True))

    result = []

    for genre, total_play in sorted_genre_play_array:
        print(genre, total_play)
        print(genre_index_play_array_dict[genre])
        sorted_genre_index_play_array = sorted(genre_index_play_array_dict[genre], key=lambda x: x[1], reverse=True)
        print('==>', sorted_genre_index_play_array)
        # 장르별로 제일 잘나가는 2곡만 넣기
        genre_song_count = 0
        for i, play in sorted_genre_index_play_array:
            if genre_song_count >= 2:
                break
            result.append(i)
            genre_song_count += 1

    return result


print("정답 = [4, 1, 3, 0] / 현재 풀이 값 = ", get_melon_best_album(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
print("정답 = [0, 6, 5, 2, 4, 1] / 현재 풀이 값 = ", get_melon_best_album(["hiphop", "classic", "pop", "classic", "classic", "pop", "hiphop"], [2000, 500, 600, 150, 800, 2500, 2000]))