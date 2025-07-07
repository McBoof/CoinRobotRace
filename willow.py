from robot_base import RobotBase
import random

class Willow(RobotBase):
    def __init__(self, x, y):
        super().__init__(x, y, "Willow")
        self.zigzag_horizontal = True
        self.steps_taken = 0
    
    def getMoveDirection(self):
        """Willow moves in a zigzag pattern"""
        self.steps_taken += 1
        
        if self.zigzag_horizontal:
            # Move horizontally
            if self.steps_taken % 5 == 0:  # Change direction every 5 steps
                self.zigzag_horizontal = False
            return random.choice([1, 3])  # East or West
        else:
            # Move vertically
            if self.steps_taken % 3 == 0:  # Change direction every 3 steps
                self.zigzag_horizontal = True
            return random.choice([0, 2])  # North or South
    
    def speak(self):
        return "Zigzagging along!"
    
    def celebrate(self):
        return "Willow's zigzag wins!"
    
    def setIcon(self):
        return (150, 255, 150)  # Light Green
