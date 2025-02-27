# Choose a mode of transportation based on the distance (e.g., <3 km: Walk, 3-15 km: Bike, >15 km: Car).

Total_Dist = int(input("Enter the total distance: "))

if Total_Dist < 3:
    Mode_Of_Transportation = 'Walk'
elif Total_Dist < 15:
    Mode_Of_Transportation = 'Bike'
else:
    Mode_Of_Transportation = 'Car'
print("The mode of transportation is", Mode_Of_Transportation)