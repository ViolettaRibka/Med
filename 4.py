#Списки

lst = [1, 3, 4, 2, 0, 123, 321, 222]

print(lst)

# Добавление элемента:
lst.append(1111)
lst.append(3_333)

print(lst)

#Расшифровка списка
#lst2 = ['first', 'second', 'third']

# lst.extend(lst2)

print(lst)

# Сортировка. Метод НИЧЕГО не возвращает
lst.sort(key=lambda x: len(str(x)))
print(f'neversed={lst}')

last = lst.pop()

print(f'last element={last}, list after second pop={lst}')

print(321 in lst, 555 in lst)

