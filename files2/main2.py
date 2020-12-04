import os
try:
    fd = "Ziyo.txt"
    file = open(fd, 'w+')
    text = file.read()
    print(text)
    os.close(file)
except TypeError:
    print("There is an issue with type")
except IOError:
    print("There is an issue reading the file")
except:
    print("No idea how to handle that")