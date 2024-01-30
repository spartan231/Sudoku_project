import pygame, sys
from constrants import *
from cell import *
from board import *
from sudoku_generator import *

def return_board(board):
    boardf = [[0 for i in range(9) for j in range(9)]]
    for row in range(len(board[:])):
        for col in range(len(board[row][:])):
            boardf[row][col] = board[row][col]
    return boardf

def main_menu(screen):
    # initalize the title fonts for title + button
    start_title = pygame.font.Font(None, 70)
    message_title = pygame.font.Font(None, 55)
    button_ez = pygame.font.Font(None, 40)
    button_med = pygame.font.Font(None, 40)
    button_hard = pygame.font.Font(None, 40)

    # sets the background color
    screen.fill(BG_COLOR)

    # initalize and draw title
    title_surface = start_title.render("Welcome to Sudoku", 0, (0, 0, 0))
    title_rectangle = title_surface.get_rect( center = (WIDTH // 2, HEIGHT//2 -100))
    screen.blit(title_surface, title_rectangle)

    other_surface = message_title.render("Select Game Mode:", 0, (0,0,0))
    other_rect = other_surface.get_rect(center = (WIDTH // 2, HEIGHT//2+10))
    screen.blit(other_surface, other_rect)

    # initalizes the buttons
    #font_e = pygame.font.SysFont('Georgia', 40)
    #surf = font_e.render('EASY', True, (255,255,255))
    #easy_b = pygame.Rect(200,200,110,60)



    easy_text = button_ez.render("EASY", 0, (255, 255, 255))
    med_text = button_med.render("MEDIUM", 0, (255, 255, 255))
    hard_text = button_hard.render("HARD", 0, (255, 255,255))

    # initalize the button background color + text
    easy_surface = pygame.Surface((100 +20, 50 + 10))
    easy_surface.fill((LINE_COLOR))
    easy_surface.blit(easy_text, (20,20))


    med_surface = pygame.Surface((100 +20, 50 + 10))
    med_surface.fill((LINE_COLOR))
    med_surface.blit(med_text, (5, 20))

    hard_surface = pygame.Surface((100 +20, 50 + 10))
    hard_surface.fill((LINE_COLOR))
    hard_surface.blit(hard_text, (20, 20))


    easy_rect = easy_surface.get_rect(center = (WIDTH//2-200, HEIGHT//2 + 100))
    med_rect = med_surface.get_rect(center = (WIDTH//2 , HEIGHT//2 + 100))
    hard_rect = hard_surface.get_rect(center = (WIDTH // 2+200, HEIGHT//2 + 100))

    screen.blit(easy_surface, easy_rect)
    screen.blit(med_surface, med_rect)
    screen.blit(hard_surface, hard_rect)

    button_text = pygame.font.SysFont(None, 40)

    reset_text = button_text.render("RESET", 0, (255, 255, 255))
    restart_text = button_text.render("RESTART", 0, (255, 255, 255))
    exit_text = button_text.render("EXIT", 0, (255, 255, 255))

    reset_surface = pygame.Surface((reset_text.get_size()[0] + 20, reset_text.get_size()[1] + 10))
    reset_surface.fill((LINE_COLOR))
    reset_surface.blit(reset_text, (20, 20))

    restart_surface = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 10))
    restart_surface.fill((LINE_COLOR))
    restart_surface.blit(restart_text, (20, 20))

    exit_surface = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 10))
    exit_surface.fill((LINE_COLOR))
    exit_surface.blit(exit_text, (20, 20))

    reset_rect = reset_surface.get_rect(center=(WIDTH // 2 - 200, HEIGHT // 2 + 100))
    restart_rect = restart_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 100))
    exit_rect = exit_surface.get_rect(center=(WIDTH // 2 + 200, HEIGHT // 2 + 100))

    global board

    while True:
        for event in pygame.event.get():
<<<<<<< HEAD
            if menu:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if easy_rect.collidepoint(event.pos):
                        board = Board(9, 9, WIDTH, HEIGHT, 30, screen)
                        Board.draw(WIDTH, HEIGHT, screen, BOARD_ROWS, BOARD_COLS)
                        screen.blit(reset_surface, reset_rect)
                        screen.blit(restart_surface, restart_rect)
                        screen.blit(exit_surface, exit_rect)
                        board.sketch(screen)
                        menu = False
                        game = True
                    elif med_rect.collidepoint(event.pos):
                        board = Board(9, 9, WIDTH, HEIGHT, 40, screen)
                        Board.draw(WIDTH, HEIGHT, screen, BOARD_ROWS, BOARD_COLS)
                        screen.blit(reset_surface, reset_rect)
                        screen.blit(restart_surface, restart_rect)
                        screen.blit(exit_surface, exit_rect)
                        board.sketch(screen)
                        menu = False
                        game = True
                    elif hard_rect.collidepoint(event.pos):
                        board = Board(9, 9, WIDTH, HEIGHT, 50, screen)
                        Board.draw(WIDTH, HEIGHT, screen, BOARD_ROWS, BOARD_COLS)
                        screen.blit(reset_surface, reset_rect)
                        screen.blit(restart_surface, restart_rect)
                        screen.blit(exit_surface, exit_rect)
                        board.sketch(screen)
                        menu = False
                        game = True
            elif game:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    row = x/SQUARE_SIZE
                    col = y/SQUARE_SIZE
                    if exit_rect.collidepoint(event.pos):
                        pygame.quit()
                        quit()
                    elif reset_rect.collidepoint(event.pos):
                        #pygame.draw.rect(screen, (0, 0, 0), (3, 3, 100, 100), 5)
                        screen.blit(reset_surface, reset_rect)
                        screen.blit(restart_surface, restart_rect)
                        screen.blit(exit_surface, exit_rect)
                        board.reset_board()
                        board.sketch(screen)
                    elif restart_rect.collidepoint(event.pos):
                        game = False
                        menu = True
                        main_menu(screen)
                    if event.button == 1:
                        position = event.pos

                elif event.type == pygame.KEYDOWN and board.available_square(row, col):
                    if event.key == pygame.K_9:
                        board.mark_square(row, col, 9)
                        board.selected_square(row, col)
                        screen.blit(reset_surface, reset_rect)
                        screen.blit(restart_surface, restart_rect)
                        screen.blit(exit_surface, exit_rect)
                    if event.key == pygame.K_8:
                        board.mark_square(row, col, 8)
                        board.selected_square(row, col)
                        screen.blit(reset_surface, reset_rect)
                        screen.blit(restart_surface, restart_rect)
                        screen.blit(exit_surface, exit_rect)
                    if event.key == pygame.K_7:
                        board.mark_square(row, col, 7)
                        board.selected_square(row, col)
                        screen.blit(reset_surface, reset_rect)
                        screen.blit(restart_surface, restart_rect)
                        screen.blit(exit_surface, exit_rect)
                    if event.key == pygame.K_6:
                        board.mark_square(row, col, 6)
                        board.selected_square(row, col)
                        screen.blit(reset_surface, reset_rect)
                        screen.blit(restart_surface, restart_rect)
                        screen.blit(exit_surface, exit_rect)
                    if event.key == pygame.K_5:
                        board.mark_square(row, col, 5)
                        board.selected_square(row, col)
                        screen.blit(reset_surface, reset_rect)
                        screen.blit(restart_surface, restart_rect)
                        screen.blit(exit_surface, exit_rect)
                    if event.key == pygame.K_4:
                        board.mark_square(row, col, 4)
                        board.selected_square(row, col)
                        screen.blit(reset_surface, reset_rect)
                        screen.blit(restart_surface, restart_rect)
                        screen.blit(exit_surface, exit_rect)
                    if event.key == pygame.K_3:
                        board.mark_square(row, col, 3)
                        board.selected_square(row, col)
                        screen.blit(reset_surface, reset_rect)
                        screen.blit(restart_surface, restart_rect)
                        screen.blit(exit_surface, exit_rect)
                    if event.key == pygame.K_2:
                        board.mark_square(row, col, 2)
                        board.selected_square(row, col)
                        screen.blit(reset_surface, reset_rect)
                        screen.blit(restart_surface, restart_rect)
                        screen.blit(exit_surface, exit_rect)
                    if event.key == pygame.K_1:
                        board.mark_square(row, col, 1)
                        board.selected_square(row, col)
                        screen.blit(reset_surface, reset_rect)
                        screen.blit(restart_surface, restart_rect)
                        screen.blit(exit_surface, exit_rect)
                    if event.key == pygame.K_RETURN:
                        board.final_square(row,col)
                        screen.blit(reset_surface, reset_rect)
                        screen.blit(restart_surface, restart_rect)
                        screen.blit(exit_surface, exit_rect)





                # elif reset_rect.collidepoint(event.pos):
=======
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_rect.collidepoint(event.pos):
                    genSudoku = generate_sudoku(9, 30)
                    board1 = return_board(genSudoku)
                    board = Board(9, 9, WIDTH, HEIGHT, "easy", board1, genSudoku)
                    screen.blit(reset_surface, reset_rect)
                    screen.blit(restart_surface, restart_rect)
                    screen.blit(exit_surface, exit_rect)
                elif med_rect.collidepoint(event.pos):
                    genSudoku = generate_sudoku(9, 40)
                    board1 = return_board(genSudoku)
                    board = Board(9, 9, WIDTH, HEIGHT, "medium", board1, genSudoku)
                    screen.blit(reset_surface, reset_rect)
                    screen.blit(restart_surface, restart_rect)
                    screen.blit(exit_surface, exit_rect)
                elif hard_rect.collidepoint(event.pos):
                    genSudoku = generate_sudoku(9, 50)
                    board1 = return_board(genSudoku)
                    board = Board(9, 9, WIDTH, HEIGHT, "hard", board1, genSudoku)
                    screen.blit(reset_surface, reset_rect)
                    screen.blit(restart_surface, restart_rect)
                    screen.blit(exit_surface, exit_rect)
                if exit_rect.collidepoint(event.pos):
                    sys.exit()
                elif reset_rect.collidepoint(event.pos):
                    genSudoku = board1
                    board = Board(9,9,WIDTH, HEIGHT, gamewindow(), board1, genSudoku)
                    screen.blit(reset_surface, reset_rect)
                    screen.blit(restart_surface, restart_rect)
                    screen.blit(exit_surface, exit_rect)
>>>>>>> 6d08c014514e73e9ce4a2ea82554d04240437769

        pygame.display.update()
def gamewindow(diff):
    board = generate_sudoku(9, diff)
    board = Board()

def game_won(screen):
    won_title = pygame.font.Font(None, 70)
    exit_font = pygame.font.Font(None, 55)

    screen.fill(BG_COLOR)

    title_surface = won_title.render("Game Won!", 0, (0, 0, 0))
    title_rectangle = title_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 - 150))
    screen.blit(title_surface, title_rectangle)

    exit_text = exit_font.render("EXIT", 0, (255, 255, 255))
    exit_surface = pygame.Surface((exit_text.get_size()[0]+20, exit_text.get_size()[1] + 10))
    exit_surface.fill((0, 139, 186))
    exit_surface.blit(exit_text, (10, 10))

    exit_rect = exit_surface.get_rect(center = (WIDTH//2, HEIGHT//2 ))
    screen.blit(exit_surface, exit_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if exit_rect.collidepoint(event.pos):
                    sys.exit()

        pygame.display.update()

def game_over(screen):
    exit_title = pygame.font.Font(None, 70)
    restart_title = pygame.font.Font(None, 55)

    screen.fill(BG_COLOR)


    title_surface = exit_title.render("Game Over :(", 0, (0,0,0))
    title_rectangle = title_surface.get_rect(center = (WIDTH//2, HEIGHT//2 -150))
    screen.blit(title_surface, title_rectangle)

    restart_text = restart_title.render("RESTART", 0, (255, 255, 255))
    restart_surface = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 10))
    restart_surface.fill((0,139,186))
    restart_surface.blit(restart_text, (10,10))

    restart_rect = restart_surface.get_rect(center = (WIDTH//2, HEIGHT//2 ))
    screen.blit(restart_surface, restart_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_rect.collidepoint(event.pos):
                    print("restart")
                    main_menu(screen)

        pygame.display.update()


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Sudoku")
    main_menu(screen)