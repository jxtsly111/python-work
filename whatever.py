def find_odd(lst):
    for val in lst:
        if lst.count(val) % 2 ==1:
            return val
a=[1,2,2,1,3,3,1,5,5]
print(find_odd(a))

