from robot_base import RobotBase
import random

class Eden(RobotBase):
    def __init__(self, x, y):
        super().__init__(x, y, "Eden")
    
    def getMoveDirection(self):
        """Eden moves towards the closest coin"""
        # Check for coins in all directions
        north_distance = self.isCoinInDirection(0)  # Check north
        east_distance = self.isCoinInDirection(1)   # Check east
        south_distance = self.isCoinInDirection(2)  # Check south
        west_distance = self.isCoinInDirection(3)   # Check west
        
        # Find the direction with the closest coin
        distances = [north_distance, east_distance, south_distance, west_distance]
        
        # Filter out directions with no coins (distance 0) and find the shortest
        valid_directions = []
        for i, distance in enumerate(distances):
            if distance > 0:  # There's a coin in this direction
                valid_directions.append((i, distance))
        
        if valid_directions:
            # Sort by distance and get the closest direction
            valid_directions.sort(key=lambda x: x[1])
            best_direction = valid_directions[0][0]
            
            # Check if we can move in that direction
            if self.movementAllowed(best_direction):
                return best_direction
        
        # If no coins found or can't move toward closest coin, move randomly but avoid walls
        attempts = 0
        while attempts < 10:  # Prevent infinite loop
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
