from robot_base import RobotBase
import random

class Zak(RobotBase):
    def __init__(self, x, y):
        super().__init__(x, y, "Zak")
        self.clockwise = True
    
    def getMoveDirection(self):
        """Zak moves in circles"""
        if self.clockwise:
            # Move clockwise: North -> East -> South -> West
            directions = [0, 1, 2, 3]
        else:
            # Move counter-clockwise: North -> West -> South -> East
            directions = [0, 3, 2, 1]
        
        # Change direction every few moves
        if random.random() < 0.1:  # 10% chance to reverse direction
            self.clockwise = not self.clockwise
        
        return directions[random.randint(0, 3)]
    
    def speak(self):
        return "Going in circles!"
    
    def celebrate(self):
        return "Zak's circle worked!"
    
    def setIcon(self):
        return (100, 255, 255)  # Cyan
