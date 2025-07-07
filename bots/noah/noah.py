from robot_base import RobotBase
import random

class Noah(RobotBase):
    def __init__(self, x, y):
        super().__init__(x, y, "Noah")
    
    def getMoveDirection(self):
        """Noah moves randomly, avoiding walls"""
        # Check for coins in all directions (as an example of using isCoinInDirection)
        coin_distances = []
        for direction in range(4):
            distance = self.isCoinInDirection(direction)
            if distance > 0:
                coin_distances.append((direction, distance))
        
        # If there are coins nearby (within 5 blocks), move toward the closest one
        if coin_distances:
            coin_distances.sort(key=lambda x: x[1])  # Sort by distance
            closest_direction = coin_distances[0][0]
            if self.movementAllowed(closest_direction):
                return closest_direction
        
        # Otherwise, move randomly while avoiding walls
        attempts = 0
        while attempts < 10:  # Prevent infinite loop
            direction = random.randint(0, 3)
            if self.movementAllowed(direction):
                return direction
            attempts += 1
        return 0  # Default fallback
    
    def celebrate(self):
        """Noah got a coin"""
        return f"{self.name} got a coin!"
    
    def getBashedInsult(self):
        """Noah's bash insult"""
        return "smashed"