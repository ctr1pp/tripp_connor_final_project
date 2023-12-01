# this file was created by: Connor Tripp

# Goals- Use arrow keys to rotate and place blocks along the screen; score points by clearing full, complete lines of blocks
# Rules- Use arrow keys to rotate and place blocks along the screen 
# Feautre Goals- display a grid like background; display blocks one at a time until they reach the bottom; display a score; display the next pice in the sequence

from settings import *
from sprites import Tetris
import sys


class App:
    def __init__(self):
        pg.init()
        pg.display.set_caption('Tetris')
        self.screen = pg.display.set_mode(FIELD_RES)       
        self.clock = pg.time.Clock()
        self.sprites = Tetris(self)

    def update(self):
        self.sprites.update()
        self.clock.tick(FPS)

    def draw(self):
        self.screen.fill(color=FIELD_COLOR)
        self.sprites.draw()
        pg.display.flip()

    def check_events(self):
        self.anim_trigger = False
        self.fast_anim_trigger = False
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit() 

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()

if __name__ == '__main__':
    app = App()
    app.run()