import pygame

pygame.init() # 초기화 (반드시 필요)

# 게임 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
pygame.display.set_mode((screen_width, screen_height))
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Game Create") # 게임 이름

# FPS
clock = pygame.time.Clock()

# 배경 이미지 불러오기
background = pygame.image.load("C:/Workspace/Python-play-2021.11-/background.png")

# 스프라이트(캐릭터) 불러오기
character = pygame.image.load("C:/Workspace/Python-play-2021.11-/charactor.png")
character_size = character.get_rect().size # 이미지 크기를 구함
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2) # 캐릭터의 x 좌표
character_y_pos = screen_height - character_height # 캐릭터의 y 좌표

# 이동할 좌표
to_x = 0
to_y = 0

# 이동 속도
character_speed = 0.6

# 적 캐릭터
enemy = pygame.image.load("C:/Workspace/Python-play-2021.11-/enemy.png")
enemy_size = enemy.get_rect().size # 이미지 크기를 구함
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = (screen_width / 2) - (enemy_width / 2) # 캐릭터의 x 좌표
enemy_y_pos = (screen_height / 2) - (enemy_height / 2) # 캐릭터의 y 좌표


# 폰트 정의가 선행되어야 함
game_font = pygame.font.Font(None, 40) #  None으로 쓰면 기본 폰트 출력

# 폰트로 총 게임 시간
total_time = 10

# 시간 계산
start_ticks = pygame.time.get_ticks() # 시작 tick을 받아옴


# 이벤트 루프
running = True # 게임이 진행중인가?
while running:
    dt = clock.tick(60) # 게임화면의 초당 프레임 수를 설정함

    print("fps : "+ str(clock.get_fps()))
    for event in pygame.event.get(): # 어떤 이벤트가 발행하였는지
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임이 진행 중이 아님
            
        if event.type == pygame.KEYDOWN: # 키 입력 확인
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed

        if event.type == pygame.KEYUP: # 방향키를 떼면 멈추도록
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x * dt # dt값을 곱하지 않으면 fps에 따라 캐릭터 이동 속도도 달라짐
    character_y_pos += to_y * dt

    # 가로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # 세로 경계값 처리
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    # 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos # 실제 캐릭터 위치대로 위치정보 바꿈

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos 

    # 충돌 체크
    if character_rect.colliderect(enemy_rect):
        print("충돌했어요!")
        running = False

        
    screen.blit(background, (0, 0)) # 배경 그리기
    # screen.fill((0, 0, 255)) # 배경을 RGB 값으로 채워주는 코드

    screen.blit(character, (character_x_pos, character_y_pos)) 

    screen.blit(enemy, (enemy_x_pos, enemy_y_pos)) # 적 그리기


    # 타이머 집어 넣기
    # 경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 # 경과 시간을 1000으로 나누어 초 단위로 표시. 나누지 않으면 ms

    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255, 255, 255))

    screen.blit(timer, (10, 10))

    # 시간이 0 이하면 게임 종료
    if total_time - elapsed_time <= 0:
        print("타임아웃")
        running = False



    pygame.display.update() # 게임화면을 계속 다시 그려줌
    

# 잠시 대기
pygame.time.delay(2000) # 게임 종료 전 2초 정도 대기


# pygame 종료
pygame.quit()