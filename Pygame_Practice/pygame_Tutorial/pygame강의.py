# 1. pygame 모듈 불러오기
import sys
from turtle import position
import pygame
import math
import random
from pygame.locals import * 

# 2. 초기화 및 화면 만들기
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
acc = [0, 0]    # 81번줄로
arrows = []    # arrows를 리스트로 만듬
badtimer = 100    # 적들이 출현하는 시간 간격 조정
badtimer1 = 0
badguys = [[640, 100]]    # 맨 처음 이 위치에서 출발
healthvalue = 194    # 초기 체력
pygame.mixer.init()

# 3. 이미지 가져오기
player = pygame.image.load("resources/images/dude.png")    # 외부에서 다운 받은 이미지 소스 불러오기, 아직 화면에 보이진 않음
grass = pygame.image.load("resources/images/grass.png")    # 배경 불러오기
castle = pygame.image.load("resources/images/castle.png")
arrow = pygame.image.load("resources/images/bullet.png")  
badguyimg = pygame.image.load("resources/images/badguy.png")
healthbar = pygame.image.load("resources/images/healthbar.png")
health = pygame.image.load("resources/images/health.png")
gameover = pygame.image.load("resources/images/gameover.png")
youwin = pygame.image.load("resources/images/youwin.png")

keys = [False, False, False, False]    # 4개의 값을 가지고 있는 list형 변수 = keys, 왼쪽부터 [0, 1, 2, 3]
playpos = [100, 100]      # 키보드로 움직이게 하기 위해 미리 변수 설정, 48번줄로 이동

# 3-1. Load audio
hit = pygame.mixer.Sound("resources/audio/explode.wav")
enemy = pygame.mixer.Sound("resources/audio/enemy.wav")
shoot = pygame.mixer.Sound("resources/audio/shoot.wav")
hit.set_volume(0.05)
enemy.set_volume(0.05)
shoot.set_volume(0.05)
pygame.mixer.music.load('resources/audio/moonlight.wav')
pygame.mixer.music.play(-1, 0.0)    # -1이 들어가면 무한 반복 플레이
pygame.mixer.music.set_volume(0.25)

# 4. 계속 화면 보이기

running = 1
exitcode = 0

