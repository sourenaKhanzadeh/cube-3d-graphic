import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *


vertices = (
    (1,  -1 , -1),
    (1,   1 , -1),
    (-1,  1 , -1),
    (-1, -1 , -1),
    (1,  -1 ,  1),
    (1,   1 ,  1),
    (-1, -1 ,  1),
    (-1,  1 ,  1)
)

edges = (
    (0, 1),
    (0, 3),
    (0, 4),
    (2, 1),
    (2, 3),
    (2, 7),
    (6, 3),
    (6, 4),
    (6, 7),
    (5, 1),
    (5, 4),
    (5, 7)
)

surfaces = (
    (0,1,2,3),
    (3,2,7,6),
    (6,7,5,4),
    (4,5,1,0),
    (1,5,7,2),
    (4,0,3,6)
)

s_color = (
    (0,0,1),
    (0,1,0),
    (1,0,0),
    (0,1,1),
    (1,0,1),
    (1,1,0)
)

def cube():
    glBegin(GL_QUADS)
    x = 0
    for surf in surfaces:
        for vertex in surf:
            glColor3fv(s_color[x])
            glVertex3fv(vertices[vertex])
        x += 1

    glEnd()

    glBegin(GL_LINES)
    glColor3fv((0,0,0))
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])

    glEnd()



def controls():
    keys = pygame.key.get_pressed()
    axis = True
    speed = 10
    if keys[pygame.K_LEFT]:
        glRotatef(speed, 0, axis, 0)
    if keys[pygame.K_RIGHT]:
        glRotatef(speed, 0, -axis, 0)
    if keys[pygame.K_UP]:
        glRotatef(speed, axis, 0, 0)
    if keys[pygame.K_DOWN]:
        glRotatef(speed, -axis, 0, 0)



def main():
    pygame.init()
    screen_w = 800
    screen_h = 600
    display = (screen_w, screen_h)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    pygame.display.set_caption("Cube Revolver")

    gluPerspective(45, screen_w/screen_h, 0.1, 50.0)

    glTranslatef(0.0, 0.0, -5)


    run = True

    while run:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        cube()

        controls()

        pygame.display.flip()


    pygame.quit()
    quit()

main()