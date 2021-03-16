# тут будет импорт разных инструментов
# для настройки запуска игры (если нужно)
from .core.app import App
import pygame as pg


def main():
    app = App()
    while True:
        app.new_game()
        app.run()
        pg.time.wait(2000)
