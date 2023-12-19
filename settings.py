import pygame as pg

vec = pg.math.Vector2

FPS = 60
# sets the color for the tetris game
FIELD_COLOR = (48, 39, 32)
# sets the color for the side screen which displays the next block and score 
BG_COLOR = (24, 89, 117)

# the time in between when tetrominoes are dropped 
ANIM_TIME_INTERVAL = 150 # milliseconds 
# the speed at which the block will fall if the user is pressing the down arrow 
FAST_ANIM_TIME_INTERVAL = 15

# the size of each tile drawn on the grid 
TILE_SIZE = 50
# the total amount of blocks within the grid 
FIELD_SIZE = FIELD_W, FIELD_H = 10, 17
FIELD_RES = FIELD_W * TILE_SIZE, FIELD_H * TILE_SIZE

# the dimensions for the side screen on the game 
FIELD_SCALE_W, FIELD_SCALE_H = 1.7, 1.0
WIN_RES = WIN_W, WIN_H = FIELD_RES[0] * FIELD_SCALE_W, FIELD_RES[1] * FIELD_SCALE_H

INIT_POS_OFFSET = vec(FIELD_W // 2 - 1, 0)
# tells the position of where the next tetromino is displayed 
NEXT_POS_OFFSET = vec(FIELD_W * 1.3, FIELD_H * 0.45)
# tells the computer where to move the blocks when different keys are pressed
MOVE_DIRECTIONS = {'left': vec(-1, 0), 'right': vec(1, 0), 'down': vec(0,1)}

# these are the tetrominoes that are drawn on the screen; each letter corisponds to the shape at which it resembles 
TETROMINOES = {
    'T': [(0,0), (-1,0), (1,0), (0,-1)],
    'O': [(0,0), (0,-1), (1,0), (1,-1)],
    'J': [(0,0), (-1,0), (0,-1), (0,-2)],
    'L': [(0,0), (1,0), (0,-1), (0,-2)],
    'I': [(0,0), (0,1), (0,-1), (0,-2)],
    'S': [(0,0), (-1,0), (0,-1), (1,-1)],
    'Z': [(0,0), (1,0), (0,-1), (-1,-1)],
    'I': [(0,0), (1,0), (2,0), (-1,0), (-2,0)],
    'U': [(0,0), (1,0), (2,0), (-1,0), (-2,0), (2, 1), (2,2), (-2,1), (-2,2)]
}
