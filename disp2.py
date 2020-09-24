import pygame as pg
import os
from sys import exit
os.environ['SDL_AUDIODRIVER'] = 'dsp'


class Display(object):
    def __init__(self, W, H):
        pg.init()
        self.W, self.H = W, H
        # this is already a surface
        self.window = pg.display.set_mode((W, H))
        self.surf = pg.display.get_surface()
        pg.display.flip()

    def paint(self, img):
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                exit(0)



        surf = pg.surfarray.pixels3d(self.surf)

        # blit
        #surf.blits
        self.surf.blits


