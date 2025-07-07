from robot_base import RobotBase
import random

class William(RobotBase):
    def __init__(self, x, y):
        super().__init__(x, y, "William")
    
    def getMoveDirection(self):
        """William moves randomly"""
        return random.randint(0, 3)
    
    def celebrate(self):
        """William got a coin"""
        return f"{self.name} got a coin!"

