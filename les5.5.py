# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

with open('les5.txt', 'w', encoding=' utf-8') as f:
    nums = input('Введите числа через пробел: ')
    f.write('Введенные числа: ' + nums + '\n')
    nums = map(int, nums.split())
    sum_nums = sum(nums)
    f.write('Сумма чисел: ' + str(sum_nums))
    print('Сумма возведенных чисел: ' , sum_nums)
print('Все записано в файл')


