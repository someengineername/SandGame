import pygame
import time

# colors initialization
COLOR_RGB_BLACK = (0, 0, 0)
COLOR_RGB_WHITE = (255, 255, 255)
COLOR_RGB_RED = (255, 0, 0)
COLOR_RGB_GREEN = (0, 255, 0)
COLOR_RGB_BLUE = (0, 0, 255)

pygame.init()


# temp function of tick (time-control)
def tick(timing: int | float):
    time.sleep(timing)
    pygame.display.update()


def return_color_for_cell(matrix, coor_x, coor_y):
    if matrix[coor_x][coor_y]:
        return COLOR_RGB_BLACK
    else:
        return COLOR_RGB_WHITE


def reverse_flag(matrix, coor_x, coor_y):
    if matrix[coor_x][coor_y] is True:
        matrix[coor_x][coor_y] = False
    else:
        matrix[coor_x][coor_y] = True


# matrix edge dimensions preparations
matrix_dimension = 50
cell_length = 10
gap_bw_cells = cell_length // 10

# screen initialization with update to cell size
screen_width = cell_length * matrix_dimension + gap_bw_cells * (matrix_dimension + 1)
screen_height = cell_length * matrix_dimension + gap_bw_cells * (matrix_dimension + 1)
screen = pygame.display.set_mode((screen_width, screen_height))

# matrix initialization - to store values
matrix = [[False for j in range(matrix_dimension)] for i in range(matrix_dimension)]

# main loop
run = True

while run:

    mouse_coord = []

    # event handler
    for event in pygame.event.get():

        # different variations of events goes here...
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONUP:
            mouse_coord = pygame.mouse.get_pos()

    # screen drawing section
    screen.fill(COLOR_RGB_BLACK)

    if mouse_coord:
        coordinates_of_click = [mouse_coord[0] // (cell_length + gap_bw_cells),
                                mouse_coord[1] // (cell_length + gap_bw_cells)]
        reverse_flag(matrix, coordinates_of_click[0], coordinates_of_click[1])

    for i in range(matrix_dimension):
        for j in range(matrix_dimension):
            pygame.draw.rect(screen, return_color_for_cell(matrix, i, j),
                             (i * (cell_length + gap_bw_cells) + gap_bw_cells,
                              j * (cell_length + gap_bw_cells) + gap_bw_cells,
                              cell_length, cell_length))

    tick(0.001)

pygame.quit()
