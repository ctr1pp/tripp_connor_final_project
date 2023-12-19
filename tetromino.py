from settings import *
import random
 
class Block(pg.sprite.Sprite):
    def __init__(self, tetromino, pos): 
        # initialize the block with it's cooresponding tetromino and position 
        self.tetromino = tetromino
        self.pos = vec(pos) + INIT_POS_OFFSET
        self.next_pos = vec(pos) + NEXT_POS_OFFSET
        self.alive = True

        super().__init__(tetromino.tetris.sprite_group)
         # this is what the tetrominoes will look like (color, shape, size)
        self.image = tetromino.image
        self.rect = self.image.get_rect()
    
    # method that checks if the block is alive 
    def is_alive(self): 
        if not self.alive: 
            # removes the block from the sprite group if it is not alive 
            self.kill()

    # rotates the block when player calls upon to do so 
    def rotate(self, pivot_pos): 
        translated = self.pos - pivot_pos
        # rotated 90 degrees 
        rotated = translated.rotate(90)
        return rotated + pivot_pos
        
    def set_rect_pos(self): 
        # determines position of termromino based on if it's next up for the current one 
        pos = [self.next_pos, self.pos][self.tetromino.current]
        self.rect.topleft = pos * TILE_SIZE

    # method that checks if the block is alive and sets the postion if it is 
    def update(self): 
        self.is_alive()
        self.set_rect_pos()

    # checks if the tetrominoes have collides with each other, so that they will not go inside one another 
    def is_collide(self, pos): 
        x, y = int(pos.x), int(pos.y)
        if 0 <= x < FIELD_W and y < FIELD_H and (
                y < 0 or not self.tetromino.tetris.field_array[y][x]): 
            return False
        return True 

# the class of tetrominoes 
class Tetromino:
    def __init__(self, tetris, current = True): 
        self.tetris = tetris
        # gives you a random tetromino that will appear once the previous one has been placed 
        self.shape = random.choice(list(TETROMINOES.keys()))
        self.image = random.choice(tetris.app.images )
        # creates the block for the tetromino that is chosen 
        self.blocks = [Block(self, pos) for pos in TETROMINOES[self.shape]]
        self.landing = False
        self.current = current

    def rotate(self): 
        pivot_pos = self.blocks[0].pos 
        # calculates the new block position once it has been rotated 
        new_block_positions = [block.rotate(pivot_pos) for block in self.blocks]

        # makes sure that there is not a collision once the rotation has happenend 
        if not self.is_collide(new_block_positions): 
            for i, block in enumerate(self.blocks): 
                block.pos = new_block_positions[i]

    # checks if the postions of the blocks have collided 
    def is_collide(self, block_positions): 
        return any(map(Block.is_collide, self.blocks, block_positions))

    # moves the blocks in the positions of which the user calls on them to be moved 
    def move(self, direction): 
        # left, right, down, up (rotate)
        move_direction = MOVE_DIRECTIONS[direction]
        # gives the new positon based on what the user chose to do 
        new_block_positions = [block.pos + move_direction for block in self.blocks]
        # checks to see if the blocks have collided 
        is_collide = self.is_collide(new_block_positions)

        # if they have no collided the player can continue to keep moving them 
        if not is_collide: 
            for block in self.blocks: 
                block.pos += move_direction
        elif direction == 'down': 
            self.landing = True 
    def update(self): 
        self.move(direction = 'down')
    