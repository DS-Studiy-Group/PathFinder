import pygame

Tile = 50
margin = 1
Rows , Cols = 10 , 10
width , height = 700 , Cols * Tile

#colors
WHITE = pygame.Color("white")
BLACK = pygame.Color("black")
GRAY = pygame.Color("gray")

pygame.init()
sc = pygame.display.set_mode((width, height))
pygame.display.set_caption("AD Maze Generator")

class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.is_wall = False
        self.visited = False
    def draw(self):
        x = self.x * Tile
        y = self.y * Tile
        pygame.draw.rect(sc, WHITE, (x, y, Tile, Tile))
        pygame.draw.rect(sc, GRAY, (x, y, Tile, Tile) , 2)

grid = [[Cell(x, y) for x in range(Cols)] for y in range(Rows)]

gameOn = True
while gameOn:
        sc.fill(GRAY)
        for row in grid:
            for cell in row:
                cell.draw()
    
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOn = False
        
pygame.quit()
