from robot_base import RobotBase
import random

class Nathan(RobotBase):
    def __init__(self, x, y):
        super().__init__(x, y, "Nathan")
        self.target_x = random.randint(0, 29)
        self.target_y = random.randint(0, 29)
    
    def getMoveDirection(self):
        """Nathan moves randomly"""
        return random.randint(0, 3)
    

