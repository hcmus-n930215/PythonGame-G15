import pygame
pygame.init()

infor_display = pygame.display.Info()
screen_size = (infor_display.current_w, infor_display.current_h)
game_width = int(screen_size[0]/2)
game_height = int(screen_size[1]/2)
screen = pygame.display.set_mode((game_width,game_height))
pygame.display.set_caption('Duongdua')
way = pygame.image.load("way.png")
way = pygame.transform.scale(way, (200,150))
turtle = pygame.image.load("Rua1.png")
turtle = pygame.transform.scale(turtle, (90,80))
grass = pygame.image.load("Co.png")
grass = pygame.transform.scale(grass,(80,80))
stone = pygame.image.load("Da.png")
stone = pygame.transform.scale(stone, (100,100))
tree = pygame.image.load("Cay.png")
tree = pygame.transform.scale(tree, (100,100))
square = pygame.image.load("Vach.png")
square = pygame.transform.scale(square,(200,200))
plant = pygame.image.load("XRong1.png")
plant = pygame.transform.scale(plant, (200,100))
clock = pygame.time.Clock()
def Begin(x):
    for i in range(0,9):
        screen.blit(square, (50+x, i*40+100))
def End(x):
    for i in range(0,9):
        screen.blit(square, (2000+x, i*40+100))
def Ways(x):
    for i in range(0,50):
        for j in range (0,7):
            screen.blit(way , (i*60+x,j*50+100))

def Grass(x):
    for i in range(0,100):
        for j in range (-1,3):
            screen.blit(grass, (i*40+x,j*40))
def Stone(x):
    for i in range(0,100):
        screen.blit(stone, (i*100+x,450))
def Tree(x):
    for i in range(0,100):
        screen.blit(tree, (i*100+x, 30))
def Turtle (x, y):
    screen.blit(turtle, (x,y))
def Plant (x, y):
    screen.blit(plant, (x,y))
def game_loop():
    gameover = False
    x = 0
    y = 0
    k = 0
    while not gameover:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameover = True
        Grass(x)
        Tree(x)
        x += -5
        y += +3
        if abs(x) >= 1300:
            gameover = True
        Ways(x-50)
        Stone(x)
        Begin(x)
        End(x)
        #Turtle(y,150)
        k = k + 1
        Plant(y,120+2*(-1)**k)
        pygame.display.update()
        clock.tick(30)

pygame.display.update()
game_loop()
pygame.quit()
quit()
