import pygame
from menu import *


class Game():
    def __init__(self):
        pygame.init()
        self.running, self.playing = True, False    # 2가지 Loop
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False  # player가 눌렀을 때 True로
        self.DISPLAY_W, self.DISPLAY_H = 800, 600   # width, height (canvas size)
        self.display = pygame.Surface((self.DISPLAY_W, self.DISPLAY_H))
        self.window = pygame.display.set_mode(((self.DISPLAY_W, self.DISPLAY_H)))
        self.font_name = 'DungGeunMo.ttf' 
        #self.font_name = pygame.font.get_default_font()
        self.BLACK, self.WHITE = (0, 0, 0), (255, 255, 255)
        self.main_menu = MainMenu(self)
        self.options = OptionsMenu(self)
        self.credits = CreditsMenu(self)
        self.curr_menu = self.main_menu

    def game_loop(self):
        while self.playing: # Loop
            self.check_events() # event 확인, 아래 def로 지정한 함수
            if self.START_KEY:
                self.playing = False
            self.display.fill(self.BLACK)
            self.draw_text('Thanks for Playing', 40, self.DISPLAY_W / 2, self.DISPLAY_H / 2)    # 화면 센터에 표시, def지정 함수
            self.window.blit(self.display, (0, 0))
            pygame.display.update()
            self.reset_keys()   # 다시 모든key False로, def지정 함수


    # make game loop
    # check the player inputs and button press
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.curr_menu.run_display = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN: 
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True

            
    # reset variables
    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False

    def draw_text(self, text, size, x, y):
        font = pygame.font.Font(self.font_name,size)
        text_surface = font.render(text, True, self.WHITE)  # 글자 나타내기
        text_rect = text_surface.get_rect() # 사각형틀 잡기
        text_rect.center = (x, y)
        self.display.blit(text_surface, text_rect)

    
