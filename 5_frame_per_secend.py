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
background = pygame.image.load("D:/HanEunji/Documents/project/PythonWorkspace/20211121 shootinggame/background.png")

# 스프라이트(캐릭터) 불러오기
character = pygame.image.load("D:/HanEunji/Documents/project/PythonWorkspace/20211121 shootinggame/charactor.png")
character_size = character.get_rect().size # 이미지 크기를 구함
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2) # 캐릭터의 x 좌표
character_y_pos = screen_height - character_height # 캐릭터의 y 좌표

# 이동할 좌표
to_x = 0
to_y = 0

# 이벤트 루프
running = True # 게임이 진행중인가?
while running:
    dt = clock.tick()
    for event in pygame.event.get(): # 어떤 이벤트가 발행하였는지
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임이 진행 중이 아님
            
        if event.type == pygame.KEYDOWN: # 키 입력 확인
            if event.key == pygame.K_LEFT:
                to_x -= 5
            elif event.key == pygame.K_RIGHT:
                to_x += 5
            elif event.key == pygame.K_UP:
                to_y -= 5
            elif event.key == pygame.K_DOWN:
                to_y += 5

        if event.type == pygame.KEYUP: # 방향키를 떼면 멈추도록
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_x = 0

    character_x_pos += to_x
    character_y_pos += to_y

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

        
    screen.blit(background, (0, 0)) # 배경 그리기
    # screen.fill((0, 0, 255)) # 배경을 RGB 값으로 채워주는 코드

    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update() # 게임화면을 계속 다시 그려줌
    

# pygame 종료
pygame.quit()