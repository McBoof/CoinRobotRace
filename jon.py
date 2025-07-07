from robot_base import RobotBase
import random

class Jon(RobotBase):
    def __init__(self, x, y):
        super().__init__(x, y, "Jon")
    
    def getMoveDirection(self):
        """Jon moves randomly"""
        return random.randint(0, 3)
    
    def celebrate(self):
        """Jon got a coin"""
        return f"{self.name} got a coin!"
