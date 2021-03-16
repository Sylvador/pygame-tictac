import pygame as pg
from ...settings import CELLSIZE, BGCOLOR, OFFSETX


class CellState:
    empty = 0
    cross = 1
    zero = 2


class Cell(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.cells
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.state = CellState.empty
        self.x = x
        self.y = y
        self.image = pg.Surface((CELLSIZE, CELLSIZE))
        self.image.fill(BGCOLOR)
        self.cross_image = game.cross_image
        self.zero_image = game.zero_image
        self.rect = self.image.get_rect()
        self.rect.x = x*CELLSIZE + OFFSETX
        self.rect.y = y*CELLSIZE

    def update():
        pass

    def on_click(self, player):
        if self.state == CellState.empty:
            x, y = self.x, self.y
            if player == 'X':
                (self.game.field
                     .check_matrix[x][y]) += self.game.field.magic_matrix[x][y]
                self.state = CellState.cross
                self.image = self.cross_image
            if player == '0':
                (self.game.field
                     .check_matrix[x][y]) -= self.game.field.magic_matrix[x][y]
                self.state = CellState.zero
                self.image = self.zero_image
            return True
        return False
