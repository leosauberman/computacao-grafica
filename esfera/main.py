import math
import sys

import sdl2
from OpenGL.GL import *
from OpenGL.GLU import *


def EsferaPontos(n, r):
    glBegin(GL_POINTS)
    for i in range(n):
        teta = ((math.pi * i)/n) - (math.pi/2)
        for j in range(n):
            phi = (2 * math.pi * j)/n
            x = r * math.cos(teta) * math.cos(phi)
            y = r * math.sin(teta)
            z = r * math.cos(teta) * math.sin(phi)
            glVertex3f(x, y, z)
    glEnd()

def calcVertices(i, j, r, n):
    teta = ((math.pi * i) / n) - (math.pi / 2)
    phi = (2 * math.pi * j) / n
    x = r * math.cos(teta) * math.cos(phi)
    y = r * math.sin(teta)
    z = r * math.cos(teta) * math.sin(phi)

    return x, y, z, teta, phi

def Esfera(n, r):
    for i in range(n):
        glBegin(GL_TRIANGLE_STRIP)
        for j in range(n + 1):
            x, y, z, teta, phi = calcVertices(i, j, r, n)
            x1, y1, z1, teta1, phi1 = calcVertices(i+1, j, r, n)
            glColor3f(i/n, j/n, (i+j)/(2 * n))
            glVertex3f(x, y, z)
            glVertex3f(x1, y1, z1)
        glEnd()

ar = 0


def desenha():
    global ar
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    glRotatef(ar, 1, 1, 1)
    # EsferaPontos(45, 1)
    Esfera(45, 1)
    glPopMatrix()
    ar += 1


WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

sdl2.SDL_Init(sdl2.SDL_INIT_EVERYTHING)
sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_CONTEXT_MAJOR_VERSION, 2)
sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_CONTEXT_MINOR_VERSION, 1)
sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_CONTEXT_PROFILE_MASK, sdl2.SDL_GL_CONTEXT_PROFILE_CORE)
sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_DOUBLEBUFFER, 1)
sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_DEPTH_SIZE, 24)
sdl2.SDL_GL_SetSwapInterval(1)
window = sdl2.SDL_CreateWindow(b"Cubo", sdl2.SDL_WINDOWPOS_CENTERED, sdl2.SDL_WINDOWPOS_CENTERED, WINDOW_WIDTH,
                               WINDOW_HEIGHT, sdl2.SDL_WINDOW_OPENGL | sdl2.SDL_WINDOW_SHOWN)
if not window:
    sys.stderr.write("Error: Could not create window\n")
    exit(1)
glcontext = sdl2.SDL_GL_CreateContext(window)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0., 0., 0., 1.)
gluPerspective(45, 800.0 / 600.0, 0.1, 100.0)
glTranslatef(0.0, 0.0, -10)

running = True
event = sdl2.SDL_Event()
while running:
    while sdl2.SDL_PollEvent(ctypes.byref(event)) != 0:
        if event.type == sdl2.SDL_QUIT:
            running = False
        if event.type == sdl2.events.SDL_KEYDOWN:
            print("SDL_KEYDOWN")
            if event.key.keysym.sym == sdl2.SDLK_ESCAPE:
                running = False
    desenha()
    sdl2.SDL_GL_SwapWindow(window)
