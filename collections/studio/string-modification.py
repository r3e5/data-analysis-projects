my_string = "LaunchCode"


# a) Use string methods to remove the first three characters from the string and add them to the end.
partial_string = my_string[:3]
new_string = (my_string[3:] + partial_string)

# Use a template literal to print the original and modified string in a descriptive phrase.
formated_string = 'I can move letters in {} around, like this: {}'.format(my_string,new_string)
print(formated_string)

# b) Modify your code to accept user input. Query the user to enter the number of letters that will be relocated.
# user_input = input('Please enter the number of letters to be relocated:')
# int_input = int(user_input)
# if int_input >=1:
#     partial_string = my_string[:int_input]
#     new_string = (my_string[int_input:] + partial_string)
#     formated_string = 'You can move letters in {} around, like this: {}'.format(my_string,new_string)
#     print(formated_string)
# c) Add validation to your code to deal with user inputs that are longer than the word. 
# In such cases, default to moving 3 characters. Also, the template literal should note the error.
user_input = input('Please enter the number of letters to be relocated: ')
int_input = int(user_input)
# while user_input == 0:
#     user_input = input('Please enter the number of letters to be relocated: ')
#     int_input = int(user_input)
if int_input > 0 and int_input < 10:
    partial_string = my_string[:int_input]
    new_string = (my_string[int_input:] + partial_string)
    formated_string = 'You can move letters in {} around, like this: {}'.format(my_string,new_string)
    print(formated_string)
elif int_input == 0:
    user_input = input('Input must be more than Zero: ')
    int_input = int(user_input)
    partial_string = my_string[:int_input]
    new_string = (my_string[int_input:] + partial_string)
    formated_string = 'You can move letters in {} around, like this: {}'.format(my_string,new_string)
    print(formated_string)
else:
    partial_string = my_string[:3]
    new_string = (my_string[3:] + partial_string)
    formated_string = "That is too many! we'll use 3 letters from {} , like this: {}".format(my_string,new_string)
    print(formated_string)