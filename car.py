from vehicle import Vehicle
import random

class Car(Vehicle):
    def __init__(self, name, initial, speed):
        """
        Initialize the Car object by calling the parent Vehicle class constructor.
        
        Parameters:
        - name: The name of the car.
        - initial: The label/initial representing the car on the track.
        - speed: The base speed of the car.
        """
        super().__init__(name, initial, speed)
    """nitro boost – passes in the location of the next
    obstacle (if there is one). If there is sufficient energy (>= 15), deduct 15 energy and
    move the car at 1.5x speed +/- 1. If there is an obstacle, then it will crash and stops on
    that space, otherwise it moves the randomized distance. If there was not sufficient
    energy, then only move up one space. Return a string that describes the event that
    occurred with the name of the car and the distance traveled"""

    def special_move(self, obs_loc):
        """
        Perform the 'Nitro Boost' special move, which moves the car at 1.5x speed +/- 1 if energy is sufficient.

        Parameters:
        - obs_loc: The position of the next obstacle on the track.

        Returns:
        - A string describing the result of the special move.
        """
        unit = 0 # Distance the car will move
        if(self._energy >= 15): # Check if the car has enough energy for the special move.
            self._energy -= 15  # Deduct 15 energy for the special move.

            # Calculate the boosted speed.
            self._speed = random.randint(int(1.5 * self._speed) - 1, int(1.5 * self._speed) + 1)
            unit = self._speed
        else: 
            # If energy is insufficient, move only 1 unit.
            unit = 1
        # Update the car's position, ensuring it doesn't exceed the finish line.
        self._position = min(self._position + unit, 99)
        # if the location is greater than the obstacle, then it crashed
        if(self._position >= obs_loc):
            self._position = obs_loc
            # return the fstring 
            return f"{self._name} using nitro boost to move {unit} units and crashed into obstacle"
        else:
            # If no crash, move the car forward by the calculated distance.
            self._position = min(self._position + unit, 99)
            return f"{self._name} using nitro boost to move {unit} units"
    