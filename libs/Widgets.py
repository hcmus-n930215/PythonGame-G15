from colormap.colors import hex2rgb
import pygame

class Button(pygame.sprite.Sprite):
    def __init__(self, startX, startY, width, height, text="Button", bgrColor="#FFFFFF") -> None:
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


    def show(self):
        showText(self.startX, self.startY, self.width, self.height, self.text, color="#B33333", bgrColor=self.bgrColor)
    def hide(self):
        showText(self.startX, self.startY, self.width, self.height, self.text, color="#FFFFFF")
    def setText(self, text):
        self.text = text
        showText(self.startX, self.startY, self.width, self.height, self.text, color="#B33333", bgrColor=self.bgrColor)
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

COLOR_INACTIVE = pygame.Color('lightskyblue3')
COLOR_ACTIVE = pygame.Color('dodgerblue2')

class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.FONT = pygame.font.SysFont('Comic Sans MS', 30)
        self.txt_surface = self.FONT.render(text, True, self.color)
        self.active = False
        self.hidetext = text
        self.isPassword = False

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


                    if self.isPassword:
                        self.hidetext += event.unicode
                        self.text += "*"
                    else:
                        self.text += event.unicode
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
    textRect.center = (x+width // 2, y+height // 2)
    screen = pygame.display.get_surface()


    screen.blit(text, textRect)
