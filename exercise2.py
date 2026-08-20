#START

smokers = {"Avi Ron", "Sara Kim", "Ben Azulay", "Nina Fox"}
ride_bikes = {"Sara Kim", "Tom Green", "Nina Fox"}
ride_motorcycles = {"Avi Ron", "Ben Azulay", "Nina Fox", "Eli Stone"}
likes_skyjump = {"Avi Ron", "Nina Fox", "Dana Wolf"}

print("suspects: ", smokers|likes_skyjump|ride_bikes|ride_motorcycles)
print()
print("clues:")
print("1. The suspect SMOKES")
print("2. The suspect likes SKYDIVING")
print("3. The suspect rides a BIKE or a MOTORCYCLE")
print("4. The suspect is NOT someone who ride BOTH bike and motorcycle")
print()
print("guilty: ", smokers&likes_skyjump&(ride_bikes^ride_motorcycles))

#STOP