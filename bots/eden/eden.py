from robot_base import RobotBase
import random

class Eden(RobotBase):
    def __init__(self, x, y):
        super().__init__(x, y, "Eden")
    
    def getMoveDirection(self):
        """Eden seeks the closest coin"""
        # Check for coins in all directions
        north_distance = self.isCoinInDirection(0)
        east_distance = self.isCoinInDirection(1)
        south_distance = self.isCoinInDirection(2)
        west_distance = self.isCoinInDirection(3)
        
        # Find the direction with the closest coin
        distances = [north_distance, east_distance, south_distance, west_distance]
        closest_direction = 0
        shortest_distance = distances[0]
        
        for i, distance in enumerate(distances):
            if distance > 0 and (shortest_distance == 0 or distance < shortest_distance):
                shortest_distance = distance
                closest_direction = i
        
        # If we found a coin, move towards it (if movement is allowed)
        if shortest_distance > 0 and self.movementAllowed(closest_direction):
            return closest_direction
        
        # Otherwise, move randomly but avoid walls
        attempts = 0
        while attempts < 10:
            direction = random.randint(0, 3)
            if self.movementAllowed(direction):
                return direction
            attempts += 1
        return 0  # Default fallback
    
    def celebrate(self):
        """Eden got a coin"""
        return f"{self.name} got a coin!"
    
    def bashDirection(self):
        """Eden picks a random direction to bash"""
        return random.randint(0, 3)
    
    def getBashedInsult(self):
        """Eden's bash insult"""
        return "eliminated"
