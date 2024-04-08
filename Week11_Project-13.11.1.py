def reverse_file_lines(file, newfile):
    """Creates a newfile with the lines of file reversed"""
    f = open(file, "r")
    content = f.readlines()     #list of lines in file
    f.close()
    x =len(content)                  #creates variable for the for loop
    reciprocal = len(content)        #creates variable for reciprocal line number
    newfile = open(newfile, "w")     #create new file
    for line in range(x):
        reciprocal -= 1
        newfile.write(content[reciprocal])  #writes reverse line of file in newfile
    newfile.close()


reverse_file_lines("Week11-Project-13-10-1.txt", "Reversed_file")
