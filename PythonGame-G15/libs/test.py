import pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))

clock = pygame.time.Clock()
for x in range(0, 800):
    pygame.draw.rect(screen, ((x+100)%255, (x*2)%255, x%255), pygame.Rect(x, 0, 1, 800))

org_screen = screen.copy()

class Cursor(object):
    def __init__(self):
        self._inner = CopyCursor()

    def mousedown(self, mpos):
        self._inner = self._inner.mousedown(mpos)

    def mouseup(self, mpos):
        self._inner = self._inner.mouseup(mpos)

    def draw(self, screen, mpos):
        self._inner.draw(screen, mpos)

class CopyCursor(object):
    def __init__(self):
        self.start, self.end = None, None

    def mousedown(self, mpos):
        self.start = mpos
        return self

    def mouseup(self, mpos):
        if self.start and self.end:
            r = pygame.Rect(self.start, self.end)
            r.normalize()
            # important to call .copy() so 'sub_surf'
            # loses its relation to 'screen'
            return BlitCursor(screen.subsurface(r).copy())
        return self

    def draw(self, screen, mpos):
        if self.start:
            self.end = mpos[0]-self.start[0], mpos[1]-self.start[1]
            rect = pygame.Rect(self.start, self.end)
            pygame.draw.rect(screen, pygame.Color('grey'), rect, 3)

class BlitCursor(object):
    def __init__(self, sub_surf):
        self.sub_surf = sub_surf

    def mousedown(self, mpos):
        pygame.event.post(pygame.event.Event(pygame.USEREVENT, surface=self.sub_surf, pos=mpos))
        return CopyCursor()

    def mouseup(self, mpos):
        pass

    def draw(self, screen, mpos):
        screen.blit(self.sub_surf, mpos)

cursor = Cursor()
while True:
    mpos = pygame.mouse.get_pos()
    for e in pygame.event.get():
        if e.type == pygame.QUIT: break
        if e.type == pygame.MOUSEBUTTONUP: cursor.mouseup(mpos)
        if e.type == pygame.MOUSEBUTTONDOWN: cursor.mousedown(mpos)
        if e.type == pygame.USEREVENT:
            org_screen.blit(e.surface, e.pos)
            screen.blit(org_screen, (0, 0))
    else:
        if not pygame.event.peek(pygame.USEREVENT):
            cursor.draw(screen, mpos)
            pygame.display.flip()
            screen.blit(org_screen, (0, 0))
        clock.tick(50)
        continue
    break