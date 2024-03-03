y = int(input("Enter any number to find out what day of the week it is! : "))

def return_weekday(x):      #turn a number between 0 and 6 into a weekday
    if x == 0:
        print("Sunday")
    elif x == 1:
        print("Monday")
    elif x == 2:
        print("Tuesday")
    elif x == 3:
        print("Wednesday")
    elif x == 4:
        print("Thursday")
    elif x == 5:
        print("Friday")
    elif x == 6:
        print("Saturday")
    

def ReturnAnyToWeekday(z):      #make any number into a weekday
    if (z<7) and (z>0):
        return_weekday(z)
    else:
        return_weekday(z % 7)
    
    



ReturnAnyToWeekday(y)
