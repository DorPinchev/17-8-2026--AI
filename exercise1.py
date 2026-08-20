#START

smokers = {"John Smith", "Maya Levi", "Noam Cohen", "Liam Patel"}
ride_bikes = {"Maya Levi", "Omer Halevi", "Liam Patel"}
ride_motorcycles = {"John Smith", "Noam Cohen", "Rina Gold"}
likes_skyjump = {"John Smith", "Rina Gold", "Dina Bar"}

print("suspects: ", smokers|likes_skyjump|ride_bikes|ride_motorcycles)
print()
print("clues:")
print("1. The suspect SMOKES")
print("2. The suspect likes SKYDIVING")
print("3. The suspect rides a BIKE or a MOTORCYCLE")
print()
print("guilty: ", smokers&likes_skyjump&(ride_bikes|ride_motorcycles))

#STOP