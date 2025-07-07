from robot_base import RobotBase
import random

class Noah(RobotBase):
    def __init__(self, x, y):
        super().__init__(x, y, "Noah")
        self.last_direction = 0
        self.move_counter = 0
    
    def getMoveDirection(self):
        """Noah moves randomly"""
        return random.randint(0, 3)
    
    def setIcon(self):
        return (255, 100, 100)  # Red
