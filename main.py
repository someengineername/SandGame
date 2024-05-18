import pygame
import time

pygame.init()


# temp function of tick (time-control)
def tick():
    time.sleep(0.5)
    pygame.display.update()


# matrix edge dimensions preparations
matrix_dimension = 10
cell_length = 40
gap_bw_cells = cell_length // 7

# screen initialization
#   with update to cell size
screen_width = cell_length * matrix_dimension + gap_bw_cells * (matrix_dimension + 1)
screen_height = cell_length * matrix_dimension + gap_bw_cells * (matrix_dimension + 1)
screen = pygame.display.set_mode((screen_width, screen_height))

# test of text

# colors initialization

COLOR_RGB_BLACK = (0, 0, 0)
COLOR_RGB_WHITE = (255, 255, 255)
COLOR_RGB_RED = (255, 0, 0)
COLOR_RGB_GREEN = (0, 255, 0)
COLOR_RGB_BLUE = (0, 0, 255)

# matrix initialization - to store values
matrix = [[0 for j in range(matrix_dimension)] for i in range(matrix_dimension)]

# mask-matrix to check mouse interaction
mask_matrix_base_coordinates_of_rectangles_wo_gaps = [[j for j in range(matrix_dimension)] for q in
                                                      range(matrix_dimension)]

for i in range(matrix_dimension):
    for j in range(matrix_dimension):
        mask_matrix_base_coordinates_of_rectangles_wo_gaps[i][j] = [gap_bw_cells + i * (cell_length + gap_bw_cells),
                                                                    gap_bw_cells + j * (cell_length + gap_bw_cells)]

for i in range(matrix_dimension):
    for j in range(matrix_dimension):
        print(mask_matrix_base_coordinates_of_rectangles_wo_gaps[i][j], end='')
    print()

    # matrix for drawing the display, based on values matrix cols|rows
drawing_coordinates_matrix = [[j for j in i] for i in matrix]

# fill drawing matrix with rectangles + gaps b\w them
for i in range(matrix_dimension):
    for j in range(matrix_dimension):
        drawing_coordinates_matrix[i][j] = pygame.Rect((i * (cell_length + gap_bw_cells) + gap_bw_cells,
                                                        j * (cell_length + gap_bw_cells) + gap_bw_cells,
                                                        cell_length, cell_length))

# main loop
run = True

while run:

    mouse_coord = []

    screen.fill(COLOR_RGB_BLACK)

    for line in drawing_coordinates_matrix:
        for pos in line:
            pygame.draw.rect(screen, COLOR_RGB_WHITE, pos)

    # event handler
    for event in pygame.event.get():

        # different variations of events goes here...
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONUP:
            mouse_coord = pygame.mouse.get_pos()

    if mouse_coord:
        pygame.draw.rect(screen, COLOR_RGB_RED, (mouse_coord[0], mouse_coord[1], 50, 50))
    else:
        pass

    # pygame.display.update()
    tick()

pygame.quit()
