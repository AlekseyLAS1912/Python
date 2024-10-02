my_dict = {'Вася': 1995, 'Петя': 1990, 'Рома': 2008}
print(my_dict)
print(my_dict['Петя'])
my_dict.update({'Ваня':2005, 'Кирилл': 1996})
print(my_dict)
del my_dict ['Петя']
print(my_dict.get('Петя'))
print(my_dict)

my_set = {1, 3, 7, 8.2, 7, 1, 345, 345, True, 'Айсберг'}
print(my_set)
my_set.update({'Снег', 829})
print(my_set)
my_set.discard(7)
print(my_set)