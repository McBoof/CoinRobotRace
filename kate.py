from robot_base import RobotBase
import random

class Kate(RobotBase):
    def __init__(self, x, y):
        super().__init__(x, y, "Kate")
        self.conservative = True
    
    def getMoveDirection(self):
        """Kate moves randomly"""
        return random.randint(0, 3)
    
    def setIcon(self):
        return (255, 150, 150)  # Pink
