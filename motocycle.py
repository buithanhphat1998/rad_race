from vehicle import Vehicle
import random
class Motocycle(Vehicle):
    def __init__(self, name, initial, speed):
        """
        Initialize the Motocycle object by calling the parent Vehicle class constructor.
        
        Parameters:
        - name: The name of the motorcycle.
        - initial: The label/initial representing the motorcycle on the track.
        - speed: The base speed of the motorcycle.
        """
        super().__init__(name, initial, speed)


    def slow(self, obs_loc):
        """
        Perform the 'slow' action, which moves the motorcycle cautiously to avoid obstacles.

        Parameters:
        - obs_loc: The position of the next obstacle on the track.

        Returns:
        - A string describing the result of the action.
        """
        # Adjust speed for slow movement (75% of base speed +/- 1)
        self._speed = random.randint(int(self._speed * 0.75) - 1, int(self._speed) + 1)
        unit = self._speed
        # Update the motorcycle's position, ensuring it doesn't exceed the finish line.
        self._position = min(self._position + unit, 99)
        # Check if the motorcycle successfully dodges the obstacle.
        if(self._position >= obs_loc):
            return f"{self._name} slowly dodges obstacle and moves {unit} units!"
        else:
            return f"{self._name} slowly moves {unit} units!"     
        
    def special_move(self, obs_loc):
        """
        Perform the 'Wheelie' special move, which moves the motorcycle at 2x speed with a chance of losing control.

        Parameters:
        - obs_loc: The position of the next obstacle on the track.

        Returns:
        - A string describing the result of the special move.
        """
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
