# Define three variables for the LaunchCode shuttle - one for the starting fuel level, 
# another for the number of astronauts aboard, and the third for the altitude the shuttle reaches.

fuel_level = 0
astronauts = 0
altitude = 0

# Exercise #1: Construct while loops to do the following:
  # a. Query the user for the starting fuel level. Validate that the user enters a positive, 
  # integer value greater than 5000 but less than 30000. 
while fuel_level <= 4999 or fuel_level >= 30001:
   fuel_level = int(input('Enter Fuel Level: '))
   if fuel_level <= 4999:
      print("That isn't enough fuel!")
   elif fuel_level >= 30001:
      print("That is too much fuel!")
   else:
      print('Fuel Tanks Ready!')

# b. Use a second loop to query the user for the number of astronauts (up to a maximum of 7). Validate the entry.
while astronauts <= 0 or astronauts >= 8:
   astronauts = int(input('Enter Crew Count: '))
   if astronauts <= 0:
      print("Someone's gotta fly this thing!")
   elif astronauts >= 8:
      print("That's gunna be tight!")
   else:
      print('Crew Aboard.')
  
  
# c. Use a final loop to monitor the fuel status and the altitude of the shuttle. 
# Each iteration, decrease the fuel level by 100 units for each astronaut aboard.
# Also, increase the altitude by 50 kilometers.
while fuel_level-100*astronauts >= 0:
   altitude += 50
   fuel_level -= 100*astronauts

# Exercise #2: Print the result with the phrase, The shuttle gained an altitude of ___ km and has ___ kg of fuel left.
#  Fill in the blanks with the altitude and fuel level values.
print('The shuttle gained an altitude of',altitude, 'km and has', fuel_level, 'kg of fuel left.')
if altitude >= 2000:
   print('Orbit achieved!')
else:
   print("Failed to reach orbit. :(")
# If the altitude is 2000 km or higher, add “Orbit achieved!” Otherwise add, “Failed to reach orbit.”