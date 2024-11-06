immutable_var=1,2,'a','b'
print('Immutable tuple:',immutable_var)
#immutable_var[1]='c'#не поддерживается выбор символа."immutable_var[1]='c'. TypeError: 'tuple' object does not support item assignment"
mutable_list=([1,2],'a','b','Modified')
print('Mutable list:',mutable_list)
mutable_list[0][0]=5
print('Mutable list:',mutable_list)
