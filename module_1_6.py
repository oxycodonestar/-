my_dict = {'anton': 2002, 'danya': 1999, 'aleks': 2005,}
print(my_dict['danya'])
my_dict['dasha'] = 1989
print(my_dict)
my_dict.update({'login': 1212, 
                'password': 4444})
print(my_dict)
my_dict.pop('anton')
print(my_dict)

my_set = {1, 2, 3, 1, 2, 3, 'hello', ('Привет, я люблю Python')}
print(my_set)
my_set.add('hello world')
my_set.discard(1)
print(my_set)
