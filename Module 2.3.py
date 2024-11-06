
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
а = 0
while а < len(my_list):
        if my_list[а] >= 0:
            if my_list[а] != 0:
                print(my_list[а])
            а = а + 1
            continue
        else:
            break