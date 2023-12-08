##Conditional Statement

##condition = True

# condition = input("Light ON-Y OFF-N: ")

# print(condition == "Y")
# print(condition == "N")

# if condition == "Y":
#     print("lights on")
# elif condition == "N":
#     print("lights off")
# else:
#     print("invalid")


# ------------------------------------------

# nested if
# print("WELCOME TO PIZZA HUT")
# print("We serve some pizza list given below")
# print("------------------")
# print("NON-VEG")
# print("1 : chicken pizza")
# print("2 : tandoori pizza")
# print("3 : mutton pizza")
# print("------------------")
# print("VEG")
# print("4 : mushroom pizza")
# print("5 : corn pizza")
# print("6 : panner pizza")
# print("------------------")

# user = int(input("Choose your pizza: "))
# totalAmount = 0

# if user == 1:
#     print("chicken pizza cost is $5")
#     totalAmount += 5
#     cheese = 0
#     topins = 0
#     isCheese = input("Do you want cheese to add Y/N: ")
#     isTopins = input("Do you want topins to add Y/N: ")
#     if isCheese == "Y":
#         cheese = 2
#         totalAmount += cheese
#     if isTopins == "Y":
#         topins = 1
#         totalAmount += topins

#     # print(f"Your Total Amount is:${totalAmount}")
#     print(f"Your Amount for cheese is: ${cheese}")
#     print(f"Your Amount for topins is: ${topins}")
#     print(f"Your Total Amount is: ${totalAmount}")


# elif user == 2:
#     print("tandoori pizza cost is $6")
# elif user == 3:
#     print("mutton pizza cost is $4")
# elif user == 4:
#     print("mushroom pizza cost is $3")
# elif user == 5:
#     print("corn pizza cost is $2")
# elif user == 6:
#     print("panner pizza cost is $1")
# else:
#     print("Sorry invalid key")


if False:
    if True:
        print(1)
    else:
        print(2)

else:
    print(0)
