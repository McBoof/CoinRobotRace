from robot_base import RobotBase
import random

class Kate(RobotBase):
    def __init__(self, x, y):
        super().__init__(x, y, "Kate")
        self.conservative = True
    
    def getMoveDirection(self):
        """Kate moves conservatively, avoiding edges"""
        valid_directions = []
        
        # Check which directions are safe (not too close to edges)
        if self.y > 2:  # Not too close to top
            valid_directions.append(0)  # North
        if self.x < 27:  # Not too close to right
            valid_directions.append(1)  # East
        if self.y < 27:  # Not too close to bottom
            valid_directions.append(2)  # South
        if self.x > 2:  # Not too close to left
            valid_directions.append(3)  # West
        
        if valid_directions:
            return random.choice(valid_directions)
        else:
            return random.randint(0, 3)  # If stuck, move randomly
    
    def speak(self):
        return "Playing it safe!"
    
    def celebrate(self):
        return "Kate's caution works!"
    
    def setIcon(self):
        return (255, 150, 150)  # Pink
