from colormap.colors import hex2rgb
from libs.global_variables import *
import pygame

class Button(pygame.sprite.Sprite):
    def __init__(self, startX, startY, width, height, text="Button",color="#B33333", bgrColor="#FFFFFF") -> None:
        super().__init__()
        self.startX = startX
        self.startY = startY
        self.width = width
        self.height = height
        self.text = text
        self.bgrColor = bgrColor
        self.rect = pygame.Rect(self.startX, self.startY, self.width, self.height)
        self.rect.normalize()
        self.surface = None
        self.bk_surf = self.surface
        self.isTransparent = True
        self.color = color


    def show(self):
        showText(self.startX, self.startY, self.width, self.height, self.text, color=self.color,isTransparent=self.isTransparent)
    def setText(self, text):
        self.text = text
        self.show()
    def is_clicked(self):

        return pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos())
    def setSurface(self, parentSurface):

        self.surface = parentSurface.subsurface(self.rect)
        self.bk_surf = self.surface.copy()
        return self.surface
    def stop(self):
        #pygame.event.post(pygame.event.Event(pygame.USEREVENT, surface=self.bk_surf, pos=mpos))
        self.surface.blit(self.bk_surf, (0, 0))
    def getSurface(self):
        return self.surface
    pass

class TextView():
    def __init__(self, startX, startY, width, height, text="TextView", inUse = False, color="#B33333") -> None:
        self.startX = startX
        self.startY = startY
        self.width = width
        self.height = height
        self.text = text
        self.color = color
        self.inUse = inUse
        self.rect = pygame.Rect(self.startX, self.startY, self.width, self.height)

        super().__init__()
    def show(self):
        showText(self.startX, self.startY, self.width, self.height, self.text, color=self.color, bgrColor="#131313")
    def hide(self):
        showText(self.startX, self.startY, self.width, self.height, self.text, color="#FFFFFF")
    def setText(self, text=""):
        self.text = text
        showText(self.startX, self.startY, self.width, self.height, self.text, color="#B33333", bgrColor="#131313")
    def is_clicked(self):

        return pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos())
    def setSurface(self, parentSurface):
        self.surface = parentSurface.subsurface()
        return self.surface
    pass

class EditText():
    def __init__(self, startX, startY, width, height, text="EditText") -> None:
        self.startX = startX
        self.startY = startY
        self.width = width
        self.height = height
        self.text = text
        self.rect = pygame.Rect(self.startX, self.startY, self.width, self.height)

        super().__init__()

    def show(self):
        showText(self.startX, self.startY, self.width, self.height, self.text, color="#B33333", bgrColor="#131313")
    def hide(self):
        showText(self.startX, self.startY, self.width, self.height, self.text, color="#FFFFFF")

    def is_clicked(self):
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
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    if self.isPassword:
                        print(self.hidetext)
                    else:
                        print(self.text)
                    #self.text = ''
                elif event.key == pygame.K_BACKSPACE:

                    self.text = self.text[:-1]
                    if self.isPassword:
                        self.hidetext = self.hidetext[:-1]
                else:

                    buffer = "" + str(event.unicode)
                    if self.isDigit and not buffer.isdigit():
                        buffer = ""
                    if self.isPassword:
                        self.hidetext += buffer
                        if len(self.hidetext) > len(self.text):
                            self.text += "*"
                    else:
                        self.text += buffer
                # Re-render the text.
                self.txt_surface = self.FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
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
        # Blit the image.
        screen.blit(self.IMAGE, (self.x, self.y))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)








def showText( x, y, width, height, text="TextView", font="freesansbold.ttf", color="#FFFFFF", textSize=20, bgrColor=None,isTransparent=True):
    font = pygame.font.SysFont('Comic Sans MS', textSize)
    if isTransparent:
        text = font.render(text, True, hex2rgb(color, normalise=False))

    elif bgrColor!=None:
        text = font.render(text, True, hex2rgb(color, normalise=False), hex2rgb(bgrColor, normalise=False))
    else:
        text = font.render(text, True, hex2rgb(color, normalise=False), bgrColor)

    # create a rectangular object for the
    # text surface object
    textRect = text.get_rect()

    # set the center of the rectangular object.
    #textRect.center = (x+width // 2, y+height // 2)
    textRect.left = (x)
    #textRect.centery = y + height//2
    #textRect = (x,y)
    textRect.centery = y + height//2
    screen = pygame.display.get_surface()


    screen.blit(text, textRect)



