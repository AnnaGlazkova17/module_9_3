first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

zp = zip(first, second)
first_result = []
for elem in zp:
    if len(elem[0]) != len(elem[1]):
        first_result.append(abs(len(elem[0]) - len(elem[1])))

multy = []
for i in range(len(first)):
    multy.append((first[i], second[i]))
second_result = (len(x[0]) == len(x[1]) for x in multy)
print(first_result)
print(list(second_result))