from colormap.colors import hex2rgb
from libs.global_variables import *
import pygame

class View(pygame.sprite.Sprite):
    def __init__(self, startX, startY, text="View", color="#B33333", bgrColor="#FFFFFF", gravity="center") -> None:
        super().__init__()
        self.startX = startX
        self.startY = startY
        self.text = text
        self.bgrColor = bgrColor
        self.rect = pygame.Rect(self.startX, self.startY, 0, 0)
        self.rect.normalize()
        self.surface = None
        self.bk_surf = self.surface
        self.isTransparent = True
        self.color = color
        self.gravity = "top_left"
        self.setGravity(gravity)
        self.SCREEN = pygame.display.get_surface()
        self.bgrImg = None
    def setGravity(self, gravity):
        list_gravity  = ["top_left", "bottom_left", "center", "center_vertical", "center_horizontal", "top_right", "bottom_right",
                         "mid_bottom", "mid_left", "mid_right"]
        if gravity in list_gravity:
            self.gravity = gravity
    def show(self):
        if self.bgrImg != None:
            self.SCREEN.blit(self.bgrImg, (self.rect.x - 10, self.rect.y - 5))
        self.rect = showText(self.startX, self.startY, self.text, color=self.color, isTransparent=self.isTransparent, gravity=self.gravity)
    def setText(self, text):
        self.text = text
        self.show()
    def setBackground(self, gameLancher, img_link=None):
        if img_link != None:
            self.bgrImg = gameLancher.load_img(img_link, self.rect.w + 20, self.rect.h + 10)
        else:
            self.bgrImg = None
        self.show()
    def is_clicked(self, gameLancher):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.setBackground(gameLancher,"img/bg_button_isclicked.png")
        else:
            self.setBackground(gameLancher=gameLancher)
        return pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos())

    pass
COLOR_INACTIVE = pygame.Color('lightskyblue3')
COLOR_ACTIVE = pygame.Color('dodgerblue2')
class InputBox:
    def __init__(self, x, y, w, h, text='', isdigit=False, ispassword =False):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.FONT = pygame.font.SysFont('Comic Sans MS', 30)
        self.txt_surface = self.FONT.render(text, True, self.color)
        self.active = False
        self.hidetext = text
        self.isPassword = ispassword
        self.isDigit = isdigit

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.active = self.rect.collidepoint(event.pos)
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                    if self.isPassword:
                        self.hidetext = self.hidetext[:-1]
                    self.txt_surface = self.FONT.render(self.text, True, self.color)
                    return 1
                else:
                    if len(self.text) >= 10:
                        return 0
                    buffer = "" + str(event.unicode)
                    if self.isDigit and not buffer.isdigit():
                        buffer = ""
                    if self.isPassword:
                        self.hidetext += buffer
                        if len(self.hidetext) > len(self.text):
                            self.text += "*"
                    else:
                        self.text += buffer
                        self.txt_surface = self.FONT.render(self.text, True, self.color)
                        return 1
                self.txt_surface = self.FONT.render(self.text, True, self.color)
        return -1
    def draw(self, screen):
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        pygame.draw.rect(screen, self.color, self.rect, 2)

class ImageView():
    def __init__(self, game, x, y, w, h, img_link):
        self.x = x
        self.y = y
        self.color = COLOR_INACTIVE
        self.game = game
        self.IMAGE = self.game.load_img(img_link, w,h)
        self.rect = self.IMAGE.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.active = False
    def setActive(self,isActive=False):
        self.active = isActive
        self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
    def is_clicked(self):
        return pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos())
    def draw(self, screen):
        screen.blit(self.IMAGE, (self.x, self.y))
        pygame.draw.rect(screen, self.color, self.rect, 2)
    pass

def showText( x, y, text="View", font="freesansbold.ttf", color="#FFFFFF", textSize=20, bgrColor=None,isTransparent=True, gravity="top_left"):
    font = pygame.font.SysFont('Comic Sans MS', textSize)
    if isTransparent:
        text = font.render(text, True, hex2rgb(color, normalise=False))
    elif bgrColor!=None:
        text = font.render(text, True, hex2rgb(color, normalise=False), hex2rgb(bgrColor, normalise=False))
    else:
        text = font.render(text, True, hex2rgb(color, normalise=False), bgrColor)
    textRect = text.get_rect()
    '''
    $ checkout the gravity
    The Rect object has several virtual attributes which can be used to move and align the Rect:
    x,y
    top, left, bottom, right
    topleft, bottomleft, topright, bottomright
    midtop, midleft, midbottom, midright
    center, centerx, centery
    size, width, height
    w,h
    '''
    list_gravity = ["top_left", "bottom_left", "center", "center_vertical", "center_horizontal", "top_right",
                    "bottom_right", "mid_bottom", "mid_left", "mid_right"]
    if gravity == "top_left":
        textRect.topleft = (x, y)
    elif gravity == "bottom_left":
        textRect.bottomleft =(x,y)
    elif gravity =="center":
        textRect.center = (x,y)
    elif gravity =="center_vertical":
        textRect.centerx = x
        textRect.y = y
    elif gravity =="center_horizontal":
        textRect.centery = y
        textRect.x = x
    elif gravity =="top_right":
        textRect.topright = (x,y)
    elif gravity == "bottom_right":
        textRect.bottomright = (x, y)
    elif gravity == "mid_bottom":
        textRect.midbottom = (x,y)
    elif gravity == "mid_left":
        textRect.midleft = (x, y)
    elif gravity == "mid_right":
        textRect.midright = (x, y)
    else:
        # set default if error
        textRect.topleft = (x, y)

    screen = pygame.display.get_surface()
    screen.blit(text, textRect)
    return  textRect
