# def convert(minutes):
#     minutes = minutes*60
#     return minutes
# print(convert(5))

# def remainder(x,y):
#      remain=x%y
#      return remain
# print(remainder(6,6))

# def circuit_power(voltage,current):
#     return voltage*current
# print

# def find_odd(lst):
#     lst=[1,2,3,2,2,3,1]
#     print(lst[2])
def find_odd(lst):
    for val in lst:
        if lst.count(val) % 2 ==1:
            return lst
    a=[1,2,2,1,3,3,1,5,5]
    print(find_odd(a))


        
       
    