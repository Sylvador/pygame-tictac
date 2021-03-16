# Тут класс приложения App с нужными методами
import sys
from os.path import dirname, join
import pygame as pg
from ..settings import WIDTH, HEIGHT, TITLE, BGCOLOR, WHITE, CELLSIZE, OFFSETX
from .components.cells import Cell
from .components.field import Field


class App:
    def __init__(self):
        self.running = False
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()

    def new_game(self):
        self.cells = pg.sprite.Group()
        self.field = Field(self)
        self.turn = 0
        self.win_state = ''
        game_folder = dirname(dirname(dirname(__file__)))
        resources_folder = join(game_folder, 'resources')
        self.cross_image = pg.transform.scale(pg.image.load(
                join(resources_folder, 'krestik.png')
            ).convert_alpha(), (CELLSIZE, CELLSIZE))
        self.zero_image = pg.transform.scale(pg.image.load(
                join(resources_folder, 'nolik.png')
            ).convert_alpha(), (CELLSIZE, CELLSIZE))
        self.zero_win_image = pg.transform.scale(pg.image.load(
                join(resources_folder, 'endgame_for_o.png')
            ).convert_alpha(), (WIDTH, HEIGHT))
        self.cross_win_image = pg.transform.scale(pg.image.load(
                join(resources_folder, 'krest.png')
            ).convert_alpha(), (WIDTH, HEIGHT))
        self.draw_image = pg.transform.scale(pg.image.load(
                join(resources_folder, 'drug.png')
            ).convert_alpha(), (WIDTH, HEIGHT))
        self.win_rect = self.draw_image.get_rect()
        for x in range(0, 3):
            for y in range(0, 3):
                self.field.cells.append(Cell(self, x, y))

    def run(self):
        self.running = True
        while self.running:
            self.dt = self.clock.tick(60)/1000
            self.events()
            self.update()
            self.draw()

    def draw_grid(self):
        for x in range(OFFSETX, 4*CELLSIZE, CELLSIZE):
            pg.draw.line(self.screen, WHITE, (x, 0), (x, 3*CELLSIZE), 6)
        for y in range(0, 4*CELLSIZE, CELLSIZE):
            pg.draw.line(self.screen, WHITE,
                         (OFFSETX, y), (3*CELLSIZE+OFFSETX, y), 6)

    def draw_endscreen(self):
        if self.win_state == 'X':
            self.screen.blit(
                    self.cross_win_image, self.win_rect
                )
        elif self.win_state == '0':
            self.screen.blit(
                    self.zero_win_image, self.win_rect
                )
        elif self.win_state == '-':
            self.screen.blit(
                    self.draw_image, self.win_rect
                )

    def draw(self):
        self.screen.fill(BGCOLOR)
        self.cells.draw(self.screen)
        self.draw_grid()
        if self.win_state != '':
            self.draw_endscreen()
        pg.display.flip()

    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        pass

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()
            if event.type == pg.MOUSEBUTTONUP:
                pos = pg.mouse.get_pos()
                clicked_sprites = [
                        s for s in self.cells if s.rect.collidepoint(pos)
                    ]
                for sprite in clicked_sprites:
                    if sprite.on_click('X' if self.turn % 2 == 0 else '0'):
                        self.turn += 1
                        self.win_state = self.field.check_win()
                        if self.win_state == '-' and self.turn != 9:
                            self.win_state = ''
                        if self.win_state != '':
                            self.running = False
