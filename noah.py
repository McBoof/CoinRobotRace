from robot_base import RobotBase
import random

class Noah(RobotBase):
    def __init__(self, x, y):
        super().__init__(x, y, "Noah")
        self.last_direction = 0
        self.move_counter = 0
    
    def getMoveDirection(self):
        """Noah moves in a pattern: goes straight for 3 moves, then turns right"""
        self.move_counter += 1
        if self.move_counter >= 3:
            self.last_direction = (self.last_direction + 1) % 4
            self.move_counter = 0
        return self.last_direction
    
    def speak(self):
        return "Building patterns!"
    
    def celebrate(self):
        return "Noah's plan worked!"
    
    def setIcon(self):
        return (255, 100, 100)  # Red
