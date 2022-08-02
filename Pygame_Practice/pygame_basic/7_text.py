import pygame

pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Nado Game") # 게임 이름

# FPS
clock = pygame.time.Clock()

# 배경 이미지 불러오기 (그림판에서 화면 크기에 맞게 제작, png)
background = pygame.image.load("C:\\Users\\hakna\\Desktop\\Python_Workspace\\Del_project\\pygame_Tutorial\\Del_project\\pygame_basic\\background.png")

# 스프라이트(캐릭터) 불러오기 (그림판 ")
character = pygame.image.load("C:\\Users\\hakna\\Desktop\\Python_Workspace\\Del_project\\pygame_Tutorial\\Del_project\\pygame_basic\\character.png")
character_size = character.get_rect().size # 이미지 크기를 구해옴
character_width = character_size[0] # 캐릭터 가로 크기
character_height = character_size[1] # 캐릭터 세로 크기
character_x_pos = (screen_width / 2) - (character_width / 2)  # 화면 가로의 절반 크기에 해당하는 곳에 위치 (가로 중간), 중앙 위치를 위해 기점을 살짝 중앙에서 왼쪽으로 이동 => -(character_width / 2)
character_y_pos = screen_height - character_height # 화면 세로 크기 가장 아래에 해당하는 곳에 위치 (세로 하단), 배경화면-캐릭터 높이를 계산하여 기점을 확실히 잡음 (그림은 (x,y) 기점으로 오른쪽, 아래로 그려짐)    

# 이동할 좌표
to_x = 0
to_y = 0

# 이동 속도
character_speed = 0.6

# 적 enemy 캐릭터
enemy = pygame.image.load("C:\\Users\\hakna\\Desktop\\Python_Workspace\\Del_project\\pygame_Tutorial\\Del_project\\pygame_basic\\enemy.png")
enemy_size = enemy.get_rect().size 
enemy_width = enemy_size[0] 
enemy_height = enemy_size[1] 
enemy_x_pos = (screen_width / 2) - (enemy_width / 2)  
enemy_y_pos = (screen_height / 2) - (enemy_height / 2)

# 폰트 정의
game_font = pygame.font.Font(None, 40)  # 폰트 객체 생성 (폰트, 크기)

# 총 시간
total_time = 10

# 시작 시간
start_ticks = pygame.time.get_ticks()   # 현재 tick을 받아옴

# 이벤트 루프 (프로그램 끝나기x)
running = True # 게임이 진행중인가?
while running:
    dt = clock.tick(60) # 게임화면의 초당 프레임 수를 설정

# 캐릭터가 100 만큼 이동해야함
# 10 fps : 1초 동안에 10번 동작 => 1번에 10만큼 이동, 10 * 10 = 100
# 20 fps : 1초 동안에 20번 동작 => 1번에 5만큼 이동, 5 * 20 = 100     => 즉 이동하는 값이 달라짐

    print("fps : " + str(clock.get_fps()))

    for event in pygame.event.get():    # 무조건 작성해야 함, 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT:   #창을 닫히는 이벤트가 발생하였는가?
            running = False # 게임이 진행중이 아님

        if event.type == pygame.KEYDOWN:    # 키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT:  # 캐릭터를 왼쪽으로
                to_x -= character_speed   # to_x = to_x - 5
            elif event.key ==pygame.K_RIGHT: # 캐릭터를 오른쪽으로
                to_x += character_speed
            elif event.key ==pygame.K_UP:   # 캐릭터를 위로
                to_y -= character_speed
            elif event.key ==pygame.K_DOWN: # 캐릭터를 아래로
                to_y += character_speed

        if event.type == pygame.KEYUP:  # 방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    # 캐릭터 실제 좌표 바꾸기
    character_x_pos += to_x * dt    # fps 곱하기 (fps에 따라 속도가 변하면 안됨, fps가 달라져도 속도 고정)
    character_y_pos += to_y * dt
    
    # 가로 경계값 처리
    if character_x_pos < 0: # 화면 왼쪽보다 이전으로 더 나갔다는 뜻
        character_x_pos = 0 # 멈춰있을 거임
    elif character_x_pos > screen_width - character_width: # 사각형의 왼쪽 상단점이 기점, 오른쪽 끝에 못나가는 것처럼 보임
        character_x_pos = screen_width - character_width

    # 세로 경계값 처리
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    # 충돌 처리를 위한 rect정보 업데이트
    character_rect = character.get_rect()   # 캐릭터가 가지는 rect 정보 가져오기
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()     # enemy 좌표 업데이트
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # 충돌 체크
    if character_rect.colliderect(enemy_rect):   # 사각형 기준 충돌 여부 확인
        print("충돌했어요")
        running = False
    

    screen.blit(background, (0, 0)) # 배경 그리기
    screen.blit(character, (character_x_pos, character_y_pos))  # 캐릭터 그리기
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))  # 적 그리기

    # 타이머 집어 넣기
    # 경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000   # 경과 시간(ms)을 1000으로 나누어서 초(s) 단위로 표시
    
    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255, 255, 255))  # 글자 그리기, ms부분은 지우기 위해 int, (출력할 글자, True, 글자색상)
    screen.blit(timer, (10, 10))

    # 만약 시간이 0 이하이면 게임 종료
    if total_time - elapsed_time <= 0:
        print("타임아웃")
        running = False

    pygame.display.update() # 게임화면을 다시 그리기! (반드시)

# 잠시 대기
pygame.time.delay(2000) # 2초 정도 대기(ms)

# pygame 종료
pygame.quit()