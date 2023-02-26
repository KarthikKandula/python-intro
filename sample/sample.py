
def ignore_3(*arg):
    total = 0
    for val in arg:
        if val == 3:
            continue
        total += val
    return total

def sum(*arg):
    total = 0
    for val in arg:
        total += val
    return total

# add = sum(1,2,3,4)
# print(add)
# add = sum(4,5)
# print(add)
# add = sum(6,7,8)
# print(add)
# add = sum([1, 2, 3])
# print(add)
