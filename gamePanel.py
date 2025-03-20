import pygame
import sys

class gameDisplay:

    def __init__(self, board):
        self.board = board
        self.WIDTH, self.HEIGHT = 1000, 800
        self.ChessWIDTH, self.ChessHEIGHT = 700, 700
        self.SQUARE_SIZE = self.ChessWIDTH // 8
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.BROWN = (139, 69, 19)
        self.BEIGE = (245, 245, 220)
        self.font = None
        self.small_font = None
        self.screen = None
        self.running = True


    def initGameDisplay(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption('ChessPy')

        self.font = pygame.font.Font("segoe-ui-symbol.ttf", 74)
        self.small_font = pygame.font.Font("segoe-ui-symbol.ttf", 36)


    def draw_button(self, text, x, y, width, height, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        button_color = (255, 255, 255) 
        hover_color = (150, 150, 150)  
        text_color = self.BLACK

        if x < mouse[0] < x + width and y < mouse[1] < y + height:
            pygame.draw.rect(self.screen, hover_color, (x, y, width, height))
            if click[0] == 1 and action:
                action() 
        else:
            pygame.draw.rect(self.screen, button_color, (x, y, width, height))

        text_surf = self.small_font.render(text, True, text_color)
        text_rect = text_surf.get_rect(center=((x + (width // 2)), (y + (height // 2))))
        self.screen.blit(text_surf, text_rect)


    def show_start_screen(self):
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    waiting = False

            self.screen.fill(self.BLACK)

            title_text = self.font.render("Chess!", True, self.WHITE)
            title_rect = title_text.get_rect(center=(self.WIDTH // 2, self.HEIGHT // 2 - 180))
            self.screen.blit(title_text, title_rect)

            self.draw_button('Player vs Player', 350, 300, 300, 100, self.player_vs_player)
            self.draw_button('Player vs AI', 350, 420, 300, 100, self.player_vs_player)
            self.draw_button('Sair', 350, 540, 300, 100, self.quit_game) 

            pygame.display.flip()

    def draw_board(self):
        start_x = (self.WIDTH - self.ChessWIDTH) // 2
        start_y = (self.HEIGHT - self.ChessHEIGHT) // 2
        for row in range(8):
            for col in range(8):
                color = self.BEIGE if (row + col) % 2 == 0 else self.BROWN
                pygame.draw.rect(self.screen, color, (start_x + col * self.SQUARE_SIZE, start_y + row * self.SQUARE_SIZE, self.SQUARE_SIZE, self.SQUARE_SIZE)) 

    def draw_pieces(self):
        piece_unicode = {
            'King Black': '♔', 'Queen Black': '♕', 'Rook Black': '♖', 
            'Bishop Black': '♗', 'Knight Black': '♘', 'Pawn Black': '♙',
            'King White': '♚', 'Queen White': '♛', 'Rook White': '♜', 
            'Bishop White': '♝', 'Knight White': '♞', 'Pawn White': '♟'
        }

        start_x = (self.WIDTH - self.ChessWIDTH) // 2
        start_y = (self.HEIGHT - self.ChessHEIGHT) // 2

        for row in range(8):
            for col in range(8):
                piece = self.board.getPiece((row, col))
                if piece != 0: 
                    piece_char = piece_unicode.get(piece.__str__())
                    print(piece_char)
                    if piece_char:
                        text_surface = self.font.render(piece_char, True, self.BLACK if piece.color == 'Black' else self.WHITE)
                        text_rect = text_surface.get_rect(center=(
                        start_x + col * self.SQUARE_SIZE + self.SQUARE_SIZE // 2, 
                        start_y + row * self.SQUARE_SIZE + self.SQUARE_SIZE // 2))
                    self.screen.blit(text_surface, text_rect)


    def display_capture(self):
            rowWhitePiece = ""
            rowBlackPiece = ""

            if self.board.blackCapture or self.board.whiteCapture:
                print("White captures: ")
                if self.board.whiteCapture:
                    for piece in self.board.whiteCapture:
                        rowBlackPiece += f" {piece.__str__()[0]} "
                print(rowBlackPiece)
                print("Black captures: ")
                if self.board.blackCapture:
                    for piece in self.board.blackCapture:
                        rowWhitePiece += f" {piece.__str__()[0]} "
                print(rowWhitePiece)

    def display_game(self):
        self.draw_board()
        self.draw_pieces()
        self.display_capture()

        pygame.display.flip()

    def player_vs_player(self):
        print("Player vs Player selected!")
        self.game_loop()

    def game_loop(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit_game()

            self.display_game()

    def quit_game(self):
        print("Sair!")
        pygame.quit()
        sys.exit()
