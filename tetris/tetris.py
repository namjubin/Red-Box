import sys
import pygame
import random

pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 400, 600
GRID_SIZE = 25

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
COLORS = [RED, BLUE, GREEN]

# Tetromino shapes
SHAPES = [
    [
        ['.....',
         '.....',
         '.....',
         'OOOO.',
         '.....'],
        ['.....',
         '..O..',
         '..O..',
         '..O..',
         '..O..']
    ],
    [
        ['.....',
         '.....',
         '..O..',
         '.OOO.',
         '.....'],
        ['.....',
         '..O..',
         '..OO.',
         '..O..',
         '.....'],
        ['.....',
         '.....',
         '.OOO.',
         '..O..',
         '.....'],
        ['.....',
         '..O..',
         '.OO..',
         '..O..',
         '.....']
    ],
    [
        [
         '.....',
         '.....',
         '..OO.',
         '.OO..',
         '.....'],
        ['.....',
         '.O...',
         '.OO..',
         '..O..',
         '.....']
    ],
    [
        ['.....',
         '.....',
         '.OO..',
         '..OO.',
         '.....'],
        ['.....',
         '..O..',
         '.OO..',
         '.O...',
         '.....']
    ],
    [
        ['.....',
         '..O..',
         '..O..',
         '..OO.',
         '.....'],
        ['.....',
         '.....',
         '.OOO.',
         '.O...',
         '.....'],
        ['.....',
         '.OO..',
         '..O..',
         '..O..',
         '.....'],
        ['.....',
         '...O.',
         '.OOO.',
         '.....',
         '.....']
    ],
    [
        ['.....',
         '..O..',
         '..O..',
         '.OO..',
         '.....'],
        ['.....',
         '.O...',
         '.OOO.',
         '.....',
         '.....'],
        ['.....',
         '..OO.',
         '..O..',
         '..O..',
         '.....'],
        ['.....',
         '.....',
         '.OOO.',
         '...O.',
         '.....']
    ],
    [
        ['.....',
         '.....',
         '.OO..',
         '.OO..',
         '.....'],
    ],
]


class Tetromino:
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = random.choice(COLORS) # You can choose different colors for each shape
        self.rotation = 0


