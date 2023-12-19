# this file was created by: Connor Tripp
# content from youtube: https://www.youtube.com/watch?v=RxWS5h1UfI4

# Goals- Use arrow keys to rotate and place blocks along the screen; score points by clearing full, complete lines of blocks
# Rules- Use arrow keys to rotate and place blocks along the screen 
# Feautre Goals- display a grid like background; display blocks one at a time until they reach the bottom; display a score; display the next pice in the sequence

from settings import *
from tetris import Tetris
import sys


class App:
    def __init__(self):
        # initialize pygame and set up the game window 
        pg.init()
        pg.display.set_caption('Tetris')
        # creats the game window with the resolution 
        self.screen = pg.display.set_mode(WIN_RES) \
        # the clock controls the frame rate       
        self.clock = pg.time.Clock()
        self.set_timer ()
        # creates and instance of tetris class 
        self.tetris = Tetris(self)
        # adds a score system to the game 
        self.score = 0 

    # tells computer when to update score 
    def update_score(self, lines_cleared, move_down_points): 
        if lines_cleared == 1: 
            self.score += 100
        elif lines_cleared == 2: 
            self.score += 300 
        elif lines_cleared == 3: 
            self.score += 500
        self.score += move_down_points
    
    def set_timer(self):
        # sets up different events for different animations that could happen  
        # checks regular animation updates 
        self.user_event = pg.USEREVENT + 0 
        # checks fast animation updates 
        self.fast_user_event = pg.USEREVENT + 1
        self.anim_trigger = False
        self.fast_anim_trigger = False
        # sets the timers for the animations 
        pg.time.set_timer(self.user_event, ANIM_TIME_INTERVAL)
        pg.time.set_timer(self.fast_user_event, FAST_ANIM_TIME_INTERVAL)

    def update(self):
        # calls on the tetris update method 
        self.tetris.update()
        self.clock.tick(FPS)

    def draw(self):
        # fills in the color of the side screen 
        self.screen.fill(color=BG_COLOR)
        # draws the score on the screen 
        self.score.draw()
        # fills in the color of the main game with the grid on it 
        self.screen.fill(color = FIELD_COLOR, rect = (0, 0, *FIELD_RES))
        self.tetris.draw()
        pg.display.flip()

    # checks for uder inputs 
    def check_events(self): 
        self.anim_trigger = False
        self.fast_anim_trigger = False
        # checks for all the events that could happen 
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                # quits the game 
                pg.quit()
                sys.exit() 
            elif event.type == pg.KEYDOWN: 
                # this is what handles the controls to the game 
                self.tetris.control(pressed_key = event.key)
            elif event.type == self.user_event: 
                # animation trigger for regular updates 
                self.anim_trigger = True
            elif event.type == self.fast_user_event: 
                # animation trigger for fast updates 
                self.fast_anim_trigger = True 

    # this is the main game loop 
    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()

# runs the code if the user is in the main.py file and presses play 
if __name__ == '__main__':
    app = App()
    app.run()