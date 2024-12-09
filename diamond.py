# make a n=3 diamond
#   *
#  ***
# *****
#  ***
#   *

#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *

# n=3 = 3 rows, 5 columns
# n=4 = 4 rows, 7 columns
# n=5 = 5 rows, 9 columns
# columns = n*2-1
n = 26

d = {}
rows = n * 2 - 1
columns = n * 2 - 1 # 5
# 0 1 [2] 3 4
# 0 [1 2 3] 4
L = n - 1 # 2
R = n - 1 # 2
for i in range(rows):
    d[i] = [0] * columns

reverse = False
letter = 65
for val_arr in d.values():
    for i, v in enumerate(val_arr):
        if L <= i <= R:
            val_arr[i] = chr(letter)

    if L == 0:
        reverse = True

    if not reverse:
        letter += 1
        L -= 1
        R += 1
    else:
        letter -= 1
        L += 1
        R -= 1

# iterate through d
for val_arr in d.values():
    for val in val_arr:
        if val == 0:
            print(' ', end='')
        else:
            print(val, end='')
    print()
