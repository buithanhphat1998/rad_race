from vehicle import Vehicle
import random

class Car(Vehicle):
    def __init__(self, name, initial, speed):
        super().__init__(name, initial, speed)
    """nitro boost – passes in the location of the next
    obstacle (if there is one). If there is sufficient energy (>= 15), deduct 15 energy and
    move the car at 1.5x speed +/- 1. If there is an obstacle, then it will crash and stops on
    that space, otherwise it moves the randomized distance. If there was not sufficient
    energy, then only move up one space. Return a string that describes the event that
    occurred with the name of the car and the distance traveled"""

    def special_move(self, obs_loc):
        unit = 0 
        if(self._energy >= 15): 
            self._energy -= 15

            self._speed = random.randint(int(1.5 * self._speed) - 1, int(1.5 * self._speed) + 1)
            unit = self._speed
        else: 
            unit = 1
        
        self._position = min(self._position + unit, 99)
        # if the location is greater than the obstacle, then it crashed
        if(self._position >= obs_loc):
            self._position = obs_loc
            # return the fstring 
            return f"{self._name} using nitro boost to move {unit} units and crashed into obstacle"
        else:
            self._position = min(self._position + unit, 99)
            return f"{self._name} using nitro boost to move {unit} units"
    