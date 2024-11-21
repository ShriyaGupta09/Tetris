import pygame


class Grid:
    def __init__(self):
        self.num_rows = 20
        self.num_cols = 10
        self.cell_size = 35

        # Initialize the grid with all cells set to 0
        self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)]

        # Get the list of colors for the cells
        self.colors = self.get_cell_colors()

    def print_grid(self):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                print(self.grid[row][column], end=" ")
            print()

    def is_inside(self, row, column):
        if 0 <= row <= self.num_rows and 0 <= column <= self.num_cols:
            return True
        return False

    def is_empty(self, row, column):
        if self.grid[row][column] == 0:
            return True
        return False

    def is_row_full(self, row):
        for column in range(self.num_cols):
            if self.grid[row][column] == 0:
                return False
        return True

    def clear_row(self, row):
        for column in range(self.num_cols):
            self.grid[row][column] = 0

    def move_row_down(self, row, num_rows):
        for column in range(self.num_cols):
            self.grid[row + num_rows][column] = self.grid[row][column]
            self.grid[row][column] = 0

    def clear_full_rows(self):
        completed = 0
        for row in range(self.num_rows - 1, -1, -1):  # Iterate from bottom to top
            if self.is_row_full(row):
                self.clear_row(row)
                completed += 1
            elif completed > 0:
                self.move_row_down(row, completed)
        return completed

    def reset(self):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                self.grid[row][column] = 0

    def draw(self, screen):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                cell_value = self.grid[row][column]
                cell_rect = pygame.Rect(column * self.cell_size + 10, row * self.cell_size + 10,
                                        self.cell_size - 1, self.cell_size - 1)
                # Draw the cell with the corresponding color
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect)

    def get_cell_colors(self):
        dark_grey = (26, 31, 40)
        red = (255, 0, 0)
        orange = (255, 165, 0)
        green = (0, 255, 0)
        yellow = (255, 255, 0)
        purple = (128, 0, 128)
        magenta = (255, 0, 255)
        blue = (0, 0, 255)
        cyan = (0, 255, 255)

        return [dark_grey, red, orange, blue, green, yellow, purple, cyan, magenta]
