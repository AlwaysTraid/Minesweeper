import pygame
import random
from pprint import PrettyPrinter

printer = PrettyPrinter()
WIDTH, HEIGHT = 700, 800

#Tutorial From https://www.youtube.com/watch?v=RRYgc4YIhEs
#Left off at 15:20


win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("MineSweeper")

BG_COLOR = "white"
ROWS, COLS = 15, 15
MINES = 15

def get_neighbors(row, col, rows, cols):
    neighbors = []
    if row > 0: # UP
        neighbors.append((row - 1, col))
    if row < rows - 1: # DOWN
        neighbors.append((row + 1, col))
    if col > 0: # LEFT
        neighbors.append((row, col - 1))
    if col < cols - 1: # RIGHT
        neighbors.append((row, col + 1))

    if row > 0 and col > 0:
        neighbors.append((row - 1, col - 1))
    if row < rows - 1 and col < cols - 1:
        neighbors.append((row + 1, col + 1))
    if row < rows - 1 and col > 0:
        neighbors.append((row + 1, col -1))
    if row > 0 and col < cols - 1:
        neighbors.append((row - 1, col + 1))

    return neighbors

def create_mine_field(rows, cols, mines):
    field = [[0 for _ in range(cols)] for _ in range(rows)]
    mine_positions = set()

    mines_created = 0
    while len(mine_positions) < mines:
        row = random.randrange(0, rows)
        col = random.randrange(0, cols)
        pos = row, col

        if pos in mine_positions:
            continue

        mine_positions.add(pos)
        field[row][col] = -1

    for mine in mine_positions:
        neighbors = get_neighbors(*mine, rows, cols)
        for r, c in neighbors:
            field[r][c] += 1 

    return field

    

def draw(win):
    win.fill(BG_COLOR)
    pygame.display.update()

def main():
    run = True

    field = create_mine_field(ROWS, COLS, MINES)

    printer.pprint(field)

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        draw(win)
    pygame.quit()

if __name__ == "__main__":
    main()