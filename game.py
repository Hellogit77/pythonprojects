# Author: Amber Lee
# Contact: cryptoboxcomics@gmail.com
# A fun little python game

name = input("What is your name?")
age = int(input("What is your age?"))
your_age_in_hundred_years = age+100
likes_pineapple_on_pizza = True

likes_pineapple_on_pizza_equals_true = likes_pineapple_on_pizza == True
print(likes_pineapple_on_pizza_equals_true)

print("Hi, " + name + "!")
print("Your age is " + str(age) + " but in 100 years, you are going to be " + str(your_age_in_hundred_years))


if(likes_pineapple_on_pizza):
    print("Hello")
if(likes_pineapple_on_pizza == True):
    print("Hello")