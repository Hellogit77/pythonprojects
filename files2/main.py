import os
try:
    # if the file does not exist, 
    # then it would throw an IOerror
    filename = 'anotherfile'
    f = open(filename, 'rU')
    f.write("blahblahblah")
    f.close()
    print("Successful!")
# Control jumps directly to here if the above
# throws an error
except IOError:
    print("Problem reading: " + filename)
# In any case, the code here continues