import csv
file = open("BookList.txt", "w+")
with open("books.csv") as f:
    f_reader = csv.DictReader(f, delimiter = ';')
    i = 1
    for row in f_reader:
        if row['Дата поступления'][6:10] == '2016' and i <= 20:
            file.write(f'{i}. {row["Автор"]}. {row["Название"]} - 2016 год\n')
            i += 1
file.close()


