import random
from robot_base import RobotBase


class zac(RobotBase):
    def __init__(self, x, y, name="zac"):
        super().__init__(x, y, name)
        self.target_route = []  # Planned coin collection route
        self.current_target_index = 0

    def speak(self):
        return f"{self.name} collecting coins!"

    def celebrate(self):
        return f"{self.name} scored!"

    def getBashedInsult(self):
        return "bam!"

    def bashDirection(self):
        # Randomly pick a bash direction (0=N,1=E,2=S,3=W)
        return random.randint(0, 3)

    def calculate_coin_interest(self, coins):
        """
        Calculate the interest for each coin.
        Interest = sum over other coins of (60 / Manhattan distance to other coin)
        coins: list of (x,y) tuples for coin positions
        Returns: dict mapping coin -> interest score (float)
        """
        interest_scores = {}
        for i, c1 in enumerate(coins):
            interest = 0.0
            for j, c2 in enumerate(coins):
                if i == j:
                    continue
                dist = abs(c1[0] - c2[0]) + abs(c1[1] - c2[1])
                if dist == 0:
                    continue
                interest += 60 / dist
            interest_scores[c1] = interest
        return interest_scores

    def plan_route(self):
        """
        Plan a route for collecting coins:
        1. Find coin with highest interest.
        2. Then add coins greedily based on shortest Manhattan distance from last added coin.
        Updates self.target_route with ordered list of coins.
        Resets current_target_index to 0.
        """
        if not hasattr(self.game_instance, "coins") or len(self.game_instance.coins) == 0:
            self.target_route = []
            self.current_target_index = 0
            return

        coins = list(self.game_instance.coins)
        interest_scores = self.calculate_coin_interest(coins)

        # 1. Find coin with highest interest
        start_coin = max(interest_scores, key=interest_scores.get)

        route = [start_coin]
        remaining = set(coins)
        remaining.remove(start_coin)

        # 2. Greedy add coins based on shortest distance to last coin in route
        while remaining:
            last = route[-1]
            next_coin = min(remaining, key=lambda c: abs(c[0] - last[0]) + abs(c[1] - last[1]))
            route.append(next_coin)
            remaining.remove(next_coin)

        self.target_route = route
        self.current_target_index = 0

    def getMoveDirection(self):
        """
        Decide the next move direction towards the current target coin.
        If no coins or route is empty, move randomly.
        """
        if not hasattr(self.game_instance, "coins") or len(self.game_instance.coins) == 0:
            # No coins visible, move randomly but allowed
            attempts = 0
            while attempts < 10:
                direction = random.randint(0, 3)
                if self.movementAllowed(direction):
                    return direction
                attempts += 1
            return 0  # default north if stuck

        # Replan route if coins changed or no route planned
        if not self.target_route or self.current_target_index >= len(self.target_route):
            self.plan_route()

        # If route empty after plan (no coins), move randomly
        if not self.target_route:
            return random.randint(0, 3)

        target = self.target_route[self.current_target_index]

        # If reached the coin, move to next target
        if (self.x, self.y) == target:
            self.current_target_index += 1
            if self.current_target_index >= len(self.target_route):
                self.plan_route()
                if not self.target_route:
                    return random.randint(0, 3)
            target = self.target_route[self.current_target_index]

        dx = target[0] - self.x
        dy = target[1] - self.y

        possible_moves = []

        if abs(dx) > abs(dy):
            # Prioritize horizontal move
            if dx > 0 and self.movementAllowed(1):
                possible_moves.append(1)
            elif dx < 0 and self.movementAllowed(3):
                possible_moves.append(3)
            if dy > 0 and self.movementAllowed(2):
                possible_moves.append(2)
            elif dy < 0 and self.movementAllowed(0):
                possible_moves.append(0)
        else:
            # Prioritize vertical move
            if dy > 0 and self.movementAllowed(2):
                possible_moves.append(2)
            elif dy < 0 and self.movementAllowed(0):
                possible_moves.append(0)
            if dx > 0 and self.movementAllowed(1):
                possible_moves.append(1)
            elif dx < 0 and self.movementAllowed(3):
                possible_moves.append(3)

        # If no prioritized moves allowed, fallback to any allowed move
        if not possible_moves:
            for direction in [0, 1, 2, 3]:
                if self.movementAllowed(direction):
                    possible_moves.append(direction)

        if possible_moves:
            return random.choice(possible_moves)
        else:
            return 0  # stuck, no move allowed