class Tetris:
    def __init__(self, screen):
        self.screen = screen
        self.surface = pygame.Surface((WIDTH, HEIGHT))
        self.width = WIDTH // GRID_SIZE
        self.height = HEIGHT // GRID_SIZE
        self.screen_size = pygame.display.get_surface().get_size()
        self.surface_size = ((self.screen_size[1]/HEIGHT)*self.surface.get_width(), self.screen_size[1])
        self.surface_loc = (self.screen_size[0]//2-self.surface_size[0]//2, 0)

        self.img1 = pygame.image.load('./tetris/img/tetris_1.png')
        self.img2 = pygame.image.load('./tetris/img/tetris_2.png')
        self.img1 = pygame.transform.scale(self.img1, ((self.screen_size[1]/self.img1.get_height())*self.img1.get_width(), self.screen_size[1]))
        self.img2 = pygame.transform.scale(self.img2, ((self.screen_size[1]/self.img2.get_height())*self.img2.get_width(), self.screen_size[1]))
        self.img1_loc = (self.surface_loc[0]-self.img1.get_width(), 0)
        self.img2_loc = (self.surface_loc[0]+self.surface_size[0], 0)

        self.setting()

    def setting(self):
        self.grid = [[0 for _ in range(self.width)] for _ in range(self.height)]
        self.current_piece = self.new_piece()
        self.game_over = False
        self.score = 0  # Add score attribute

    def new_piece(self):
        # Choose a random shape
        shape = random.choice(SHAPES)
        # Return a new Tetromino object
        return Tetromino(self.width // 2, 0, shape)

    # def valid_move(self, piece, x, y, rotation):
    #     """Check if the piece can move to the given position"""
    #     for i, row in enumerate(piece.shape[(piece.rotation + rotation) % len(piece.shape)]):
    #         for j, cell in enumerate(row):
    #             try:
    #                 if cell == 'O' and (self.grid[piece.y + i + y][piece.x + j + x] != 0):
    #                     return False
    #             except IndexError:
    #                 return False
    #     return True

    def valid_move(self, piece, x, y, rotation):
        """Check if the piece can move to the given position"""
        for i, row in enumerate(piece.shape[(piece.rotation + rotation) % len(piece.shape)]):
            for j, cell in enumerate(row):
                try:
                    if cell == 'O':
                        if (piece.x + j + x < 0) or (piece.x + j + x >= self.width):  # Check for wall collision
                            return False
                        if (piece.y + i + y >= self.height) or (self.grid[piece.y + i + y][piece.x + j + x] != 0):  # Check for block collision
                            return False
                except IndexError:
                    return False
        return True

    def clear_lines(self):
        """Clear the lines that are full and return the number of cleared lines"""
        lines_cleared = 0
        new_grid = []
        for row in self.grid:
            if all(cell != 0 for cell in row):
                lines_cleared += 1
            else:
                new_grid.append(row)
        while len(new_grid) < self.height:
            new_grid.insert(0, [0] * self.width)
        self.grid = new_grid
        return lines_cleared


    def lock_piece(self, piece):
        """Lock the piece in place and check for cleared lines"""
        for i, row in enumerate(piece.shape[piece.rotation % len(piece.shape)]):
            for j, cell in enumerate(row):
                if cell == 'O':
                    self.grid[piece.y + i][piece.x + j] = piece.color
        # Clear the lines and update the score
        lines_cleared = self.clear_lines()
        self.score += lines_cleared * 100  # Update the score based on the number of cleared lines
        # Create a new piece
        self.current_piece = self.new_piece()
        # Check if the game is over
        if not self.valid_move(self.current_piece, 0, 0, 0):
            self.game_over = True
        return lines_cleared

    def update(self):
        """Move the tetromino down one cell"""
        if not self.game_over:
            if self.valid_move(self.current_piece, 0, 1, 0):
                self.current_piece.y += 1
            else:
                self.lock_piece(self.current_piece)

    def draw(self):
        """Draw the grid and the current piece"""
        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(self.surface, cell, (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE - 1, GRID_SIZE - 1))

        if self.current_piece:
            for i, row in enumerate(self.current_piece.shape[self.current_piece.rotation % len(self.current_piece.shape)]):
                for j, cell in enumerate(row):
                    if cell == 'O':
                        pygame.draw.rect(self.surface, self.current_piece.color, ((self.current_piece.x + j) * GRID_SIZE, (self.current_piece.y + i) * GRID_SIZE, GRID_SIZE - 1, GRID_SIZE - 1))

    def show(self):
        # Create a clock object
        run = True
        clock = pygame.time.Clock()
        # Create a Tetris object
        fall_time = 0
        fall_speed = 10  # You can adjust this value to change the falling speed, it's in milliseconds
        while run:
            # Fill the screen with black
            self.surface.fill((BLACK))
            self.screen.fill((BLACK))
            for event in pygame.event.get():
                # Check for the QUIT event
                if event.type == pygame.QUIT:
                    run = False
                # Check for the KEYDOWN event
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        run = False
                    if self.game_over:
                        self.setting()
                    else:
                        if event.key == pygame.K_LEFT:
                            if self.valid_move(self.current_piece, -1, 0, 0):
                                self.current_piece.x -= 1  # Move the piece to the left
                        if event.key == pygame.K_RIGHT:
                            if self.valid_move(self.current_piece, 1, 0, 0):
                                self.current_piece.x += 1  # Move the piece to the right
                        if event.key == pygame.K_DOWN:
                            if self.valid_move(self.current_piece, 0, 1, 0):
                                self.current_piece.y += 1  # Move the piece down
                        if event.key == pygame.K_UP:
                            if self.valid_move(self.current_piece, 0, 0, 1):
                                self.current_piece.rotation += 1  # Rotate the piece
                        if event.key == pygame.K_SPACE:
                            while self.valid_move(self.current_piece, 0, 1, 0):
                                self.current_piece.y += 1  # Move the piece down until it hits the bottom
                            self.lock_piece(self.current_piece)  # Lock the piece in place
            # Get the number of milliseconds since the last frame
            delta_time = clock.get_rawtime() 
            # Add the delta time to the fall time
            fall_time += 1 
            if fall_time >= fall_speed:
                # Move the piece down
                self.update()
                # Reset the fall time
                fall_time = 0
            # Draw the score on the screen
            draw_score(self.surface, self.score, 10, 10)
            # Draw the grid and the current piece
            self.draw()
            if self.game_over:
                # Draw the "Game Over" message
                draw_game_over(self.surface, WIDTH // 2 - 100, HEIGHT // 2 - 30)
            
            self.screen.blit(self.img1, self.img1_loc)
            self.screen.blit(self.img2, self.img2_loc)
            self.screen.blit(pygame.transform.scale(self.surface, self.surface_size), self.surface_loc)
            
            # Update the display
            pygame.display.flip()
            # Set the framerate
            clock.tick(60)



def draw_score(screen, score, x, y):
    font = pygame.font.Font(None, 36)
    text = font.render(f"score : {score}", False, WHITE)
    screen.blit(text, (x, y))
    
    
def draw_game_over(screen, x, y):
    """Draw the game over text on the screen"""
    font = pygame.font.Font(None, 48)
    text = font.render("Game Over", False, WHITE)
    screen.blit(text, (x, y))

if __name__ == "__main__":
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Tetris')
    tetris = Tetris(screen)
    tetris.show()