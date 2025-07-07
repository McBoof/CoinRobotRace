import random
import itertools
from robot_base import RobotBase

class Zac(RobotBase):
    def __init__(self, x, y, name="zac"):
        super().__init__(x, y, name)
        self.target_route = []  # Planned coin collection route (3 coins lookahead)
        self.current_target_index = 0
        self.previous_coins = set()  # Track coins from last check to detect new coins
        self.distance_cache = {}  # Cache Manhattan distances to avoid recomputation

    def speak(self):
        return f"{self.name} collecting coins!"

    def celebrate(self):
        return f"{self.name} scored!"

    def getBashedInsult(self):
        return "bam!"

    def bashDirection(self):
        # Random bash direction (0=N,1=E,2=S,3=W)
        return random.randint(0, 3)

    def manhattan_distance(self, a, b):
        # Cache distances for speed
        key = (a, b) if a <= b else (b, a)
        if key not in self.distance_cache:
            self.distance_cache[key] = abs(a[0] - b[0]) + abs(a[1] - b[1])
        return self.distance_cache[key]

    def should_recalculate_route(self, current_coins):
        """
        Return True if a new coin appeared among the 8 closest coins.
        """
        new_coins = current_coins - self.previous_coins
        if not new_coins:
            return False

        # Find 8 closest coins to current position
        sorted_coins = sorted(current_coins, key=lambda c: self.manhattan_distance((self.x, self.y), c))
        closest_coins = set(sorted_coins[:8])

        # If any new coin is in the 8 closest, recalc route
        for coin in new_coins:
            if coin in closest_coins:
                return True

        return False

    def plan_route(self):
        """
        Plan the optimal route looking 3 moves ahead by checking all permutations
        of 3 coins, choose the minimal total Manhattan distance path.

        Updates self.target_route with first 3 coins in optimal order.
        Resets current_target_index to 0.
        """
        if not hasattr(self.game_instance, "coins") or len(self.game_instance.coins) == 0:
            self.target_route = []
            self.current_target_index = 0
            self.previous_coins = set()
            return

        current_coins = set(self.game_instance.coins)

        # Clear distance cache every time to keep it fresh and small
        self.distance_cache.clear()

        # Check if we should recalc
        if self.previous_coins and not self.should_recalculate_route(current_coins):
            # No need to recalc route, keep old route
            return

        self.previous_coins = current_coins.copy()

        # If fewer than 3 coins, just plan route greedily for all coins
        if len(current_coins) <= 3:
            # Greedy shortest path for all coins
            coins = list(current_coins)
            route = []
            pos = (self.x, self.y)
            while coins:
                next_coin = min(coins, key=lambda c: self.manhattan_distance(pos, c))
                route.append(next_coin)
                pos = next_coin
                coins.remove(next_coin)
            self.target_route = route
            self.current_target_index = 0
            return

        # More than 3 coins: check all permutations of 3 coins to find minimal route
        min_distance = float('inf')
        best_route = None
        coins_list = list(current_coins)
        start_pos = (self.x, self.y)

        for combo in itertools.permutations(coins_list, 4):
            # Total distance from current position to first coin + first to second + second to third
            dist = (self.manhattan_distance(start_pos, combo[0]) +
                    self.manhattan_distance(combo[0], combo[1]) +
                    self.manhattan_distance(combo[1], combo[2]))

            if dist < min_distance:
                min_distance = dist
                best_route = combo

        self.target_route = list(best_route)
        self.current_target_index = 0

    def getMoveDirection(self):
        """
        Decide next move towards current target coin.
        If no coins or route empty, move randomly.
        Recalculate route as needed.
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

        # Plan or replan route if needed
        self.plan_route()

        if not self.target_route:
            return random.randint(0, 3)

        # If reached current target coin, advance to next coin
        target = self.target_route[self.current_target_index]
        if (self.x, self.y) == target:
            self.current_target_index += 1
            if self.current_target_index >= len(self.target_route):
                # Finished route, plan again next tick
                self.plan_route()
                if not self.target_route:
                    return random.randint(0, 3)
            target = self.target_route[self.current_target_index]

        dx = target[0] - self.x
        dy = target[1] - self.y

        possible_moves = []

        if abs(dx) > abs(dy):
            # Prioritize horizontal moves
            if dx > 0 and self.movementAllowed(1):
                possible_moves.append(1)
            elif dx < 0 and self.movementAllowed(3):
                possible_moves.append(3)
            if dy > 0 and self.movementAllowed(2):
                possible_moves.append(2)
            elif dy < 0 and self.movementAllowed(0):
                possible_moves.append(0)
        else:
            # Prioritize vertical moves
            if dy > 0 and self.movementAllowed(2):
                possible_moves.append(2)
            elif dy < 0 and self.movementAllowed(0):
                possible_moves.append(0)
            if dx > 0 and self.movementAllowed(1):
                possible_moves.append(1)
            elif dx < 0 and self.movementAllowed(3):
                possible_moves.append(3)

        # Fallback to any allowed move if none prioritized
        if not possible_moves:
            for direction in [0, 1, 2, 3]:
                if self.movementAllowed(direction):
                    possible_moves.append(direction)

        if possible_moves:
            return random.choice(possible_moves)
        else:
            return 0  # stuck, no allowed move