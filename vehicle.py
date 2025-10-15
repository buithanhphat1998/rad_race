from abc import ABC, abstractmethod
import random

class Vehicle(ABC): 
    """Attributes: 
    ._name: vehicle name
    ._initial: vehicle's label
    ._speed: vehicle's speed
    ._position: vehicle's position
    ._energy: vehicle's power level
    """
    def __init__(self, name, initial, speed):
        self._name = name
        self._initial = initial
        self._speed = speed
        self._position = 0
        self._energy = 100
    @property
    def initial(self):
        return self._initial
    @property
    def position(self): 
        return self._position
    @property
    def energy(self): 
        return self._energy
    
    def fast(self, obs_loc):
        units = 0
        if(self._energy >=5 ): 
            self._energy -= 5
            self._speed = random.randint(self._speed -1, self._speed + 1)

            # increase unit by speed
            units += self._speed
        # if energy is less than 5, increase 1 unit        
        else: 
            units += 1
            return f"{self._name} is out of energy, move {units} units"

        self._position = min(self._position + units, 99)

        # if crash
        if(self._position > obs_loc): 
            self._position = obs_loc
            return f"{self._name} quickly moves {units} units and crashed!"
        
        return f"{self._name} quickly moves {units} units!"
           
        
            
    def slow(self, obs_loc): 
        self._speed = random.randint(int(self._speed/2) - 1, int(self._speed/2) + 1)
        unit = self._speed
        
        self._position = min(self._position + unit, 99)
        
        if(self._position > obs_loc):
            return f"{self._name} slowly dodges obstacle and moves {unit} units!"
        elif(self._position == obs_loc): 
            self._position = min(self._position + 1, 99)
            return f"{self._name} slowly dodges obstacle and moves {unit} units!"

        return f"{self._name} slowly moves {unit} units!"     

    def __str__(self):
        return f"{self._name} [Position - {self._position}, Energy - {self._energy}]"
    
    @abstractmethod
    def special_move(self, obs_loc):
        pass
