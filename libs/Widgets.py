from colormap.colors import hex2rgb
import pygame

class Button(pygame.sprite.Sprite):
    def __init__(self, startX, startY, width, height, text="Button", inUse = False) -> None:
        super().__init__()
        self.startX = startX
        self.startY = startY
        self.width = width
        self.height = height
        self.text = text
        self.inUse = inUse
        self.rect = pygame.Rect(self.startX, self.startY, self.width, self.height)
        self.rect.normalize()
        self.surface = None
        self.bk_surf = self.surface


    def show(self):
        showText(self.startX, self.startY, self.width, self.height, self.text, color="#B33333", bgrColor="#131313")
    def hide(self):
        showText(self.startX, self.startY, self.width, self.height, self.text, color="#FFFFFF")
    def setText(self, text):
        self.text = text
        showText(self.startX, self.startY, self.width, self.height, self.text, color="#B33333", bgrColor="#131313")
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
    def __init__(self, startX, startY, width, height, text="TextView", inUse = False) -> None:
        self.startX = startX
        self.startY = startY
        self.width = width
        self.height = height
        self.text = text
        self.inUse = inUse
        self.rect = pygame.Rect(self.startX, self.startY, self.width, self.height)

        super().__init__()
    def show(self):
        showText(self.startX, self.startY, self.width, self.height, self.text, color="#B33333", bgrColor="#131313")
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


def showText( x, y, width, height, text="TextView", font="freesansbold.ttf", color="#FFFFFF", textSize=20, bgrColor=None):
    font = pygame.font.SysFont('Comic Sans MS', textSize)
    if bgrColor!=None:
        text = font.render(text, True, hex2rgb(color, normalise=False), hex2rgb(bgrColor, normalise=False))
    else:
        text = font.render(text, True, hex2rgb(color, normalise=False), bgrColor)

    # create a rectangular object for the
    # text surface object
    textRect = text.get_rect()

    # set the center of the rectangular object.
    #textRect.center = (x+width // 2, y+height // 2)
    textRect.left = x
    textRect.top = y
    screen = pygame.display.get_surface()


    screen.blit(text, textRect)
