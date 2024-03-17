def print_triangular_numbers(n):        #Using Code from textbook and making it my own
    """ Print all triangular numbers <=n """
    ss  = 0
    v = 1
    while v <= n:
        ss = ss + v
        v = v + 1
        print(v-1, "\t", ss)
    print()
    return ss

def print_triangular_numbers2(n):       #Using for loop
    """ Prints all triangular number <= n """
    count = 0
    v = 1
    for i in range(n):
        count = count + v
        v = v + 1
        print(v-1, "\t", count)
    print()
    return n


print_triangular_numbers(5)
print_triangular_numbers2(5)
