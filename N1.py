import csv

with open('vacancy.csv', encoding='UTF-8') as file:
    data = list(csv.DictReader(file, delimiter=';'))


'''#streams;artist_name;track_name;date

def t(music):
    d, m, g, = music['date'].split('.')
    Ln = len(music['artist_name'])
    Ls = len(music['track_name'])
    rg = 



with open('songs.csv', encoding='UTF-8') as file:
    data = list(csv.DictReader(file, delimiter=';'))
    print(data[:3])
    for songer in data:
        chis, mes, year = songer['date'].split('.')
        if int(chis) <= 1 and int(mes) <= 1 and int(year) <= 2002:
            print(f'{songer["track_name"]} - {songer["artist_name"]} - ')
'''
