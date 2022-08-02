import pygame

pygame. init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Nado Game") # 게임 이름

# 배경 이미지 불러오기 (그림판에서 화면 크기에 맞게 제작, png)
background = pygame.image.load("C:\\Users\\hakna\\OneDrive\\바탕 화면\\pygame_Tutorial\\Del_project\\pygame_Tutorial\\pygame_basic\\background.png")

# 스프라이트(캐릭터) 불러오기 (그림판 ")
character = pygame.image.load("C:\\Users\\hakna\\OneDrive\\바탕 화면\\pygame_Tutorial\\Del_project\\pygame_Tutorial\\pygame_basic\\character.png")
character_size = character.get_rect().size # 이미지 크기를 구해옴
character_width = character_size[0] # 캐릭터 가로 크기
character_height = character_size[1] # 캐릭터 세로 크기
character_x_pos = (screen_width / 2) - (character_width / 2)  # 화면 가로의 절반 크기에 해당하는 곳에 위치 (가로 중간), 중앙 위치를 위해 기점을 살짝 중앙에서 왼쪽으로 이동 => -(character_width / 2)
character_y_pos = screen_height - character_height # 화면 세로 크기 가장 아래에 해당하는 곳에 위치 (세로 하단), 배경화면-캐릭터 높이를 계산하여 기점을 확실히 잡음 (그림은 (x,y) 기점으로 오른쪽, 아래로 그려짐)       

# 이벤트 루프 (프로그램 끝나기x)
running = True # 게임이 진행중인가?
while running:
    for event in pygame.event.get():    # 무조건 작성해야 함, 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT:   #창을 닫히는 이벤트가 발생하였는가?
            running = False # 게임이 진행중이 아님

    screen.blit(background, (0, 0)) # 배경 그리기

    screen.blit(character, (character_x_pos, character_y_pos))  # 캐릭터 그리기

    pygame.display.update() # 게임화면을 다시 그리기! (반드시)

# pygame 종료
pygame.quit()