while running:    # running이 0이 되면 실행 x
    badtimer1 -= 1    # 타이머가 계속 줄어듬
    # 5. 화면을 깨끗하게 하기
    screen.fill((0, 0, 0))    # (R, G, B)

    # 6. 모든 요소들을 다시 그린다. (레이어처럼 배경 먼저 작성)
    for x in range(width//grass.get_width() + 1):    # grass.get_width() 는 100 (이미지 폭), //는 소수점을 버림 = 6, 나머지 40 공간 채우기 위해 +1
        for y in range(height//grass.get_height() + 1 ):     # y축
            screen.blit(grass, (x*100, y*100))    # x나 y는 0, 1, 2, 3 ... 이기 때문에 100 곱하기

    screen.blit(castle, (0, 30))
    screen.blit(castle, (0, 135))
    screen.blit(castle, (0, 240))
    screen.blit(castle, (0, 345))    # blit : 첫번째 그림을 두번째 장소로 옮김
            

    # 6-1. Set player position and rotation
    position = pygame.mouse.get_pos()    # 마우스의 위치값 전달 함수
    angle = math.atan2(position[1] - (playpos[1] + 32), position[0] - (playpos[0]+26)) # atan2(y, x) = atan(y/x)
    playerrot = pygame.transform.rotate(player, 360 - angle * 57.29)    # 57.29 -> 2파이 : 360 = 1 : ? (?가 57.29)
    playpos1 = (playpos[0] - playerrot.get_rect().width//2, playpos[1] - playerrot.get_rect().height//2) # get_rect : 사각형 정보값, 회전할 때 중앙을 기점으로 맞추기 위해
    screen.blit(playerrot, playerpos1)
    
    # 6-2. Draw arrows
    for bullet in arrows:    # bullet <== [각도, 플레이어의 x좌표, 플레이어의 y좌표] (아래 append함수에서)
        index = 0
        velx = math.con(bullet[0]) * 10    # 각도, x방향 속도
        vely = math.sin(bullet[0]) # 10    # y방향 속도
        bullet[1] += velx    # velx만큼 화살 움직이게 하기
        bullet[2] += vely
        if bullet[1] <- 64 or bullet[1] > 640 or bullet[2] <- 64 or bullet[2] > 480:    # 화면 밖으로 나갔다는 의미
            arrows.pop(index)    # pop은 index를 없애기(삭제)
        index += 1

    for projectile in arrows:    # 화살을 화면에 나오게 하기
        arrow1 = pygame.transform.rotate(arrow, 360 - projectile[0] * 57.29)    # projectile[0]은 각도 from bullet
        screen.blit(arrow1, (projectile[1], projectile[2]))

    # 6-3. Draw Badguys
    if badtimer == 0:
        badguys.append([640, random.randint(50, 430)])    # x좌표는 640, y좌표는 랜덤 (50 ~ 429중)
        badtimer = 100 - (badtimer1 * 2)
        if badtimer1 >= 35:
            badtimer1 = 35
        else:
            badtimer1 += 5

    index = 0
    for badguy in badguys:
        if badguy[0] <- 64:    # badguy[0] = 640
            badguys.pop(index)    # 없애기
        else:
            badguy[0] -= 7    # 왼쪽으로 점점 이동

        # 6-3-1. Attack castle
        badrect = pygame.Rect(badguyimg.get_rect())    # Rect 는 객체의 사각형 정보를 가져옴
        badrect.top = badguy[1]    # y좌표값
        badrect.left = badguy[0]   # x좌표값
        if badrect.left < 64:    # castle 4개에 도착하면
            hit.play()   # hit 이라는 효과음 플레이
            healthvalue -= random.randint(5, 20)
            badguys.pop(index)

        # 6-3-2. Check for collisions
        index1 = 0
        for bullet in arrows:
            bullrect = pygame.Rect(arrow.get_rect())
            bullrect.left = bullet[1]
            bullrect.top = bullet[2]
            if badrect.colliderect(bullrect):    # colliderect 서로 사각형으로 충돌했는지 (badrect와 bullrect)
                enemy.play()
                acc[0] += 1   # 맞은 누적 개수
                badguys.pop(index)    # badguy를 없앤다
                arrows.pop(index1)    # arrow를 없앤다
            index1 += 1

        index += 1
    for badguy in badguys:
        screen.blit(badguyimg, badguy)

    # 6-4. Draw clock
    font = pygame.font.Font(None, 24)    # None은 기본 폰트
    survivedtext = font.render(str(int((90000 - pygame.time.get_ticks()) / 60000)) +":"\    # 90000은 90초
        +str(int((90000 - pygame.time.get_ticks()) / 1000 % 60)).zfill(2), True, (0, 0, 0))    # 1000 나눠서 초 단위로 만들고 60으로 나눈 나머지
    textRect = survivedtext.get_rect()
    textRect.topright = [635, 5]    # 오른쪽 상단에 위치
    screen.blit(survivedtext, textRect)

    # 6-5. Draw health bar
    screen.blit(healthbar, (5, 5))    # (5, 5)가 위치 좌표
    for health1 in range(healthvalue):
        screen.blit(health, (health1 + 8, 8))


    # 7. 화면 다시 그리기
    pygame.display.flip()    # flip 은 화면 전체 업데이트 메소드

    # 8. 게임 종료
    for event in pygame.event.get():    # pygame에서 어떤 event 얻어 오기
        # 창x표시가 눌리면 게임 종료
        if event.type == pygame.QUIT:
            # 게임 종료
            pygame.quit()
            exit(0)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:    # w 라는 키보드가 눌리면
                keys[0] = True
            elif event.key == pygame.K_a:
                keys[1] = True
            elif event.key == pygame.K_s:
                keys[2] = True
            elif event.key == pygame.K_d:
                keys[3] = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:    # w 라는 키보드가 떼지면
                keys[0] = False
            elif event.key == pygame.K_a:
                keys[1] = False
            elif event.key == pygame.K_s:
                keys[2] = False
            elif event.key == pygame.K_d:
                keys[3] = False

        if event.type == pygame.MOUSEBUTTONDOWN:    # 마우스가 눌릴 때
            shoot.play()
            position = pygame.mouse.get_pos()    # 마우스의 현재 위치값 찾아서 position이라는 변수에 저장
            acc[1] = accp[1] + 1    # 모든 화살이 발사된 갯수
            arrows.append([math.atan2(position[1] - (playpos[1] + 32), \
                position[0] - (playpos[0]+26)), playerpos1[0] + 32, \
                playerpos1[1] + 32])

# math.atan2(position[1] - (playpos[1] + 32), position[0] - (playpos[0]+26))    # 32, 26은 그림 크기의 x, y 각각의 절반
# playerpos1[0] + 32,    # [0]은 x좌표, 32를 더해서 대략 가운데 값이 되게 만듬
# playerpos1[1] + 32     # [1]은 y좌표



    # 9. Move player (True일 때 작동)
    if keys[0]:
        playpos[1] = playpos [1] - 5    # 위로
    elif keys[2]:
        playpos[1] = playpos [1] + 5    # 아래로
    elif keys[1]:
        playpos[0] = playpos [0] - 5    # 왼쪽으로
    elif keys[3]:
        playpos[0] = playpos [0] + 5    # 오른쪽으로

     #10 - Win/Lose 검사
    if pygame.time.get_ticks() >= 90000:
        running = 0
        exitcode = 1
    if healthvalue <= 0:
        running = 0
        exitcode = 0
    if acc[1] != 0:    # acc[1]은 전체 화살의 갯수
        accuracy = acc[0]*1.0/acc[1]*100    # acc[0] 은 화살과 적이 맞은 횟수
    else:
        accuracy = 0

# 11 - Win/lose 디스플레이
if exitcode == 0:    # 패배 (LOSE)
    pygame.font.init()    # 폰트 초기화
    font = pygame.font.Font(None, 24)
    text = font.render("Accuracy: "+"{0:.2f}".format(accuracy)+"%", True, (255,0,0))
    textRect = text.get_rect()
    textRect.centerx = screen.get_rect().centerx
    textRect.centery = screen.get_rect().centery+24
    screen.blit(gameover, (0,0))
    screen.blit(text, textRect)

else:    # 게임승리 (WIN)
    pygame.font.init()
    font = pygame.font.Font(None, 24)
    text = font.render("Accuracy: "+"{0:.2f}".format(accuracy)+"%", True, (0,255,0))
    textRect = text.get_rect()
    textRect.centerx = screen.get_rect().centerx
    textRect.centery = screen.get_rect().centery+24
    screen.blit(youwin, (0,0))
    screen.blit(text, textRect)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
    pygame.display.flip()