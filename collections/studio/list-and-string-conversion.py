proto_list1 = "3,6,9,12"
proto_list2 = "A;C;M;E"
proto_list3 = "space delimited string"
proto_list4 = "Comma-spaces, might, require, typing, caution"

strings = [proto_list1, proto_list2, proto_list3, proto_list4]

# a) Use the 'in' method to check to see if the words in each string are separated by
# commas (,), semicolons (;) or just spaces.

#Determine delimiter for proto_list1
for string in strings:
    if ", " in string:
        print("{} contains a comma-space as the delimiter.".format(string))
    elif " " in string:
        print("{} contains a space as the delimiter.".format(string))
    elif ";" in string: 
        print("{} contains a semicolon as the delimiter.".format(string))
    elif "," in string:
        print("{} contains a comma as the delimiter.".format(string))

# b) If the string uses commas to separate the words, split it into an array,
#  reverse the entries, and then join the array into a new comma separated string.
for string in strings:
    if "," in string:
        split_string = string.split(",")
        reversed_string = split_string[::-1]
        new_list = ',' .join(reversed_string)
        print(new_list)

# c) If the string uses semicolons to separate the words, split it into an array,
#  alphabetize the entries, and then join the array into a new comma separated string.
for string in strings:
    if ";" in string:
        split_string = string.split(";")
        ordered_string = sorted(split_string)
        new_list = ','.join(ordered_string)
        print(new_list)

# d) If the string uses spaces to separate the words, split it into an array,
#  reverse alphabetize the entries, and then join the array into a new space separated string.
for string in strings:
    if " " in string:
        split_string = string.split(" ")
        ordered_string = sorted(split_string, reverse=True)
        new_list = ' '.join(ordered_string)
        print(new_list)

# e) If the string uses ‘comma spaces’ to separate the list, modify your code to produce the same result as part “b”,
#  making sure that the extra spaces are NOT part of the final string.
for string in strings:
    if ", " in string:
        split_string = string.split(", ")
        reversed_string = split_string[::-1]
        new_list = ',' .join(reversed_string)
        print(new_list)