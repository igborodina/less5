# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.


with open('les4.txt', encoding=' utf-8') as f:
    lines = f.readlines()

with open('les4.2.txt', 'w', encoding=' utf-8') as f:
    for line in lines:
        if '1' in line:
            line = line.replace('one', 'один')
        elif '2' in line:
            line = line.replace('two', 'два')
        elif '3' in line:
            line = line.replace('three', 'три')
        elif '4' in line:
            line = line.replace('four', 'четыре')
    f.write(line)
