import pygame

pygame.init()

# screen initialization
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# drawings initialization
Rec1 = pygame.Rect((100, 100, 50, 50))

RGB_WHITE = (255, 255, 255)
RGB_RED = (255, 0, 0)

# matrix initialization - to store values
matrix_edge_range = 5
matrix = [[0 for j in range(matrix_edge_range)] for i in range(matrix_edge_range)]

for i in matrix:
    for j in i:
        print(j, end=' ')
    print()

# matrix for drawing the display, based on values matrix cols|rows
drawing_coordinates_matrix = [[(0, 0) for j in i] for i in matrix]
# print(len(drawing_coordinates_matrix))

for i in range(len(drawing_coordinates_matrix)):
    for j in range(len(drawing_coordinates_matrix[j])):
        print(j, end='')
    print()

# main loop
run = True

while run:

    screen.fill(RGB_WHITE)

    # event handler
    for event in pygame.event.get():

        # different variations of events goes here...
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
