import pygame
import random

Margin = 1
Width, Height = 1000, 600
Rows, Cols = 10 , 10
CELL_SIZE = Width // Cols
obstacles = 25
numbers = 10
# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

pygame.init()

sc = pygame.display.set_mode((Width , Height))
pygame.display.set_caption("Group MazeMaker")

font = pygame.font.SysFont("Arial" , 20)

clock = pygame.time.Clock()

def generate_maze(rows, cols, obstacles, numbers):
    maze = [[' ' for _ in range(cols)] for _ in range(rows)]

    maze[0][0] = "Start"
    maze[rows - 1][cols - 1] = "End"

    #Obstacles
    placed_obstacles = 0
    while placed_obstacles < obstacles:
        r, c = random.randint(0, rows-1), random.randint(0, cols-1) #random number for column =c , and same thing for r
        if maze[r][c] == ' ':
            maze[r][c] = 'XcloseX'
            placed_obstacles = placed_obstacles + 1


    #Numbers
    placed_numbers = 0
    while placed_numbers < numbers:
        r, c = random.randint(0, rows-1), random.randint(0, cols-1)
        if maze[r][c] == ' ':
            maze[r][c] = random.randint(-9, 9)
            placed_numbers = placed_numbers + 1

    return maze
 

def draw_maze(screen, maze):

    for row in range(len(maze)):
        for col in range(len(maze[row])):
            x = col * CELL_SIZE
            y = row * CELL_SIZE
            if maze[row][col] == 'Start':
                pygame.draw.rect(screen, GREEN, (x, y, CELL_SIZE, CELL_SIZE))
            elif maze[row][col] == 'End':
                pygame.draw.rect(screen, RED, (x, y, CELL_SIZE, CELL_SIZE))
            elif maze[row][col] == 'XcloseX':
                pygame.draw.rect(screen, BLACK, (x, y, CELL_SIZE, CELL_SIZE))
            elif isinstance(maze[row][col], int):
                pygame.draw.rect(screen, YELLOW, (x, y, CELL_SIZE, CELL_SIZE))
                text = font.render(str(maze[row][col]), True, BLUE)
                screen.blit(text, (x + CELL_SIZE // 4, y + CELL_SIZE // 4))
            else:
                pygame.draw.rect(screen, WHITE, (x, y, CELL_SIZE, CELL_SIZE))
            # Draw grid lines
            pygame.draw.rect(screen, BLACK, (x, y, CELL_SIZE, CELL_SIZE), 1)

# Generate the maze
maze = generate_maze(Rows, Cols, obstacles, numbers)

gameOn = True
while gameOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOn = False

    sc.fill(WHITE)
    draw_maze(sc, maze)
    pygame.display.flip()

    
pygame.quit()

