""" CECS 277 – Lab 6 – Class Relationships
10/15/2025
    Group 4
    Student 1: Thanh Phat Bui
    Student 2: Ha Gia Bao Hoang
Description: Rad Racer: Create a game where the user must choose a vehicle, either a Car, Motorcycle, or Truck and then
race against the remaining choices. On each turn, a vehicle may choose to go fast, slow, or to
use a special move. The vehicles race on a track that has obstacles in the way. If the vehicle is
going fast, then it will crash, if it is going slow, then it can maneuver around the obstacle. The
special moves are “Nitro Boost” for the car, which makes the car go 1.5x faster, “Wheelie” for
the motorcycle, which makes it go 2x faster, but has a chance of falling over, and “Ram” for the
truck, which makes it go 2x faster and also allows it to bash through an obstacle. Whichever
vehicle reaches the finish first wins the race."""
from car import Car
from motocycle import Motocycle
from truck import Truck
import random
import check_input
def main():
    # Initialize track lanes; each lane is a list of 100 characters representing the track.
    lanes = [
        ['-'] * 100,
        ['-'] * 100,
        ['-'] * 100
    ]

    # Add two obstacles per lane at random positions (1 to 99).
    for row in range(3):
        for num_obstacle in range(2):
            lanes[row][random.randint(1,99)] = '0'
    # Display game title and instructions.
    print("Rad Racer!")
    print("Choose a vehicle and race it down the track (Player = 'P'). Slow down for obsatcle ('0') or else you'll crash")
    print("1. Lightning Car - a fast car. Speed: 7. Special: Nitro Boost (1.5x speed)")
    print("2. Swift Bike - a speedy motorcycle. Speed: 8. Special: Wheelie (2x speed but there's a chance you'll wipe out).")
    print("3. Behemoth Truck - a heavy truck. Speed: 6. Special: Ram (2x speed and it smashes through obstacles).")
    # Prompt player to choose a vehicle
    option = check_input.get_int_range("Choose your vehicle (1-3): ", 1,3)
    option -= 1

    vehicle = []
    opponents = []

    # Initialize vehicle objects based on player choice.
    match option: 
        case 0: 
            vehicle = [
                Car("Lighning Car", "P", 30),
                Motocycle("Swift Bike", "M", 20),
                Truck("Behemoth Truck", "T", 25)
            ]
        case 1: 
            vehicle = [
                Car("Lighning Car", "C", 30),
                Motocycle("Swift Bike", "P", 20),
                Truck("Behemoth Truck", "T", 25)
            ]

        case 2: 
            vehicle = [
                Car("Lighning Car", "C", 30),
                Motocycle("Swift Bike", "M", 20),
                Truck("Behemoth Truck", "P", 25)
            ]
    # Main game loop
    while True:
        # Display gameplay screen
        for lane in range(3):
            print(vehicle[lane])

        # Draw the track for each lane with vehicles positioned on it.
        for row in range(len(lanes)):
            for column in range(len(lanes[row])):
                if (vehicle[row].position == column):
                    print(vehicle[row].initial, end= '')
                else:
                    print(lanes[row][column],end='')
            print()
        # Check if any vehicle has reached the finish line.
        if(vehicle[0].position == 99 or vehicle[1].position == 99 or vehicle[2].position == 99):
            sorted(vehicle, key = lambda x: x.position, reverse= True)
            print(f"1st Place: {vehicle[0]}")
            print(f"2nd Place: {vehicle[1]}")
            print(f"3rd Place: {vehicle[2]}")
            break
        # Get input from user
        choice = check_input.get_int_range("Choose action (1.Fast, 2. Slow, 3. Special Move): ", 1,3)

        match choice: 
                case 1: 
                    # track the previous position by *
                    lanes[option][vehicle[option].position] = '*'
                    # call the fast function
                    # the obs_loc is the index of the first '0' found starting from the vehicle's position
                    try:
                        print(vehicle[option].fast(lanes[option].index('0',vehicle[option].position)))
                    except ValueError:
                        print(vehicle[option].fast(100))

                    if(vehicle[option].position >= 99):
                        lanes[option][99] = vehicle[option].initial
                        continue
                    # Round up the position and set the current position as initial
                    lanes[option][round(vehicle[option].position)] = vehicle[option].initial
                case 2: 
                    # track the previous position by *
                    lanes[option][round(vehicle[option].position)] = '*'
                    # call the fast function
                    # the obs_loc is the index of the first '0' found starting from the vehicle's position
                    try:
                        print(vehicle[option].slow(lanes[option].index('0',round(vehicle[option].position))))
                    except ValueError:
                        vehicle[option].slow(100)

                    if(vehicle[option].position >= 100):
                        lanes[option][99] = vehicle[0].initial
                        continue
                    # Round up the position and set the current position as initial
                    lanes[option][round(vehicle[option].position)] = vehicle[option].initial
                case 3: 
                    # track the previous position by *
                    lanes[option][round(vehicle[option].position)] = '*'
                    # call the fast function
                    # the obs_loc is the index of the first '0' found starting from the vehicle's position
                    try:
                        print(vehicle[option].special_move(lanes[option].index('0',round(vehicle[option].position))))
                    except ValueError:
                        vehicle[option].special_move(100)

                    if(vehicle[option].position >= 100):
                        lanes[option][99] = vehicle[option].initial
                        continue
                        # Round up the position and set the current position as initial
                    lanes[option][round(vehicle[option].position)] = vehicle[option].initial
        chance = random.random()
        for index, opponent in enumerate(vehicle): 
            if(opponent.initial == vehicle[option].initial):
                continue
            if(chance < 0.3):
                lanes[index][round(opponent.position)] = '*'
                # call the fast function
                # the obs_loc is the index of the first '0' found starting from the vehicle's position
                try:
                    print(opponent.fast(lanes[index].index('0',round(opponent.position))))
                except ValueError:
                    opponent.fast(100)

                if(opponent.position >= 100):
                    lanes[index][99] = opponent.initial
                    continue
                    # Round up the position and set the current position as initial
                lanes[index][round(opponent.position)] = opponent.initial
            elif 0.3 < chance < 0.6:
                lanes[index][round(opponent.position)] = '*'
                # call the fast function
                # the obs_loc is the index of the first '0' found starting from the vehicle's position
                try:
                    print(opponent.special_move(lanes[index].index('0',round(opponent.position))))
                except ValueError:
                    opponent.special_move(100)

                if(opponent.position >= 100):
                    lanes[index][99] = opponent.initial
                    continue
                    # Round up the position and set the current position as initial
                lanes[index][round(opponent.position)] = opponent.initial
            else: 
                lanes[index][round(opponent.position)] = '*'
                # call the fast function
                # the obs_loc is the index of the first '0' found starting from the vehicle's position
                try:
                    print(opponent.slow(lanes[index].index('0',round(opponent.position))))
                except ValueError:
                    opponent.slow(100)

                if(opponent.position >= 100):
                    lanes[index][99] = opponent.initial
                    continue
                    # Round up the position and set the current position as initial
                lanes[index][round(opponent.position)] = opponent.initial
                    
if __name__ == "__main__":
    main()