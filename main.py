"""
The main module
"""
import os

import pygame

from pygame.locals import QUIT, MOUSEMOTION, MOUSEBUTTONUP, MOUSEBUTTONDOWN

from models import Graph, Node, Connection
from views import ToolBar, PathMenu
import mapPoints

RUNNING = True

READONLY = True

bg = pygame.image.load("bg.png")


def quit_callback():
    """
    This method marks the exit of the program.
    """
    global RUNNING
    RUNNING = False


def main():
    """
    This is the main method of the program
    """
    global RUNNING

    # sets the window position
    os.environ['SDL_VIDEO_WINDOW_POS'] = f"{300},{100}"

    # initialize pygame
    pygame.init()
    pygame.font.init()

    graph = Graph(mapPoints.nodesPlaces +
                  mapPoints.nodePaths,
                  mapPoints.connections)

    # initialize tkinter
    pathMenu = PathMenu(graph)
    toolbar = None
    if not READONLY:
        toolbar = ToolBar(graph)
        toolbar.protocol("WM_DELETE_WINDOW", quit_callback)

    pathMenu.protocol("WM_DELETE_WINDOW", quit_callback)

    # start pygame clock
    clock = pygame.time.Clock()

    # initialize variables
    font = pygame.font.SysFont("Consolas", 15)
    framerate = 30
    double_click_duration = 150  # ms
    last_click = 0

    # sets the window size
    pygame.display.set_caption("这是地图")
    screen = pygame.display.set_mode((1241, 838))

    while RUNNING:
        for event in pygame.event.get():
            if event.type == QUIT:
                RUNNING = False

            elif event.type == MOUSEBUTTONDOWN:
                now = pygame.time.get_ticks()
                double_click = (now - last_click) <= double_click_duration
                last_click = pygame.time.get_ticks()
                if not READONLY:
                    toolbar.tool.handle_mouse_down(event, double_click)

            if not READONLY:
                if event.type == MOUSEBUTTONUP:
                    toolbar.tool.handle_mouse_up(event)
                elif event.type == MOUSEMOTION:
                    toolbar.tool.handle_mouse_move(event)

        # Rendering
        clock.tick(framerate)
        screen.blit(bg, (0, 0))

        if not READONLY:
            toolbar.tool.render_preview(screen)

        for connection in graph.connections:
            connection.render(screen, font)

        for node in graph.nodes:
            node.render(screen, font)

        pygame.display.update()
        pathMenu.update()
        if not READONLY:
            toolbar.update()

    if not READONLY:
        toolbar.destroy()

    pathMenu.destroy()


if __name__ == "__main__":
    main()
