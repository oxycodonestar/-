#immutable_var = 1, "строка", 3.14, True
#print(immutable_var)
#immutable_var [0] = 5 
# Кортеж нельзя изменить, т.к он содержит набор фиксированных значений, которые не могут изменяться после создания

mutable_list = [0, 5, "i love iqos"]
print(mutable_list)
mutable_list [0] = 3
print(mutable_list) 
mutable_list [2] = "smoking badly"
print(mutable_list)