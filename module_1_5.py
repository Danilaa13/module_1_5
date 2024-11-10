immutable_var = (1,2,3, "string", True)
#immutable_var[1] = False
#immutable_var.append(4)
#immutable_var.extend(['string', 5])
# Кортеж является неизменяемым объектом и служит в качестве хранилища значений
print(immutable_var)
mutable_list = ['football', 'swimming','boxing','tennis']
mutable_list[0] = 'cycling'
mutable_list.append(True)
mutable_list[2] = 2
mutable_list.extend(['string', 3])
print(mutable_list)