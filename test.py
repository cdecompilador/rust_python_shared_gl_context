import testing
from OpenGL.GL import *
import sys, sdl2, ctypes

if sdl2.SDL_Init(sdl2.SDL_INIT_VIDEO) != 0:
    print(sdl2.SDL_GetError())
    sys.error()

window = sdl2.SDL_CreateWindow(b"OpenGL demo",
                               sdl2.SDL_WINDOWPOS_UNDEFINED,
                               sdl2.SDL_WINDOWPOS_UNDEFINED, 
                               500, 500,
                               sdl2.SDL_WINDOW_OPENGL)
if not window:
    print(sdl2.SDL_GetError())
    sys.exit()

context = sdl2.SDL_GL_CreateContext(window)
get_proc_addr = sdl2.SDL_GL_GetProcAddress
testing.clear(get_proc_addr)

event = sdl2.SDL_Event()
running = True
while running:
    while sdl2.SDL_PollEvent(ctypes.byref(event)) != 0:
        if event.type == sdl2.SDL_QUIT:
            running = False

    testing.clear(get_proc_addr)
    sdl2.SDL_GL_SwapWindow(window)
