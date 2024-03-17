import sys

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

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

def print_triangular_numbers3(n):       #Using formula from internet adapted to work in python
    """ Prints triangular numbers 1 through n """
    count = 0
    v = 0
    t= 0
    while v <= n-1:
        count = count + 1
        v = v + 1
        t = int((v**2 +v)/2)
        print(count, "\t", t)
    print()
    return t

print_triangular_numbers(5)
print_triangular_numbers2(5)
print_triangular_numbers3(5)

test(print_triangular_numbers(5) == 15)
test(print_triangular_numbers2(5) == 15)
test(print_triangular_numbers3(5) == 15)
