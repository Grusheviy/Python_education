# Задача №17. Общее обсуждение
# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.

# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

# list = [1, 1, 2, 0, -1, 3, 4, 4]
# list_of_unique_numbers = []
# unique_numbers = set(list)

# for list in unique_numbers:
#     list_of_unique_numbers.append(list)
# print(list_of_unique_numbers)

list_1 = [1, 1, 2, 0, -1, 3, 4, 4]
unique_numbers = list(set(list_1))
print(unique_numbers)
print(len(unique_numbers))