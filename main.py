"""
The main module
"""
import os

import pygame
from pygame.locals import QUIT, MOUSEMOTION, MOUSEBUTTONUP, MOUSEBUTTONDOWN

from models import Graph, Node, Connection
from views import ToolBar

RUNNING = True
bg=pygame.image.load("bg.png")


def quit_callback():
    """
    This method marks the exit of the program.
    """
    global RUNNING
    RUNNING = False


def on_node_hover(graph):
    """
    This method marks the nodes that are hovered onto by the mouse.
    """
    for node in graph.nodes:
        node.hovered = False
        if node.pos[0] <= pygame.mouse.get_pos()[0]+node.radius and \
            node.pos[0] >= pygame.mouse.get_pos()[0]-node.radius and \
                node.pos[1] <= pygame.mouse.get_pos()[1]+node.radius and \
        node.pos[1] >= pygame.mouse.get_pos()[1]-node.radius:
            node.hovered = True


def main():
    """
    This is the main method of the program
    """
    global RUNNING

    # sets the window position
    os.environ['SDL_VIDEO_WINDOW_POS'] = f"{100},{100}"

    # initialize pygame
    pygame.init()
    pygame.font.init()

    # Add the Nodes and Connections
    nodesPreset = [Node('a', (50, 150)), Node('b', (50, 300)),
                   Node('c', (200,150)), Node('d', (200,300))]
    
    connectionPreset = [Connection((nodesPreset[0], nodesPreset[1]), 4, (0, 50, 50)),
                        Connection((nodesPreset[0], nodesPreset[2]), 3, (0, 50, 50)),
                        Connection((nodesPreset[1], nodesPreset[2]), 2, (0, 50, 50)),
                        Connection((nodesPreset[1], nodesPreset[3]), 1, (0, 50, 50)),
                        Connection((nodesPreset[2], nodesPreset[3]), 5, (0, 50, 50))
                        ]
    graph = Graph(nodesPreset, connectionPreset)

    # initialize tkinter
    toolbar = ToolBar(graph)
    toolbar.geometry(
        f'{toolbar.winfo_width()}x{toolbar.winfo_height()}+1+600')
    toolbar.protocol("WM_DELETE_WINDOW", quit_callback)

    # start pygame clock
    clock = pygame.time.Clock()

    # initialize variables
    font = pygame.font.SysFont("Consolas", 15)
    framerate = 30
    double_click_duration = 150  # ms
    last_click = 0

    # sets the window title
    screen = pygame.display.set_caption('Dijkstra 2019-2020')
    
    # sets the window size
    screen = pygame.display.set_mode((1022, 752))

    while RUNNING:
        for event in pygame.event.get():
            if event.type == QUIT:
                RUNNING = False
            elif event.type == MOUSEMOTION:
                toolbar.tool.handle_mouse_move(event)

                on_node_hover(graph)
            elif event.type == MOUSEBUTTONDOWN:
                now = pygame.time.get_ticks()
                double_click = (now - last_click) <= double_click_duration
                last_click = pygame.time.get_ticks()

                toolbar.tool.handle_mouse_down(event, double_click)

            elif event.type == MOUSEBUTTONUP:
                toolbar.tool.handle_mouse_up(event)

        # Rendering
        clock.tick(framerate)
        screen.blit(bg,(0,0))

        toolbar.tool.render_preview(screen)

        for connection in graph.connections:
            connection.render(screen, font)

        for node in graph.nodes:
            node.render(screen, font)

        pygame.display.update()

        toolbar.update()
        # try:
        # except Exception as exc:
        #     print("ToolBar error")

    toolbar.destroy()


if __name__ == "__main__":
    main()
