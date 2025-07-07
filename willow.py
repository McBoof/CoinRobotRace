from robot_base import RobotBase
import random

class Willow(RobotBase):
    def __init__(self, x, y):
        super().__init__(x, y, "Willow")
        self.zigzag_horizontal = True
        self.steps_taken = 0
    
    def getMoveDirection(self):
        """Willow moves randomly"""
        return random.randint(0, 3)
    

