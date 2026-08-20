#START

night_shift = {"Alex", "Jordan", "Taylor", "Casey"}
access_server_room = {"Jordan", "Casey", "Morgan", "Riley"}
hardware_expert = {"Taylor", "Riley", "Casey", "Alex"}
management_role = {"Jordan", "Morgan"}

print("suspects: ", night_shift|access_server_room|hardware_expert|management_role)
print()
print("clues:")
print("1. The suspect was on the NIGHT SHIFT")
print("2. The suspect has access to the SERVER ROOM")
print("3. The suspect is a HARDWARE EXPERT")
print("4. The suspect is NOT in a MANAGMENT ROLE")
print()
print("guilty: ", (night_shift&access_server_room&hardware_expert)-management_role)
print(len((night_shift&access_server_room&hardware_expert)-management_role))
print(((night_shift&access_server_room&hardware_expert)-management_role) <= night_shift)

#STOP