from robot_base import RobotBase
import random

class Eden(RobotBase):
    def __init__(self, x, y):
        super().__init__(x, y, "Eden")
        self.spiral_step = 0
        self.spiral_direction = 0
        self.steps_in_direction = 0
        self.max_steps = 1
    
    def getMoveDirection(self):
        """Eden moves randomly"""
        return random.randint(0, 3)
    

