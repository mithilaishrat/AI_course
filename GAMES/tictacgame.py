import pygame
import sys

# Initialization 

pygame.init()


WIDTH, HEIGHT = 300, 350
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LINE_COLOR = (10, 10, 10)
X_COLOR = (200, 0, 0)
O_COLOR = (0, 0, 200)
LINE_WIDTH = 5
FONT = pygame.font.SysFont(None, 80)
SMALL_FONT = pygame.font.SysFont(None, 40)

board = [' '] * 10  
player = 'O'
computer = 'X'


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe AI")

def draw_board():
    screen.fill(WHITE)
    
    for i in range(1, 3):
        pygame.draw.line(screen, LINE_COLOR, (0, i * 100), (300, i * 100), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (i * 100, 0), (i * 100, 300), LINE_WIDTH)
    # Draw marks
    for i in range(1, 10):
        x = ((i - 1) % 3) * 100 + 50
        y = ((i - 1) // 3) * 100 + 50
        if board[i] == 'X':
            text = FONT.render('X', True, X_COLOR)
            screen.blit(text, text.get_rect(center=(x, y)))
        elif board[i] == 'O':
            text = FONT.render('O', True, O_COLOR)
            screen.blit(text, text.get_rect(center=(x, y)))

def space_is_free(pos):
    return board[pos] == ' '

def check_draw():
    return all(space != ' ' for space in board[1:])

def check_win():
    wins = [(1,2,3), (4,5,6), (7,8,9),
            (1,4,7), (2,5,8), (3,6,9),
            (1,5,9), (3,5,7)]
    for a,b,c in wins:
        if board[a] == board[b] == board[c] and board[a] != ' ':
            return board[a]
    return None

def minimax(is_max):
    winner = check_win()
    if winner == computer:
        return 1
    elif winner == player:
        return -1
    elif check_draw():
        return 0
   #recursive condition 
    if is_max:
        best = -float('inf')
        for i in range(1, 10):
            if board[i] == ' ':
                board[i] = computer
                score = minimax(False)
                board[i] = ' '
                best = max(best, score)
        return best
    else:
        best = float('inf')
        for i in range(1, 10):
            if board[i] == ' ':
                board[i] = player
                score = minimax(True)
                board[i] = ' '
                best = min(best, score)
        return best

def computer_move():
    best_score = -float('inf')
    best_move = 0
    for i in range(1, 10):
        if board[i] == ' ':
            board[i] = computer
            score = minimax(False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                best_move = i
    board[best_move] = computer

def show_result(text):
    message = SMALL_FONT.render(text, True, BLACK)
    screen.blit(message, message.get_rect(center=(WIDTH // 2, HEIGHT - 25)))

# loop
running = True
player_turn = True
winner = None
game_over = False

while running:
    screen.fill(WHITE)
    draw_board()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if not game_over and player_turn and event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if y < 300:
                col, row = x // 100, y // 100
                pos = row * 3 + col + 1
                if 1 <= pos <= 9 and space_is_free(pos):
                    board[pos] = player
                    player_turn = False

    if not game_over and not player_turn:
        pygame.time.wait(500)
        computer_move()
        player_turn = True

    winner = check_win()
    if winner and not game_over:
        show_result(f"{winner} wins!")
        game_over = True
    elif check_draw() and not game_over:
        show_result("It's a draw!")
        game_over = True

    pygame.display.update()

pygame.quit()
sys.exit()
  