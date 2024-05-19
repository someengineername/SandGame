import pygame
import time
import random

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
        return COLOR_RGB_WHITE
    else:
        return COLOR_RGB_BLACK


# matrix edge dimensions preparations
matrix_dimension = 100
cell_length = 5
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
    pressed_mouse = False

    # -------------
    # event handler
    # -------------
    for event in pygame.event.get():

        # different variations of events goes here...
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            pressed_mouse = True

        if event.type == pygame.MOUSEBUTTONUP:
            pressed_mouse = False

    temp_coordinates = pygame.mouse.get_pos()
    coordinates_of_click = [temp_coordinates[0] // (cell_length + gap_bw_cells),
                            temp_coordinates[1] // (cell_length + gap_bw_cells)]

    if (0 < coordinates_of_click[0] < matrix_dimension - 1) and (0 < coordinates_of_click[1] < matrix_dimension - 1):
        if (matrix[coordinates_of_click[0] + 1][coordinates_of_click[1] + 1] is False and
                matrix[coordinates_of_click[0] - 1][coordinates_of_click[1] + 1] is False and
                matrix[coordinates_of_click[0]][coordinates_of_click[1] + 1] is False):
            matrix[coordinates_of_click[0]][coordinates_of_click[1]] = True

    # -------------
    # matrix-for-drawing preparation
    # -------------
    temp_matrix = [[False for j in range(matrix_dimension)] for i in range(matrix_dimension)]

    # matrix re-filament section ( check value in matrix and copy it
    for i in range(matrix_dimension - 1, -1, -1):
        for j in range(matrix_dimension - 1, -1, -1):
            if matrix[i][j] is True:
                # bottom-side condition
                if j == matrix_dimension - 1:
                    temp_matrix[i][j] = True
                # left-hand side condition
                elif i == 0:
                    # if bottom is empty
                    if matrix[i][j + 1] is False:
                        temp_matrix[i][j] = False
                        temp_matrix[i][j + 1] = True
                    # if bottom is occupied
                    else:
                        # if only bottom
                        if matrix[i + 1][j + 1] is False:
                            temp_matrix[i][j] = False
                            temp_matrix[i + 1][j + 1] = True
                        # right-side as well, do nothing
                        elif matrix[i + 1][j + 1] is True:
                            temp_matrix[i][j] = True
                # right-hand side condition
                elif i == matrix_dimension - 1:
                    # if bottom is empty
                    if matrix[i][j + 1] is False:
                        temp_matrix[i][j] = False
                        temp_matrix[i][j + 1] = True
                    # if bottom is occupied
                    else:
                        # if only bottom
                        if matrix[i - 1][j + 1] is False:
                            temp_matrix[i][j] = False
                            temp_matrix[i - 1][j + 1] = True
                        # left-side as well, do nothing
                        elif matrix[i - 1][j + 1] is True:
                            temp_matrix[i][j] = True
                # general behaviour condition
                else:
                    # if bottom is empty
                    if matrix[i][j + 1] is False:
                        temp_matrix[i][j] = False
                        temp_matrix[i][j + 1] = True
                    # if bottom is occupied
                    else:
                        # if right side occupied
                        if matrix[i - 1][j + 1] is False and matrix[i + 1][j + 1] is True:
                            temp_matrix[i - 1][j + 1] = True
                        # if left side occupied
                        elif matrix[i + 1][j + 1] is False and matrix[i - 1][j + 1] is True:
                            temp_matrix[i + 1][j + 1] = True
                        # if both sides occupied - 50|50 %
                        elif matrix[i + 1][j + 1] is False and matrix[i - 1][j + 1] is False:
                            if random.randint(0, 1) == 1:
                                temp_matrix[i - 1][j + 1] = True
                            else:
                                temp_matrix[i + 1][j + 1] = True
                        # if everything's occupied
                        elif matrix[i + 1][j + 1] is True and matrix[i - 1][j + 1] is True and matrix[i][j + 1] is True:
                            temp_matrix[i][j] = True

    # -------------
    # screen drawing section
    # -------------

    # drawing black canvas
    screen.fill(COLOR_RGB_WHITE)

    # drawing rectangles according to validity (TRUE | FALSE)
    for i in range(matrix_dimension):
        for j in range(matrix_dimension):
            pygame.draw.rect(screen, return_color_for_cell(temp_matrix, i, j),
                             (i * (cell_length + gap_bw_cells) + gap_bw_cells,
                              j * (cell_length + gap_bw_cells) + gap_bw_cells,
                              cell_length, cell_length))

    # -------------
    # frame-generation-like
    # -------------
    tick(0.0001)

    matrix = temp_matrix

pygame.quit()
