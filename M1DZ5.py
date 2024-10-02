immutable_var = (1, 2.5, True, 'Айсберг')
print(immutable_var)
#immutable_var [1] = 5 #кортеж является неизменяемой коллекцией. Он хранит только ссылку на список, а не сам список.

mutable_list = [1, 2.5, True, 'Айсберг']
print(mutable_list)
mutable_list [0] = 'снег'
print(mutable_list)
