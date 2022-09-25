#Второе задание: Выдать количество записей, у которых в поле Название строка длиннее 30 символов.
import csv
with open("books.csv") as f:
    f_reader = csv.DictReader(f, delimiter = ';')
    count = 0
    for row in f_reader:
        if len(row['Название']) > 30:
            count += 1
    print(f'Записей, с названием больше 30 символов - {count}.')
