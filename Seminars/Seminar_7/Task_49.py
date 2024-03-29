# Задача №49. Решение в группах
# Планеты вращаются вокруг звезд по эллиптическим орбитам.
# Назовем самой далекой планетой ту, орбита которой имеет
# самую большую площадь. Напишите функцию
# find_farthest_orbit(list_of_orbits), которая среди списка орбит
# планет найдет ту, по которой вращается самая далекая
# планета. Круговые орбиты не учитывайте: вы знаете, что у
# вашей звезды таких планет нет, зато искусственные спутники
# были были запущены на круговые орбиты. Результатом
# функции должен быть кортеж, содержащий длины полуосей
# эллипса орбиты самой далекой планеты. Каждая орбита
# представляет из себя кортеж из пары чисел - полуосей ее
# эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b,
# где a и b - длины полуосей эллипса. При решении задачи
# используйте списочные выражения. Подсказка: проще всего
# будет найти эллипс в два шага: сначала вычислить самую
# большую площадь эллипса, а затем найти и сам эллипс,
# имеющий такую площадь. Гарантируется, что самая далекая
# планета ровно одна

# def find_farthest_orbit(orbits):
#     max_area = 0
#     for r, v in orbits:
#         if r != v:
#             area = r * v * 3.14
#             if area > max_area:
#                 max_area = area
#     return max_area

# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(find_farthest_orbit(orbits))

def find_farthest_orbit(list_of_orbits):
    #arr = list(filter(lambda x:x[0]!=x[1],list_of_orbits))
    #arr_2 = list(map(lambda x:x[0]*x[1],arr))
    #max_s = max(arr_2)
    #i_max = arr_2.index(max_s)
    #return(arr[i_max])
    i_max = 0
    s_max = 0
    #a,b,d,f = (12,34,'rfdg', 23)
    #for i,cur_tuple in enumerate(list_of_orbits):
    #    print(i, end=' индекс кортежа ')
    #    print(cur_tuple)
    for i, el_tuple in enumerate(list_of_orbits):
        s_cur = el_tuple[0] * el_tuple[1]
        if el_tuple[0] != el_tuple[1] and s_max < s_cur:
            i_max = i
            s_max = s_cur
    return list_of_orbits[i_max]


orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(*find_farthest_orbit(orbits))