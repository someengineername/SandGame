import pygame

pygame.init()

# matrix drawings preparations

matrix_edge_range = 20

cell_edge_dimension = 20
gap_bw_cells = cell_edge_dimension // 5

# screen initialization
screen_width = cell_edge_dimension * matrix_edge_range + gap_bw_cells * (matrix_edge_range + 1)
screen_height = cell_edge_dimension * matrix_edge_range + gap_bw_cells * (matrix_edge_range + 1)
screen = pygame.display.set_mode((screen_width, screen_height))

# drawings|colors initialization
# Rec1 = pygame.Rect((100, 0, 50, 50))

COLOR_RGB_BLACK = (0, 0, 0)
COLOR_RGB_WHITE = (255, 255, 255)
COLOR_RGB_RED = (255, 0, 0)
COLOR_RGB_GREEN = (0, 255, 0)
COLOR_RGB_BLUE = (0, 0, 255)

# matrix initialization - to store values

matrix = [[0 for j in range(matrix_edge_range)] for i in range(matrix_edge_range)]

for i in matrix:
    for j in i:
        print(j, end=' ')
    print()

# matrix for drawing the display, based on values matrix cols|rows
drawing_coordinates_matrix = [[j for j in i] for i in matrix]

# fill drawing coordinates (start of Rec's)
for i in range(matrix_edge_range):
    for j in range(matrix_edge_range):
        drawing_coordinates_matrix[i][j] = pygame.Rect((i * (cell_edge_dimension + gap_bw_cells) + gap_bw_cells,
                                                        j * (cell_edge_dimension + gap_bw_cells) + gap_bw_cells,
                                                        cell_edge_dimension, cell_edge_dimension))
    # print()

# main loop
run = True

while run:

    screen.fill(COLOR_RGB_BLACK)

    for line in drawing_coordinates_matrix:
        for pos in line:
            pygame.draw.rect(screen, COLOR_RGB_WHITE, pos)

    # event handler
    for event in pygame.event.get():

        # different variations of events goes here...
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
