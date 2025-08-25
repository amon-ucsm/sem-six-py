import pygame as pg 
import sys

pg.init()
scr = pg.display.set_mode((600, 500))
font = pg.font.SysFont('arial', 18)
new_font = pg.font.SysFont('Timenewroman', 25)
new_font1 = pg.font.SysFont('impact', 70)

text = font.render('Welcome to Pygame World', True, (0, 255, 0))
fun = new_font.render('Enjoy the games', True, (0, 255, 255))
game_end = new_font1.render('Game ends', True, (255, 0, 0))

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    scr.fill((255, 255, 255))
    scr.blit(text, (40, 60))
    scr.blit(fun, (40, 90))
    scr.blit(game_end, (40, 140))
    pg.display.flip()