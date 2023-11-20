'''
Измените знак каждого элемента списка на противоположный:
'''
t1_list1 = [1, 2, 3, 4, 5]  # [-1, -2, -3, -4, -5]
t1_list2 = [1, -2, 3, -4, 5]  # [-1, 2, -3, 4, -5]
t1_list3 = []  # []
'''
print([i*-1 for i in t1_list1])
print([i*-1 for i in t1_list2])
print([i*-1 for i in t1_list3])
'DONE'
'''

'''
Дан массив целых чисел. На основе данного массива получите массив, где первый 
элемент — это количество положительных чисел, а второй элемент — сумма отрицательных чисел.
'''
'''
t2_list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]  # [10, -65]
t2_list2 = [0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14]  # [8, -50]
t2_list3 = [1]  # [1, 0]
t2_list4 = [-1]  # [0, -1]
t2_list5 = [0, 0, 0, 0, 0, 0, 0, 0, 0]  # [0, 0]
#count = 0
#negativ_sum = 0
count = negativ_sum = 0
for i in t2_list5:
    if i > 0:
        count +=1
    else:
        negativ_sum += i    
print([count,negativ_sum])
'DONE'  
'''

'''
Возьмите массив и удалите каждый второй элемент из массива. Всегда сохраняйте 
первый элемент и начинайте удаление со следующего элемента. Попробуйте написать более одного решения задачи.
'''
t3_list1 = ['Hello', 'Goodbye', 'Hello Again']  # ['Hello', 'Hello Again']
t3_list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # [1, 3, 5, 7, 9]
t3_list3 = [[1, 2]]  # [[1, 2]]

print([el for i, el in enumerate(t3_list1) if not i % 2])
print([el for i, el in enumerate(t3_list2) if not i % 2])
print([el for i, el in enumerate(t3_list3) if not i % 2])

print(t3_list1[::2])
print(t3_list2[::2])
print(t3_list3[::2])

rem_list = []
for i, el in enumerate(t3_list3):
    if i % 2 != 0:
        rem_list.append(el)
for i in rem_list:
    t3_list3.remove(i)
print(t3_list3)


