import csv

with open('songs.csv', encoding='UTF-8') as file:
    data = list(csv.DictReader(file, delimiter=';'))
    artists = {}
    for singer in data:
        artists[singer['artist_name']] = artists.get(singer['artist_name'], 0) + 1
    print(artists)
    for singer in artists:
        print(singer)
        break