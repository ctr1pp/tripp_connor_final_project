from settings import * 
import math 
from tetromino import Tetromino

class Tetris: 
    def __init__(self, app): 
        self.app = app 

    # code that checks for a full line to clear
    def check_full_lines(self): 
        row = FIELD_H - 1
        for y in range(FIELD_H - 1, -1, -1): 
            # copies the content on the row that is above the full bottom row when it is cleared 
            for x in range(FIELD_W): 
                self.field_array[row][x] = self.field_array[y][x]
                
                if self.field_array[y][x]: 
                    self.field_array[row][x].pos = vec(x, y)
            # checks if the current row has spaces in the line (is it full basically)
            if sum(map(bool, self.field_array[y])) < FIELD_W: 
                row -= 1
            else: 
                # update the game if the row is full 
                for x in range(FIELD_W): 
                    self.field_array[row][x].alive = False
                    self.field_array[row][x] = 0 
                self.full_lines += 1

    def put_tetromino_blocks_in_array(self): 
        for block in self.tetromino.blocks: 
            # gets the coordinates of the current block's position 
            x, y = int(block.pos.x), int(block.pos.y)
            # places the block in it's coorisponding position 
            self.field_array[y][x] = block 

    def get_field_array(self): 
        return [[0 for x in range(FIELD_W)] for y in range(FIELD_H)]
    
    # checks to see if the game is over (are the blocks able to be placed on the screen anymore)
    def is_game_over(self): 
        if self.tetromino.blocks[0].pos.y == INIT_POS_OFFSET[1]: 
            # waits a second before telling that the game is over 
            pg.time.wait(300)
            return True 
    # checks to see where the tetromino has landed 
    def check_tetromino_landing(self): 
        if self.tetromino.landing:
            # checks to see if the game is over and it needs to restart
            if self.is_game_over(): 
                self.__init__(self.app)
            else:
                self.speed_up = False 
                self.put_tetromino_blocks_in_array()
                # puts the tetromino that was the next one as the current one 
                self.next_tetromino.current = True 
                self.tetromino = self.next_tetromino
                # puts a new next tetromino in place 
                self.next_tetromino = Tetromino(self, current = False)

    def control(self, pressed_key): 
        # if player presses the left key the tetromino will move left
        if pressed_key == pg.K_LEFT: 
            self.tetromino.move(direction = 'left')
        # if player presses the right key the tetromino will move right
        elif pressed_key == pg.K_RIGHT: 
            self.tetromino.move(direction = 'right')
        # if player presses the up key the tetromino will rotate 
        elif pressed_key == pg.K_UP: 
            self.tetromino.rotate()
        # if player presses the down key the tetromino will speed up 
        elif pressed_key == pg.K_DOWN: 
            self.speed_up = True 

    # draws the grid on the screen 
    def draw_grid(self):
        for x in range(FIELD_W): 
            for y in range (FIELD_H):
                pg.draw.rect(self.app.screen, 'black',
                            (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE), 1)
                
    def update(self): 
        trigger = [self.app.anim_trigger, self.app.fast_anim_trigger] # [self.speed_up]
        # checks if the animation trigger has occured 
        if trigger: 
            self.check_full_lines
            self.tetromino.update() 
            self.check_tetromino_landing()
        self.sprite_group.update()

    def draw(self): 
        self.draw_grid() 
        self.sprite_group.draw(self.app.screen)