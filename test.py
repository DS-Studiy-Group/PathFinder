import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 600
ROWS, COLS = 10, 10
CELL_SIZE = WIDTH // COLS

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Generator")

# Font setup
font = pygame.font.SysFont("Arial", 24)

def generate_maze(rows, cols, obstacles, numbers):
    """
    Generates a maze grid with specified rows, cols, obstacles, and numbers.
    """
    maze = [[' ' for _ in range(cols)] for _ in range(rows)]

    # Place start and end points
    maze[0][0] = 'S'
    maze[rows-1][cols-1] = 'E'

    # Randomly place obstacles
    placed_obstacles = 0
    while placed_obstacles < obstacles:
        r, c = random.randint(0, rows-1), random.randint(0, cols-1)
        if maze[r][c] == ' ':
            maze[r][c] = 'X'
            placed_obstacles += 1

    # Randomly place numbers
    placed_numbers = 0
    while placed_numbers < numbers:
        r, c = random.randint(0, rows-1), random.randint(0, cols-1)
        if maze[r][c] == ' ':
            maze[r][c] = random.randint(-10, 10)
            placed_numbers += 1

    return maze

def draw_maze(screen, maze):
    """
    Draws the maze on the screen.
    """
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            x, y = col * CELL_SIZE, row * CELL_SIZE
            # Draw cells
            if maze[row][col] == 'S':
                pygame.draw.rect(screen, GREEN, (x, y, CELL_SIZE, CELL_SIZE))
            elif maze[row][col] == 'E':
                pygame.draw.rect(screen, RED, (x, y, CELL_SIZE, CELL_SIZE))
            elif maze[row][col] == 'X':
                pygame.draw.rect(screen, BLACK, (x, y, CELL_SIZE, CELL_SIZE))
            elif isinstance(maze[row][col], int):
                pygame.draw.rect(screen, YELLOW, (x, y, CELL_SIZE, CELL_SIZE))
                text = font.render(str(maze[row][col]), True, BLUE)
                screen.blit(text, (x + CELL_SIZE // 4, y + CELL_SIZE // 4))
            else:
                pygame.draw.rect(screen, WHITE, (x, y, CELL_SIZE, CELL_SIZE))
            # Draw grid lines
            pygame.draw.rect(screen, BLACK, (x, y, CELL_SIZE, CELL_SIZE), 1)

# Parameters for the maze
rows, cols = ROWS, COLS
obstacles = 20
numbers = 15

# Generate the maze
maze = generate_maze(rows, cols, obstacles, numbers)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill screen with white
    screen.fill(WHITE)

    # Draw the maze
    draw_maze(screen, maze)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
