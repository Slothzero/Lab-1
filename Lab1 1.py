import csv
with open("books.csv") as f:
    f_reader = csv.DictReader(f, delimiter = ';')
    count = 0
    for row in f_reader:
        count += 1
    print(f'Всего в файле {count} записей.')
