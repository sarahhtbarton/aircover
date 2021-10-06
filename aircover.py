import math

def print_ac(size):

    a_thickness = 'A' * math.ceil(size/4)
    top_indentation = ' ' * (size + math.floor((size-1)/8) - 1)

    for i in range(size):
        if i == 0: #top row
            print(top_indentation + a_thickness)
        elif i == math.floor(size/2): #middle row
            print((' ' * (size - i - 1)) + a_thickness + ('A'*((i-1)*2)) + a_thickness)
        else: #all other rows
            print((' ' * (size - i - 1)) + a_thickness + (' '*((i-1)*2)) + a_thickness)

print_ac(1)
print_ac(3)
print_ac(4)
print_ac(5)
print_ac(7)
print_ac(13)
print_ac(29)
