import csv


def rus(name):
    alphabet = 'ёйцукенгшщзхъфывапролджэячсмитьбюЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ'
    for let in name:
        if let in alphabet:
            return True
    else:
        return False


with open('songs.csv', encoding='UTF-8') as file:
    data = list(csv.DictReader(file, delimiter=';'))
    russian_artists, foreign_artists = [], []
    for singer in data:
        if rus(singer["artist_name"]) and singer["artist_name"] not in russian_artists:
            russian_artists.append(singer["artist_name"])
        else:
            if singer["artist_name"] not in foreign_artists and singer["artist_name"] not in russian_artists:
                foreign_artists.append(singer["artist_name"])
    print(f"Количество российских исполнителей: {len(russian_artists)}")
    print(f"Количество иностранных исполнителей: {len(foreign_artists)}")

