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

def circular(x, y):
    return x**2 + y **2

def hiperbolica(x, y):
    return x**2 - y **2

def triangular(x, y):
    return x * y

def teste(x, y):
    return x**2 * y

def Paraboloide(nx, ny, x_i, x_f, y_i, y_f, fn):
    dx = (x_f - x_i)/nx
    dy = (y_f - y_i)/ny
    glBegin(GL_POINTS)
    for i in range(nx):
        for j in range(ny):
            x = x_i + (i * dx)
            y = y_i + (j * dy)
            z = fn(x, y)
            glVertex3f(x, y, z)
    glEnd()


def ParaboloideMalhaCircular(ns, nt, rf, fn):
    d_teta = (2 * math.pi)/ns
    d_r = rf/nt
    glBegin(GL_POINTS)
    for i in range(ns):
        for j in range(nt):
            raio = (j * rf)/nt
            teta = i * d_teta
            x = raio * math.cos(teta)
            y = raio * math.sin(teta)
            z = fn(x, y)
            glVertex3f(x, y, z)
    glEnd()

def ParaboloideMalhaCircularPreenchida(ns, nt, rf, fn):
    d_teta = (2 * math.pi)/ns
    d_r = rf/nt
    for i in range(ns):
        glBegin(GL_TRIANGLE_STRIP)
        for j in range(nt):
            raio = (j * rf)/nt
            teta = i * d_teta
            phi = (i + 1) * d_teta 
            x = raio * math.cos(teta)
            y = raio * math.sin(teta)
            z = fn(x, y)
            x1 = raio * math.cos(phi)
            y1 = raio * math.sin(phi)
            z1 = fn(x1, y1)
            # glColor3f(i/ns, j/nt, (i+j)/(ns+nt))
            glColor4f(0.4588235294117647, 0.5843137254901961, 0.9372549019607843, 0.3)
            glVertex3f(x, y, z)
            glVertex3f(x1, y1, z1)
        glEnd()

ar = 0


def desenha():
    global ar
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    glRotatef(ar, 1, 1, 0)
    # Paraboloide(40, 40, -2, 2, -2, 2, teste)
    # ParaboloideMalhaCircular(40, 40, 3, teste)
    ParaboloideMalhaCircularPreenchida(40, 40, 0.8, circular)
    glPopMatrix()
    ar += 0.5


WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

sdl2.SDL_Init(sdl2.SDL_INIT_EVERYTHING)
sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_CONTEXT_MAJOR_VERSION, 2)
sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_CONTEXT_MINOR_VERSION, 1)
sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_CONTEXT_PROFILE_MASK, sdl2.SDL_GL_CONTEXT_PROFILE_CORE)
sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_DOUBLEBUFFER, 1)
sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_DEPTH_SIZE, 24)
sdl2.SDL_GL_SetSwapInterval(1)
window = sdl2.SDL_CreateWindow(b"Computacao Grafica", sdl2.SDL_WINDOWPOS_CENTERED, sdl2.SDL_WINDOWPOS_CENTERED, WINDOW_WIDTH,
                               WINDOW_HEIGHT, sdl2.SDL_WINDOW_OPENGL | sdl2.SDL_WINDOW_SHOWN)
if not window:
    sys.stderr.write("Error: Could not create window\n")
    exit(1)
glcontext = sdl2.SDL_GL_CreateContext(window)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glEnable(GL_BLEND)
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
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
