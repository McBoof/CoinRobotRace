from robot_base import RobotBase
import random

class Zak(RobotBase):
    def __init__(self, x, y):
        super().__init__(x, y, "Zak")
        self.clockwise = True
    
    def getMoveDirection(self):
        """Zak moves randomly"""
        return random.randint(0, 3)
    

