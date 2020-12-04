# Importing packages in python
import os

os.system("ls -lah")
print(os.environ['envresource'])


superpower = os.environ['environmentalpower']
print("The superpower you got from the environment is " + superpower)

# Pre script
os.mkdir(superpower)
print("Directory regarding your superpower has been created!")

# Do things
os.system("touch " + superpower + "/thunder")
os.system("touch " + superpower + "/lightning")
os.system("ls -lah " + superpower)

# Post script
os.system("rm -rf " + superpower)