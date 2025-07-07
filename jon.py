from robot_base import RobotBase
import random

class Jon(RobotBase):
    def __init__(self, x, y):
        super().__init__(x, y, "Jon")
        self.patrol_route = [(10, 10), (90, 10), (90, 90), (10, 90)]
        self.current_target = 0
    
    def getMoveDirection(self):
        """Jon follows a patrol route"""
        target_x, target_y = self.patrol_route[self.current_target]
        
        # Check if we've reached the current target
        if self.x == target_x and self.y == target_y:
            self.current_target = (self.current_target + 1) % len(self.patrol_route)
            target_x, target_y = self.patrol_route[self.current_target]
        
        # Move toward current target
        if self.x < target_x:
            return 1  # East
        elif self.x > target_x:
            return 3  # West
        elif self.y < target_y:
            return 2  # South
        else:
            return 0  # North
    
    def speak(self):
        return "On patrol!"
    
    def celebrate(self):
        return "Jon's patrol finds treasure!"
    
    def setIcon(self):
        return (100, 150, 255)  # Light Blue
