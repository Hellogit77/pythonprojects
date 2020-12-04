# Get values from a .py file
import listofvariables
print(listofvariables.name)
print(listofvariables.race)

print("break")
# Get values from ANY file
file1 = open("listofvariables.txt", 'w') # w or r 
file1.write("asldfkajsldkfjasdklfjadklfj")
file1.close()