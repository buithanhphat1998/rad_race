from vehicle import Vehicle
import random
class Motocycle(Vehicle):
    def __init__(self, name, initial, speed):
        super().__init__(name, initial, speed)


    def slow(self, obs_loc):
        self._speed = random.randint(int(self._speed * 0.75) - 1, int(self._speed) + 1)
        unit = self._speed
        self._position = min(self._position + unit, 99)
        
        if(self._position >= obs_loc):
            return f"{self._name} slowly dodges obstacle and moves {unit} units!"
        else:
            return f"{self._name} slowly moves {unit} units!"     
        
    def special_move(self, obs_loc):
        unit = 0 
        if(self._energy >= 15): 
            self._energy -= 15

            # There is 75% chance that the motocycle will move at 2x speed. 
            chance = random.random()
            # If under 75 % percent
            if(chance <= 0.75): 
                # set 2x the speed +/- 1
                self._speed = random.randint(int(2 * self._speed) - 1, int(2 * self._speed) + 1)
                # The unit move is the self._speed
                unit += self._speed
                # increase the location by the unit
                self._position = min(self._position + unit, 99)
            else: 
                # other 25%, set the location randomly
                self._position = random.randint(self._position,99)
        else: 
            unit = 1
            self._position = min(self._position + unit, 99)
            print(f"{self._name} is out of energy")
        
        # Check crash
        if(self._position >= obs_loc):
            # if it crash, then the number of unit moved is the obstacle location - the current location
            unit = self._position - obs_loc
            # set current location to obstacle location
            self._position = obs_loc
            return f"{self._name} using wheelie to move {unit} units and crashed into obstacle"
        # If not crash, then return units moved
        else:
            return f"{self._name} using wheelie to move {unit} units"
