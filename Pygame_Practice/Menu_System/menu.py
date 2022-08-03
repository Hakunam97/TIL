import pygame

class Menu():
    def __init__(self, game):   # use reference of game object(game.py)
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2   # 화면 중간
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)    # (x, y) = (0, 0) 그리고 size는 20x20
        self.offset = - 100 # 커서가 글자 위로 가는걸 원하지 않음, to the x position

    def draw_cursor(self):
        self.game.draw_text('*', 15, self.cursor_rect.x, self.cursor_rect.y)   # game.py의 def지정 함수, reference로서 사용

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()

class MainMenu(Menu): # (inherit)
    def __init__(self, game):
        Menu.__init__(self,game)
        self.state = "Start"
        self.startx, self.starty = self.mid_w, self.mid_h + 30  # start버튼 가운데에서 조금 위로 배치
        self.optionsx, self.optionsy = self.mid_w, self.mid_h + 50  # 
        self.creditsx, self.creditsy = self.mid_w, self.mid_h + 70  #
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)  # 마우스 커서 위치

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text("Main Menu", 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 20) # 약간 위로
            self.game.draw_text("Start Game", 20, self.startx, self.starty)
            self.game.draw_text("Options", 20, self.optionsx, self.optionsy)
            self.game.draw_text("Credits", 20, self.creditsx, self.creditsy)
            self.draw_cursor()
            self.blit_screen()

    # move cursor
    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Options'
            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state == 'Credits'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state == 'Start'
        elif self.game.UP_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state == 'Start'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
                self.state == 'Options'

    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'Start':
                self.game.playing = True
            elif self.state == 'Options':
                pass
            elif self.state == 'Credits':
                pass
            self.run_display = False
        