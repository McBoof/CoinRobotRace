from robot_base import RobotBase
import random

class Katie(RobotBase):
    def __init__(self, x, y):
        super().__init__(x, y, "Katie")
        self.aggressive = True
        self.last_move = 0
    
    def getMoveDirection(self):
        """Katie moves aggressively, changing direction often"""
        # Very high chance to change direction
        if random.random() < 0.7:  # 70% chance to change direction
            new_direction = random.randint(0, 3)
            while new_direction == self.last_move:
                new_direction = random.randint(0, 3)
            self.last_move = new_direction
            return new_direction
        else:
            return self.last_move
    
    def speak(self):
        return "Fast and fierce!"
    
    def celebrate(self):
        return "Katie's aggression wins!"
    
    def setIcon(self):
        return (255, 100, 50)  # Red-Orange
