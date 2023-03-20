# Задача №21. Решение в группах
# Напишите программу для печати всех уникальных значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
# Примечание: Список словарей задан изначально.
# Пользователь его не вводит
'''
dictionary = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},{"VI": "S005"},
              {"VII": " S005 "}, {" V ":" S009 "}, {" VIII":" S007 "}]
unique_keys = set()
for dict in dictionary:
    for key in dict:
        unique_keys.add(dict[key].strip())
print(unique_keys)
'''
dictionary = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},{"VI": "S005"},
              {"VII": " S005 "}, {" V ":" S009 "}, {" VIII":" S007 "}]
unique_keys = set()
for dict in dictionary:
    for values in dict.values():
        unique_keys.add(values.strip())
print(unique_keys)
        