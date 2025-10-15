from vehicle import Vehicle
import random

class Truck(Vehicle):
    def __init__(self, name, initial, speed):
        super().__init__(name, initial, speed)

    def special_move(self, obs_loc):
        unit = 0 
        if(self._energy >= 15): 
            self._energy -= 15

            self._speed = (2 * self._speed)
            unit = self._speed
        else: 
            unit = 1
        
        self._position = min(self._position + unit, 99)
        
        # Check crash
        if(self._position >= obs_loc):
            return f"{self._name} using ram to move {unit} units and ramed obstacle"
        else:
            return f"{self._name} using ram to move {unit} units"