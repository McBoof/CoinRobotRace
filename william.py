from robot_base import RobotBase
import random

class William(RobotBase):
    def __init__(self, x, y):
        super().__init__(x, y, "William")
        self.preferred_direction = random.randint(0, 3)
    
    def getMoveDirection(self):
        """William moves randomly"""
        return random.randint(0, 3)
    
    def setIcon(self):
        return (255, 200, 100)  # Orange
