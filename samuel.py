from robot_base import RobotBase
import random

class Samuel(RobotBase):
    def __init__(self, x, y):
        super().__init__(x, y, "Samuel")
    
    def getMoveDirection(self):
        """Samuel moves randomly"""
        return random.randint(0, 3)
    
    def celebrate(self):
        """Samuel got a coin"""
        return f"{self.name} got a coin!"
