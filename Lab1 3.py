#Третье задание: Реализовать поиск книги по автору, использовать ограничение на выдачу в зависимости от варианта.
# вариант 5 - нет ограничений
import csv
with open("books.csv") as f:
    f_reader = csv.DictReader(f, delimiter = ";")
    count = 0
    name = input("Имя автора - ")
    for row in f_reader:
        if row['Автор'] == name:
            print(', '.join(row.values()))
            count += 1
    if count == 0:
        print('Автор не найден')

