import pygame
import random
import time
import os
import sys
from robot_base import RobotBase

# Import all robot classes
from bots.noah.noah import Noah
from bots.zac.zac import Zac
from bots.nathan.nathan import Nathan
from bots.eden.eden import Eden
from bots.samuel.samuel import Samuel
from bots.zak.zak import Zak
from bots.william.william import William
from bots.sophia.sophia import Sophia
from bots.willow.willow import Willow
from bots.kate.kate import Kate
from bots.katie.katie import Katie
from bots.jon.jon import Jon

class Game:
    def __init__(self):
        pygame.init()
        
        # Game constants
        self.WORLD_SIZE = 30
        self.TILE_SIZE = 24
        self.WINDOW_WIDTH = self.WORLD_SIZE * self.TILE_SIZE + 200  # Extra space for UI
        self.WINDOW_HEIGHT = self.WORLD_SIZE * self.TILE_SIZE
        
        # Colors
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.GRAY = (128, 128, 128)
        self.LIGHT_GRAY = (200, 200, 200)
        self.GOLD = (255, 215, 0)
        self.GREEN = (0, 255, 0)
        self.BLUE = (0, 0, 255)
        self.RED = (255, 0, 0)
        self.LIGHT_RED = (255, 150, 150)
        
        # Initialize pygame
        self.screen = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        pygame.display.set_caption("Robot Simulation Game")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 24)
        self.small_font = pygame.font.Font(None, 18)
        
        # Game state
        self.world = [[None for _ in range(self.WORLD_SIZE)] for _ in range(self.WORLD_SIZE)]
        self.coins = []  # List of (x, y) positions
        self.robots = []
        self.speech_bubbles = []  # List of (robot, text, end_time)
        self.bash_flashes = []  # List of (x, y, end_time) for red flash effects
        self.robots_bashing = set()  # Set of robots currently bashing (can't move)
        
        # Timing
        self.last_coin_spawn = time.time()
        self.last_robot_move = time.time()
        self.last_robot_speak = time.time()
        self.last_bash_time = time.time()
        
        # Initialize robots
        self.init_robots()
        
        # Game loop control
        self.running = True
        self.game_won = False
        self.winner = None
        
    def init_robots(self):
        """Initialize all 12 robots with random starting positions"""
        robot_classes = [Noah, Zac, Nathan, Eden, Samuel, Zak, William, Sophia, Willow, Kate, Katie, Jon]
        
        for robot_class in robot_classes:
            # Find a random empty position
            while True:
                x = random.randint(0, self.WORLD_SIZE - 1)
                y = random.randint(0, self.WORLD_SIZE - 1)
                if self.world[y][x] is None:
                    break
            
            # Create robot instance
            robot = robot_class(x, y)
            robot.game_instance = self  # Give robot access to game instance
            self.robots.append(robot)
            self.world[y][x] = robot
    
    def spawn_coin(self):
        """Spawn a coin at a random empty position"""
        attempts = 0
        while attempts < 100:  # Avoid infinite loop
            x = random.randint(0, self.WORLD_SIZE - 1)
            y = random.randint(0, self.WORLD_SIZE - 1)
            
            if self.world[y][x] is None and (x, y) not in self.coins:
                self.coins.append((x, y))
                break
            attempts += 1
    
    def move_robots(self):
        """Move all robots in random order"""
        # Shuffle robots to randomize movement order
        robot_order = self.robots.copy()
        random.shuffle(robot_order)
        
        for robot in robot_order:
            if robot.alive and robot not in self.robots_bashing:
                # Get movement direction from robot
                try:
                    direction = robot.getMoveDirection()
                    if direction not in [0, 1, 2, 3]:
                        direction = random.randint(0, 3)  # Default to random if invalid
                except:
                    direction = random.randint(0, 3)  # Default to random if error
                
                # Calculate new position
                new_x, new_y = robot.x, robot.y
                if direction == 0:  # North
                    new_y = max(0, robot.y - 1)
                elif direction == 1:  # East
                    new_x = min(self.WORLD_SIZE - 1, robot.x + 1)
                elif direction == 2:  # South
                    new_y = min(self.WORLD_SIZE - 1, robot.y + 1)
                elif direction == 3:  # West
                    new_x = max(0, robot.x - 1)
                
                # Check if new position is empty or has a coin
                if self.world[new_y][new_x] is None or (new_x, new_y) in self.coins:
                    # Clear old position
                    self.world[robot.y][robot.x] = None
                    
                    # Check for coin collection
                    if (new_x, new_y) in self.coins:
                        self.coins.remove((new_x, new_y))
                        robot.score += 1
                        
                        # Check for win condition
                        if robot.score >= 10:
                            self.game_won = True
                            self.winner = robot
                            self.add_speech_bubble(robot, f"{robot.name} wins!", 5.0)
                        else:
                            # Trigger celebration
                            try:
                                celebration_text = robot.celebrate()
                                if celebration_text:
                                    self.add_speech_bubble(robot, celebration_text, 3.0)
                            except:
                                self.add_speech_bubble(robot, f"{robot.name} celebrates!", 3.0)
                    
                    # Move robot
                    robot.x, robot.y = new_x, new_y
                    self.world[new_y][new_x] = robot
    
    def robot_bash(self):
        """Make robots bash every 5 seconds"""
        for robot in self.robots:
            if robot.alive:
                try:
                    bash_dir = robot.bashDirection()
                    if bash_dir is not None:
                        # Add robot to bashing set (prevents movement this turn)
                        self.robots_bashing.add(robot)
                        
                        # Calculate bash target position
                        bash_x, bash_y = robot.x, robot.y
                        if bash_dir == 0:  # North
                            bash_y -= 1
                        elif bash_dir == 1:  # East
                            bash_x += 1
                        elif bash_dir == 2:  # South
                            bash_y += 1
                        elif bash_dir == 3:  # West
                            bash_x -= 1
                        
                        # Check if bash target is within bounds
                        if 0 <= bash_x < self.WORLD_SIZE and 0 <= bash_y < self.WORLD_SIZE:
                            # Add flash effect
                            self.bash_flashes.append((bash_x, bash_y, time.time() + 0.2))
                            
                            # Check if there's a robot at the bash position
                            target_robot = self.world[bash_y][bash_x]
                            if target_robot and target_robot != robot:
                                # Get the insult word
                                insult_word = robot.getBashedInsult()
                                
                                # Show bash message
                                bash_message = f"{robot.name} {insult_word} {target_robot.name}!"
                                self.add_speech_bubble(robot, bash_message, 3.0)
                                
                                # Transfer all coins from target to basher
                                robot.score += target_robot.score
                                target_robot.score = 0
                                
                                # Show victim's reaction
                                self.add_speech_bubble(target_robot, "Ouch!", 2.0)
                                
                except:
                    pass  # Ignore bash errors

    def robot_speak(self):
        """Make robots speak every 10 seconds"""
        for robot in self.robots:
            if robot.alive:
                try:
                    speech_text = robot.speak()
                    if speech_text:
                        self.add_speech_bubble(robot, speech_text, 3.0)
                except:
                    self.add_speech_bubble(robot, robot.name, 3.0)
    
    def add_speech_bubble(self, robot, text, duration):
        """Add a speech bubble for a robot"""
        end_time = time.time() + duration
        # Remove existing bubble for this robot
        self.speech_bubbles = [bubble for bubble in self.speech_bubbles if bubble[0] != robot]
        # Add new bubble
        self.speech_bubbles.append((robot, text, end_time))
    
    def update_speech_bubbles(self):
        """Remove expired speech bubbles"""
        current_time = time.time()
        self.speech_bubbles = [bubble for bubble in self.speech_bubbles if bubble[2] > current_time]

    def update_bash_flashes(self):
        """Remove expired bash flashes"""
        current_time = time.time()
        self.bash_flashes = [flash for flash in self.bash_flashes if flash[2] > current_time]
    
    def draw_world(self):
        """Draw the game world"""
        # Clear screen
        self.screen.fill(self.WHITE)
        
        # Draw grid
        for x in range(self.WORLD_SIZE + 1):
            pygame.draw.line(self.screen, self.LIGHT_GRAY, 
                           (x * self.TILE_SIZE, 0), 
                           (x * self.TILE_SIZE, self.WORLD_SIZE * self.TILE_SIZE))
        
        for y in range(self.WORLD_SIZE + 1):
            pygame.draw.line(self.screen, self.LIGHT_GRAY, 
                           (0, y * self.TILE_SIZE), 
                           (self.WORLD_SIZE * self.TILE_SIZE, y * self.TILE_SIZE))
        
        # Draw coins
        for coin_x, coin_y in self.coins:
            pygame.draw.circle(self.screen, self.GOLD, 
                             (coin_x * self.TILE_SIZE + self.TILE_SIZE // 2,
                              coin_y * self.TILE_SIZE + self.TILE_SIZE // 2), 
                             self.TILE_SIZE // 3)

        # Draw bash flash effects
        for flash_x, flash_y, end_time in self.bash_flashes:
            flash_rect = pygame.Rect(flash_x * self.TILE_SIZE, flash_y * self.TILE_SIZE, 
                                   self.TILE_SIZE, self.TILE_SIZE)
            pygame.draw.rect(self.screen, self.LIGHT_RED, flash_rect)
        
        # Draw robots
        for robot in self.robots:
            if robot.alive:
                # Get robot icon image
                icon_image = robot.getIcon()
                
                # Draw robot icon
                self.screen.blit(icon_image, (robot.x * self.TILE_SIZE, robot.y * self.TILE_SIZE))
                
                # Draw robot name (small text)
                name_text = self.small_font.render(robot.name[:3], True, self.BLACK)
                self.screen.blit(name_text, (robot.x * self.TILE_SIZE + 1, 
                                           robot.y * self.TILE_SIZE + 1))
    
    def draw_speech_bubbles(self):
        """Draw speech bubbles for robots"""
        for robot, text, end_time in self.speech_bubbles:
            if robot.alive:
                # Calculate bubble position
                bubble_x = robot.x * self.TILE_SIZE + self.TILE_SIZE
                bubble_y = robot.y * self.TILE_SIZE - 30
                
                # Render text
                text_surface = self.small_font.render(text, True, self.BLACK)
                text_rect = text_surface.get_rect()
                
                # Draw bubble background
                bubble_rect = pygame.Rect(bubble_x - 5, bubble_y - 5, 
                                        text_rect.width + 10, text_rect.height + 10)
                pygame.draw.rect(self.screen, self.WHITE, bubble_rect)
                pygame.draw.rect(self.screen, self.BLACK, bubble_rect, 2)
                
                # Draw text
                self.screen.blit(text_surface, (bubble_x, bubble_y))
    
    def draw_leaderboard(self):
        """Draw the leaderboard on the right side"""
        # Sort robots by score (descending)
        sorted_robots = sorted(self.robots, key=lambda r: r.score, reverse=True)
        
        # Draw leaderboard background (semi-transparent, top left)
        leaderboard_x = 10
        leaderboard_y = 10
        leaderboard_width = 180
        leaderboard_height = len(sorted_robots) * 25 + 40
        
        # Create semi-transparent surface
        leaderboard_surface = pygame.Surface((leaderboard_width, leaderboard_height))
        leaderboard_surface.set_alpha(150)  # Semi-transparent
        leaderboard_surface.fill(self.LIGHT_GRAY)
        self.screen.blit(leaderboard_surface, (leaderboard_x, leaderboard_y))
        
        pygame.draw.rect(self.screen, self.BLACK, 
                        (leaderboard_x, leaderboard_y, leaderboard_width, leaderboard_height), 2)
        
        # Draw title
        if self.game_won:
            title_text = self.font.render(f"{self.winner.name} WINS!", True, self.RED)
        else:
            title_text = self.font.render("Leaderboard", True, self.BLACK)
        self.screen.blit(title_text, (leaderboard_x + 10, leaderboard_y + 10))
        
        # Draw robot scores
        for i, robot in enumerate(sorted_robots):
            y_pos = leaderboard_y + 35 + i * 25
            score_text = self.small_font.render(f"{robot.name}: {robot.score}", True, self.BLACK)
            self.screen.blit(score_text, (leaderboard_x + 10, y_pos))
    
    def handle_events(self):
        """Handle pygame events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
    
    def update(self):
        """Update game state"""
        # Don't update if game is won
        if self.game_won:
            self.update_speech_bubbles()
            self.update_bash_flashes()
            return
            
        current_time = time.time()
        
        # Spawn coins every second
        if current_time - self.last_coin_spawn >= 1.0:
            self.spawn_coin()
            self.last_coin_spawn = current_time
        
        # Move robots every 0.5 seconds
        if current_time - self.last_robot_move >= 0.5:
            self.move_robots()
            self.last_robot_move = current_time
        
        # Robots bash every 5 seconds
        if current_time - self.last_bash_time >= 5.0:
            self.robot_bash()
            self.last_bash_time = current_time
        
        # Clear bashing robots after each movement cycle (they can move again next cycle)
        # This happens after bash but before next movement
        current_move_time = current_time - self.last_robot_move
        if current_move_time >= 0.25:  # Clear halfway through movement cycle
            self.robots_bashing.clear()
        
        # Robots no longer speak automatically - only when they get coins
        
        # Update speech bubbles and bash flashes
        self.update_speech_bubbles()
        self.update_bash_flashes()
    
    def draw(self):
        """Draw everything"""
        self.draw_world()
        self.draw_speech_bubbles()
        self.draw_leaderboard()
        pygame.display.flip()
    
    def run(self):
        """Main game loop"""
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)  # 60 FPS
        
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.run()
