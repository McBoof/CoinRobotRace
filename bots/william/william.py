from robot_base import RobotBase
import random

class William(RobotBase):
    def __init__(self, x, y):
        super().__init__(x, y, "William")

    def getMoveDirection(self):
        # Get current position
        my_x, my_y = self.x, self.y

        # Get list of coins from game instance
        coins = self.game_instance.coins

        if not coins:
            # No coins visible, move randomly but safely
            safe_dirs = [d for d in range(4) if self.movementAllowed(d)]
            if safe_dirs:
                return random.choice(safe_dirs)
            return 0

        # Find closest coin by Manhattan distance
        def manhattan_distance(coin):
            return abs(coin[0] - my_x) + abs(coin[1] - my_y)

        closest_coin = min(coins, key=manhattan_distance)
        coin_x, coin_y = closest_coin

        possible_directions = []

        # Check directions that move closer to the coin and are allowed

        if coin_y < my_y and self.movementAllowed(0):  # North
            possible_directions.append(0)
        if coin_x > my_x and self.movementAllowed(1):  # East
            possible_directions.append(1)
        if coin_y > my_y and self.movementAllowed(2):  # South
            possible_directions.append(2)
        if coin_x < my_x and self.movementAllowed(3):  # West
            possible_directions.append(3)

        if possible_directions:
            # Choose randomly among all valid directions that move closer
            return random.choice(possible_directions)

        # No allowed directions toward the coin; move randomly but safely
        safe_dirs = [d for d in range(4) if self.movementAllowed(d)]
        if safe_dirs:
            return random.choice(safe_dirs)

        # No moves possible; stay put or default direction
        return 0

    def celebrate(self):
        return f"{self.name} got a coin!"

    def bashDirection(self):
        return random.randint(0, 3)

    def getBashedInsult(self):
        return "walloped"
