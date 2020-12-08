# Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке.

with open('text.txt') as f:
    lines = f.readlines()
print('Количество строк:' , len(lines))
for num_lines, line in enumerate(lines, start= 1):
    print('{} Строка содержит - {} слов'. format(num_lines, len(line.split())))


