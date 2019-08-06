my_dict = {}
for i in range(1, 51):
    if i % 2 == 0 and i % 7 == 0:
        my_dict[i] = i*2
    elif i % 2 == 0:
        my_dict[i] = i + 1
    elif i % 7 == 0:
        my_dict[i] = i - 1
    else:
        my_dict[i] = i

print(my_dict)

