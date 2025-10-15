from car import Car
from motocycle import Motocycle
from truck import Truck
import random
import check_input
def main():
    lanes = [
        ['-'] * 100,
        ['-'] * 100,
        ['-'] * 100
    ]

    for row in range(3):
        for num_obstacle in range(2):
            lanes[row][random.randint(1,99)] = '0'
    print("Rad Racer!")
    print("Choose a vehicle and race it down the track (Player = 'P'). Slow down for obsatcle ('0') or else you'll crash")
    print("1. Lightning Car - a fast car. Speed: 7. Special: Nitro Boost (1.5x speed)")
    print("2. Swift Bike - a speedy motorcycle. Speed: 8. Special: Wheelie (2x speed but there's a chance you'll wipe out).")
    print("3. Behemoth Truck - a heavy truck. Speed: 6. Special: Ram (2x speed and it smashes through obstacles).")
    option = check_input.get_int_range("Choose your vehicle (1-3): ", 1,3)
    option -= 1

    vehicle = []
    opponents = []
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

    while True:
        # Display gameplay screen
        for lane in range(3):
            print(vehicle[lane])

        for row in range(len(lanes)):
            for column in range(len(lanes[row])):
                if (vehicle[row].position == column):
                    print(vehicle[row].initial, end= '')
                else:
                    print(lanes[row][column],end='')
            print()
        
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