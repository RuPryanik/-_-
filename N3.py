import csv

with open('vacancy.csv', encoding='UTF-8', newline='') as file:
    data = list(csv.DictReader(file, delimiter=';'))
    print(data[0])
    vac = input()
    while vac != 'None':
        for work in data:
            if vac in work['Company']:
                print(f"В {work['Company']} найдена вакансия: {work['Role']}. З/п составит: {work['Salary']}")
        else:
            print('К сожалению, ничего не удалось найти')
        vac = input()