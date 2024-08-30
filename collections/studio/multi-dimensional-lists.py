food = "water bottles,meal packs,snacks,chocolate"
equipment = "space suits,jet packs,tool belts,thermal detonators"
pets = "parrots,cats,moose,alien eggs"
sleep_aids = "blankets,pillows,eyepatches,alarm clocks"

# a) Use split to convert the strings into four cabinet lists. Alphabetize the contents of each cabinet.
food_split = food.split(",")
food_ordered = sorted(food_split)
food_list = ", ".join(food_ordered)

equipment_split = equipment.split(",")
equipment_ordered = sorted(equipment_split)
equipment_list = ", ".join(equipment_ordered)

pets_split = pets.split(",")
pets_ordered = sorted(pets_split)
pets_list = ", ".join(pets_ordered)

sleep_aids_split = sleep_aids.split(",")
sleep_aids_ordered = sorted(sleep_aids_split)
sleep_aids_list = ", ".join(sleep_aids_ordered)

# b) Initialize a cargo_hold list and add the cabinet lists to it. Print cargo_hold to verify its structure.
cargo_hold = [food_list,equipment_list,pets_list,sleep_aids_list]

# print(cargo_hold)

# c) Query the user to select a cabinet (0 - 3) in the cargo_hold.
# user_input = input("Please select a cabinet (0 - 3): ")
# int_cabinet = int(user_input)
# d) Use bracket notation and format to display the contents of the selected cabinet.
#   If the user entered an invalid number, print an error message.
# if int_cabinet >= 0 and int_cabinet < 4:
#     selected_cabinet = cargo_hold[int_cabinet]
#     display_cargo = 'The cabinet you selected contains: {}'.format(selected_cabinet)
#     print(display_cargo)
# elif int_cabinet < 0:
#     user_input = input("Please select a valid value between (0 - 3): ")
#     int_cabinet = int(user_input)
#     selected_cabinet = cargo_hold[int_cabinet]
#     display_cargo = 'The cabinet you selected contains: {}'.format(selected_cabinet)
#     print(display_cargo)
# elif int_cabinet >= 4:
#     user_input = input("Please select a valid value between (0 - 3): ")
#     int_cabinet = int(user_input)
#     selected_cabinet = cargo_hold[int_cabinet]
#     display_cargo = 'The cabinet you selected contains: {}'.format(selected_cabinet)
#     print(display_cargo)

# e) Modify the code to query the user for BOTH a cabinet in cargo_hold AND a particular item.
#  Use the in method to check if the cabinet contains the selected item, 
# then print “Cabinet ____ DOES/DOES NOT contain ____.”
cabinet_selection = input("Please select a cabinet (0 - 3): ")
item_selection = input("Please query for an item: ")
int_cabinet = int(cabinet_selection)
if int_cabinet >= 0 and int_cabinet < 4:
    selected_cabinet = cargo_hold[int_cabinet]
    if item_selection in selected_cabinet:
        print("Cabinet {} does contains {}.".format(selected_cabinet,item_selection))
    elif int_cabinet >= 0 and int_cabinet < 4:
        selected_cabinet = cargo_hold[int_cabinet]
        if item_selection not in selected_cabinet:
            print("I'm sorry that cabinet does not contain {}".format(item_selection))
elif int_cabinet < 0:
    selected_cabinet = cargo_hold[int_cabinet]
    if item_selection in selected_cabinet:
        print("Cabinet {} does contains {}.".format(selected_cabinet,item_selection))
    elif int_cabinet >= 0 and int_cabinet < 4:
        selected_cabinet = cargo_hold[int_cabinet]
        if item_selection not in selected_cabinet:
            print("I'm sorry that cabinet does not contain {}".format(item_selection))
elif int_cabinet >= 4:
    selected_cabinet = cargo_hold[int_cabinet]
    if item_selection in selected_cabinet:
        print("Cabinet {} does contains {}.".format(selected_cabinet,item_selection))
    elif int_cabinet >= 0 and int_cabinet < 4:
        selected_cabinet = cargo_hold[int_cabinet]
        if item_selection not in selected_cabinet:
            print("I'm sorry that cabinet does not contain {}".format(item_selection))