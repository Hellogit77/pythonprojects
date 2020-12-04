# decision = ""
# while(decision == "" or decision != "1" or decision != "2"):
#     print("Please type in 1 or 2")
#     decision = input("> ")
#     if (decision == "1"):
#         print("decision 1")
#     elif (decision == "2"):
#         print("decision 2")
#     else:
#         print("Only 1 or 2 accepted")

shopping_list = ["potatoes", "ramen", "coca-cola"]
print(shopping_list)

# generally more readable
for item in shopping_list:
    print(item)

# does the same thing, but a bit uglier
for i in range(0,3):
    print(shopping_list[i])

