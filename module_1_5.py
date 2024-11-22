immutable_var = (1,2,'Win',False)
print(immutable_var)
#immutable_var[1]=100
#print(immutable_var) #кортеж не поддерживает обращение по элементам.
mutable_list = ([66,1,2],0)
print(mutable_list)
mutable_list[0][0]=1
print(mutable_list)