from robot_base import RobotBase
import random

class Nathan(RobotBase):
    def __init__(self, x, y):
        super().__init__(x, y, "Nathan")
    
    def getMoveDirection(self):
        """Nathan moves randomly"""
        return random.randint(0, 3)
    
    def celebrate(self):
        """Nathan got a coin"""
        return f"{self.name} got a coin!"
