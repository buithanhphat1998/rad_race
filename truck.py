from vehicle import Vehicle
import random

class Truck(Vehicle):

    def __init__(self, name, initial, speed):
        """
        Initialize the Truck object by calling the parent Vehicle class constructor.
        
        Parameters:
        - name: The name of the truck.
        - initial: The label/initial representing the truck on the track.
        - speed: The base speed of the truck.
        """
        super().__init__(name, initial, speed)

    def special_move(self, obs_loc):
        """
        Perform the 'Ram' special move, which moves the truck at 2x speed and allows it to smash through obstacles.

        Parameters:
        - obs_loc: The position of the next obstacle on the track.

        Returns:
        - A string describing the result of the special move.
        """
        unit = 0 # Distance the truck will move.
        if(self._energy >= 15): # Check if the truck has enough energy for the special move.
            self._energy -= 15 # Deduct 15 energy for the special move.
            # Double the truck's speed for the special move.
            self._speed = (2 * self._speed)
            unit = self._speed
        else: 
            unit = 1 # If energy is insufficient, move only 1 unit.
        
        self._position = min(self._position + unit, 99)
        
        # Check crash
        if(self._position >= obs_loc):
            return f"{self._name} using ram to move {unit} units and ramed obstacle"
        else:
            return f"{self._name} using ram to move {unit} units"