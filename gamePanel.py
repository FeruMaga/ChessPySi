import pygame
import sys

class gameDisplay:

    def __init__(self):
        self.WIDTH, self.HEIGHT = 800, 600
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.font = None
        self.small_font = None
        self.screen = None

    def initGameDisplay(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption('ChessPy')

        self.font = pygame.font.Font(None, 74)
        self.small_font = pygame.font.Font(None, 36)

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
            title_rect = title_text.get_rect(center=(self.WIDTH // 2, self.HEIGHT // 2 - 150))
            self.screen.blit(title_text, title_rect)

            self.draw_button('Player vs Player', 300, 200, 200, 50, self.player_vs_player)
            self.draw_button('Player vs AI', 300, 300, 200, 50, self.player_vs_player)
            self.draw_button('Sair', 300, 400, 200, 50, self.quit_game) 

            pygame.display.flip()

    def player_vs_player(self):
        print("Player vs Player selected!")
        pygame.quit()
        sys.exit()

    def player_vs_ai(self):
        print("Player vs AI selected!")
        pygame.quit()
        sys.exit()

    def quit_game(self):
        print("Sair!")
        pygame.quit()
        sys.exit()
