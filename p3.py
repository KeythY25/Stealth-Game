import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
PLAYER_SIZE = 20
GUARD_SIZE = 30
GOAL_SIZE = 30
VISION_RANGE = 100
OBSTACLE_COUNT = 5

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
GRAY = (100, 100, 100)

# Setup screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("AI Stealth Game")

# Player class
class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, PLAYER_SIZE, PLAYER_SIZE)
        self.speed = 3
    
    def move(self, keys):
        if keys[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.x < WIDTH - PLAYER_SIZE:
            self.rect.x += self.speed
        if keys[pygame.K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.y < HEIGHT - PLAYER_SIZE:
            self.rect.y += self.speed
    
    def draw(self):
        pygame.draw.rect(screen, BLUE, self.rect)

# Guard class
class Guard:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, GUARD_SIZE, GUARD_SIZE)
        self.speed = 2
        self.direction = random.choice(["horizontal", "vertical"])
        self.patrol_distance = 100
        self.start_x = x
        self.start_y = y
        self.moving_forward = True
    
    def patrol(self):
        if self.direction == "horizontal":
            if self.moving_forward:
                self.rect.x += self.speed
                if self.rect.x >= self.start_x + self.patrol_distance:
                    self.moving_forward = False
            else:
                self.rect.x -= self.speed
                if self.rect.x <= self.start_x:
                    self.moving_forward = True
        else:
            if self.moving_forward:
                self.rect.y += self.speed
                if self.rect.y >= self.start_y + self.patrol_distance:
                    self.moving_forward = False
            else:
                self.rect.y -= self.speed
                if self.rect.y <= self.start_y:
                    self.moving_forward = True
    
    def detect_player(self, player):
        distance = ((self.rect.centerx - player.rect.centerx) ** 2 + (self.rect.centery - player.rect.centery) ** 2) ** 0.5
        return distance < VISION_RANGE
    
    def draw(self):
        pygame.draw.rect(screen, RED, self.rect)
        pygame.draw.circle(screen, (255, 200, 200), self.rect.center, VISION_RANGE, 1)

# Generate obstacles
obstacles = [pygame.Rect(random.randint(50, WIDTH - 100), random.randint(50, HEIGHT - 100), 50, 50) for _ in range(OBSTACLE_COUNT)]

# Initialize player, guards, and goal
player = Player(50, HEIGHT - 50)
guards = [Guard(300, 300), Guard(500, 200)]
goal = pygame.Rect(WIDTH - 50, 50, GOAL_SIZE, GOAL_SIZE)

# Game loop
running = True
while running:
    pygame.time.delay(30)
    screen.fill(WHITE)
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Player movement
    keys = pygame.key.get_pressed()
    player.move(keys)
    
    # Guards' patrol and detection
    for guard in guards:
        guard.patrol()
        if guard.detect_player(player):
            print("Caught! Resetting game...")
            player.rect.x, player.rect.y = 50, HEIGHT - 50  # Reset player position
    
    # Draw elements
    pygame.draw.rect(screen, GREEN, goal)
    player.draw()
    for guard in guards:
        guard.draw()
    for obs in obstacles:
        pygame.draw.rect(screen, GRAY, obs)
    
    # Check if player reaches goal
    if player.rect.colliderect(goal):
        print("You win!")
        running = False
    
    pygame.display.update()

pygame.quit()
