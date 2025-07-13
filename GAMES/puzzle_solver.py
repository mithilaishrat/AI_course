import pygame
import time
from copy import deepcopy


DIRECTIONS = {"U": [-1, 0], "D": [1, 0], "L": [0, -1], "R": [0, 1]}


END = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
END_KEY = tuple(tuple(row) for row in END)

#class for A* search
class Node:
    def __init__(self, current_node, previous_key, g, h, dir):
        self.current_node = current_node
        self.previous_key = previous_key
        self.g = g
        self.h = h
        self.dir = dir
        self.key = tuple(tuple(row) for row in current_node)

    def f(self):
        return self.g + self.h

def get_pos(state, element):
    for row in range(len(state)):
        if element in state[row]:
            return (row, state[row].index(element))

def manhattanCost(state):
    cost = 0
    for row in range(3):
        for col in range(3):
            val = state[row][col]
            if val != 0:
                goal_row, goal_col = get_pos(END, val)
                cost += abs(row - goal_row) + abs(col - goal_col)
    return cost

def getAdjNode(node):
    adj_nodes = []
    empty_pos = get_pos(node.current_node, 0)

    for dir in DIRECTIONS:
        new_row = empty_pos[0] + DIRECTIONS[dir][0]
        new_col = empty_pos[1] + DIRECTIONS[dir][1]
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_state = deepcopy(node.current_node)
            new_state[empty_pos[0]][empty_pos[1]] = new_state[new_row][new_col]
            new_state[new_row][new_col] = 0
            adj_nodes.append(Node(new_state, node.key, node.g + 1, manhattanCost(new_state), dir))
    return adj_nodes

def getBestNode(openSet):
    best_node = None
    best_f = float('inf')
    for node in openSet.values():
        if node.f() < best_f:
            best_node = node
            best_f = node.f()
    return best_node

def buildPath(closedSet, end_key):
    node = closedSet[end_key]
    path = []
    while node.previous_key is not None:
        path.append({'dir': node.dir, 'node': node.current_node})
        node = closedSet[node.previous_key]
    path.append({'dir': '', 'node': node.current_node})
    path.reverse()
    return path

def astar_main(puzzle):
    start_key = tuple(tuple(row) for row in puzzle)
    open_set = {start_key: Node(puzzle, None, 0, manhattanCost(puzzle), "")}
    closed_set = {}

    while open_set:
        current_node = getBestNode(open_set)
        closed_set[current_node.key] = current_node

        if current_node.key == END_KEY:
            return buildPath(closed_set, END_KEY)

        for neighbor in getAdjNode(current_node):
            if neighbor.key in closed_set:
                continue
            if neighbor.key not in open_set or neighbor.f() < open_set[neighbor.key].f():
                open_set[neighbor.key] = neighbor

        del open_set[current_node.key]

# Pygame Part
WIDTH, HEIGHT = 300, 400
TILE_SIZE = 100
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 100, 100)
BUTTON_COLOR = (70, 130, 180)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("8 Puzzle A* Solver")
font = pygame.font.SysFont(None, 50)
button_font = pygame.font.SysFont(None, 35)

def draw_grid(state):
    screen.fill(WHITE)
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            rect = pygame.Rect(j*TILE_SIZE, i*TILE_SIZE, TILE_SIZE, TILE_SIZE)
            pygame.draw.rect(screen, RED if value == 0 else BLACK, rect)
            if value != 0:
                text = font.render(str(value), True, WHITE)
                text_rect = text.get_rect(center=rect.center)
                screen.blit(text, text_rect)
            pygame.draw.rect(screen, BLACK, rect, 3)

def draw_button(text):
    btn_rect = pygame.Rect(75, 320, 150, 50)
    pygame.draw.rect(screen, BUTTON_COLOR, btn_rect)
    txt = button_font.render(text, True, WHITE)
    txt_rect = txt.get_rect(center=btn_rect.center)
    screen.blit(txt, txt_rect)
    return btn_rect

def main_game():
    running = True
    start_state = [[0,8, 7], [6, 5, 4], [3, 2, 1]]
    solution = []
    button_rect = draw_button("Solve")
    draw_grid(start_state)
    pygame.display.flip()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and button_rect.collidepoint(event.pos):
                solution = astar_main(start_state)
                for step in solution:
                    draw_grid(step['node'])
                    pygame.display.flip()
                    time.sleep(0.6)

        pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
    main_game()
