from robot_base import RobotBase
import random

class William(RobotBase):
    def __init__(self, x, y):
        super().__init__(x, y, "William")
        self.preferred_direction = random.randint(0, 3)
    
    def getMoveDirection(self):
        """William prefers one direction but occasionally changes"""
        if random.random() < 0.8:  # 80% chance to go preferred direction
            return self.preferred_direction
        else:
            # 20% chance to go random direction
            return random.randint(0, 3)
    
    def speak(self):
        return "Staying focused!"
    
    def celebrate(self):
        return "William's focus pays off!"
    
    def setIcon(self):
        return (255, 200, 100)  # Orange
