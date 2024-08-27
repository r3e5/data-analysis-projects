# 1. Declare and assign the variables here:
ShuttleName = "Determination"
ShuttleSpeed = 17500
DistanceMars = 225000000
DistanceMoon = 384400
MilesPerKM = 0.621
# 2. Use print() to print the 'type' each variable. Print one item per line.
print("ShuttleName",type(ShuttleName))
print("ShuttleSpeed",type(ShuttleSpeed))
print("DistanceMars",type(DistanceMars))
print("DistanceMoon", type(DistanceMoon))
print("MilesPerKM", type(MilesPerKM))

# Code your solution to exercises 3 and 4 here:
MilesToMars = DistanceMars * MilesPerKM
HoursToMars = DistanceMars / ShuttleSpeed
DaysToMars = HoursToMars / 24

print(ShuttleName,"will take",DaysToMars,"days to reach Mars.")
# Code your solution to exercise 5 here
MilesToMoon = DistanceMoon* MilesPerKM
HoursToMoon = DistanceMoon / ShuttleSpeed
DaysToMoon = HoursToMoon / 24

print(ShuttleName,"will take",DaysToMoon,"days to reach the Moon.")
print("austin"'\n'"rees")