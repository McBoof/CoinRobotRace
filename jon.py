from robot_base import RobotBase
import random

class Jon(RobotBase):
    def __init__(self, x, y):
        super().__init__(x, y, "Jon")
        self.patrol_route = [(5, 5), (25, 5), (25, 25), (5, 25)]
        self.current_target = 0
    
    def getMoveDirection(self):
        """Jon moves randomly"""
        return random.randint(0, 3)
