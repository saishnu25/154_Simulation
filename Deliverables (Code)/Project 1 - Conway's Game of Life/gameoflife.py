import pygame
import numpy as np

# Define constants
WIDTH, LENGTH = 700, 700
BLOCK_SIZE = 10
ROWS, COLS = LENGTH // BLOCK_SIZE, WIDTH // BLOCK_SIZE

# Initialize Pygame
pygame.init()

# Create the display
screen = pygame.display.set_mode((WIDTH, LENGTH))
pygame.display.set_caption("Conway's Game of Life")

# Function to create the initial state of the grid
def create_grid():
    grid = np.random.choice([0, 1], (ROWS, COLS), p=[0.7, 0.3])
    return grid

# Function to update the state of the grid
def update_grid(grid):
    new_grid = np.zeros((ROWS, COLS))
    for i in range(ROWS):
        for j in range(COLS):
            neighbors = (
                grid[i-1:i+2, j-1:j+2].sum() - grid[i, j]
            )
            if grid[i, j] == 0 and neighbors == 3:
                new_grid[i, j] = 1
            elif grid[i, j] == 1 and (neighbors < 2 or neighbors > 3):
                new_grid[i, j] = 0
            else:
                new_grid[i, j] = grid[i, j]
    return new_grid

# Function to draw the grid
def draw_grid(grid):
    for i in range(ROWS):
        for j in range(COLS):
            color = (200, 200, 200) if grid[i, j] == 0 else (0, 0, 0)
            pygame.draw.rect(screen, color, (j*BLOCK_SIZE, i*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

# Main function
def main():
    # Create the initial grid
    grid = create_grid()

    # Main loop
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update the grid
        grid = update_grid(grid)

        # Draw the grid
        draw_grid(grid)

        # Update the display
        pygame.display.flip()

    # Quit Pygame
    pygame.quit()

if __name__ == '__main__':
    main()