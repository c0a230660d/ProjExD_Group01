import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))

#リセット画面
class Resetout(pg.sprite.Sprite):
    """
    リセット画面に関するクラス
    """
    def __init__(self,screen):
        super().__init__()
        screen = pg.display.set_mode((600, 600))
        self.image = pg.image.load("fig/maguma.jpg")
        self.rect = self.image.get_rect()
        self.rect.center = 100, 100
        
        pg.display.update()
        
        
        
        
        
    

def main():
    pg.display.set_caption("はじめてのPygame")
    screen = pg.display.set_mode((600, 900))
    clock = pg.time.Clock()
    font = pg.font.Font(None, 80)
    resets = pg.sprite.Group()
    resets.add(Resetout(screen))

    enn = pg.Surface((20, 20))
    pg.draw.circle(enn, (255, 0, 0), (10, 10), 10)
    enn.set_colorkey((0, 0, 0))

    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        
        txt = font.render(str(tmr), True, (255, 255, 255))
        screen.fill((50, 50, 50))
        screen.blit(txt, [300, 200])
        screen.blit(enn, [100, 400])
        resets.update()
        resets.draw(screen)
        pg.display.update()
        tmr += 1        
        clock.tick(1)
        
    


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()