#Write a function named readposint that uses the input dialog to prompt the
#user for a positive integer and then checks the input to confirm that it meets
#the requirements. It should be able to handle inputs that cannot be converted
#to int, as well as negative ints, and edge cases
#(e.g. when the user closes the dialog, or does not enter anything at all.)

#Week 14 19.6.1 Project

def readposint():       #does not need try...except statement
    """Checks input to see if it is a positive integer"""
    n = input("Choose a positive intiger: ")
    

    #check n to be positive int
    if n == "":
        print("'{0}' is not a valid positive integer.".format(n))
    elif int(float(n))!= n:
        if int(float(n))>0:
            print("'{0}' is a positive integer.".format(n))
        else:
            print("'{0}' is not a valid positive integer.".format(n))
    elif " " in n:
        print("'{0}' is not a valid positive integer.".format(n))
    elif int(n)<=0:
        print("'{0}' is not a valid positive integer.".format(n))

            

readposint()

