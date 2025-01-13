# Example file showing a basic pygame "game loop"
import pygame
import random

# pygame setup
pygame.init()
# pygame.quit()
screen_width = 400
screen_height = 400
game_screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Patrick's Snake Game")
clock = pygame.time.Clock()
running = True

x, y = 200, 200
delta_x, delta_y = 10, 0

food_x, food_y = random.randrange(0, screen_width)//10*10, random.randrange(0, screen_height)//10*10 # The random snake food that will randomly appear on screen 

body_list = [(x, y)]

clock = pygame.time.Clock()

font = pygame.font.SysFont("bahnschrift", 25)

game_over = False

def snake():
    global x, y, food_x, food_y, game_over
    x = (x + delta_x)%screen_width
    y = (y + delta_y)%screen_height

    if (x,y) in body_list: # if the head of the snack or body of the snack touches each other then game over
        game_over = True
        return

    body_list.append((x,y))

    if food_x == x and food_y == y: # when the head of the snake 
        while((food_x, food_y) in body_list):
            food_x, food_y = random.randrange(0,screen_width)//10*10, random.randrange(0, screen_height)//10*10
    else:
        del body_list[0]
               

    game_screen.fill((0,0,0))
    score = font.render('Score: ' + str(len(body_list)), True, (255, 255, 255))
    game_screen.blit(score, [0,0])
    pygame.draw.rect(game_screen, (225, 0,0), [food_x, food_y, 10, 10])
    for (i,j) in body_list:
        pygame.draw.rect(game_screen, (255, 255, 255), [i,j,10,10])
    pygame.display.update()


while running:
    if(game_over):
        game_screen.fill((0,0,0))
        score = font.render('Score: ' + str(len(body_list)), True, (255, 255, 255))
        game_screen.blit(score, [0,0])
        message = font.render('..YOU SUCK..GAME OVER!', True, (255, 255, 255))
        game_screen.blit(message, [screen_width//3, screen_height//3])
        pygame.display.update()
        pygame.time.delay(9000)  # Delay for 5000 milliseconds (5 seconds) before quitting
        pygame.quit()
        quit()
    events = pygame.event.get()
    for event in events:
        if (event.type == pygame.QUIT):
            pygame.quit()
            quit()
        if (event.type == pygame.KEYDOWN):
            if (event.key == pygame.K_LEFT):
                if delta_x != 10:
                    delta_x = -10
                delta_y = 0
            elif(event.key == pygame.K_RIGHT):
                if delta_x != -10:
                    delta_x = 10
                delta_y = 0
            elif(event.key == pygame.K_UP):
                delta_x = 0
                if delta_y != 10:
                    delta_y = -10
            elif(event.key == pygame.K_DOWN):
                delta_x = 0
                if delta_y != -10:
                    delta_y = 10
            else:
                continue
            snake()
    if not events:
        snake()
        clock.tick(10) #Frame rate