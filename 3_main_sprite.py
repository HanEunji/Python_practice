import pygame

pygame.init() # 초기화 (반드시 필요)

# 게임 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
pygame.display.set_mode((screen_width, screen_height))
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Game Create") # 게임 이름

# 배경 이미지 불러오기
background = pygame.image.load("C:/Workspace/Python-play-2021.11-/background.png")

# 스프라이트(캐릭터) 불러오기
character = pygame.image.load("C:/Workspace/Python-play-2021.11-/charactor.png")
character_size = character.get_rect().size # 이미지 크기를 구함
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2) # 캐릭터의 x 좌표
character_y_pos = screen_height - character_height # 캐릭터의 y 좌표

# 이벤트 루프
running = True # 게임이 진행중인가?
while running:
    for event in pygame.event.get(): # 어떤 이벤트가 발행하였는지
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임이 진행 중이 아님
            
    screen.blit(background, (0, 0)) # 배경 그리기
    # screen.fill((0, 0, 255)) # 배경을 RGB 값으로 채워주는 코드

    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update() # 게임화면을 계속 다시 그려줌
    

# pygame 종료
pygame.quit()