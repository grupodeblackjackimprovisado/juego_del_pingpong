import random
import pygame
from pygame.locals import QUIT
from bola import PelotaPong
from bola import Margen_H
from bola import Margen_V
from bola import FPS
from juego import main
BLANCO = (255, 255, 255) 
NEGRO = (0, 0, 0)
class RaquetaPong:
    def __init__(self):
        self.imagen = pygame.image.load("raqueta.png").convert_alpha()
        self.ancho, self.alto = self.imagen.get_size()
        self.x = 0
        self.y = Margen_V/ 2 - self.alto / 2
        self.dir_y = 0
    def mover(self):
        self.y += self.dir_y
        if self.y <= 0:
            self.y = 0
        if self.y + self.alto >= Margen_V:
            self.y = Margen_V - self.alto  
    def mover_ia(self, pelota):
        if self.y > pelota.y:
            self.dir_y = -3
        elif self.y < pelota.y:
            self.dir_y = 3
        else:
            self.dir_y = 0

        self.y += self.dir_y
    def golpear(self, pelota):

        if (
            pelota.x < self.x + self.ancho
            and pelota.x > self.x
            and pelota.y + pelota.alto > self.y
            and pelota.y < self.y + self.alto
        ):
             pelota.dir_x = -pelota.dir_x
             pelota.x = self.x + self.ancho

    def golpear_ia(self, pelota):
        if (
            pelota.x + pelota.ancho > self.x
            and pelota.x < self.x + self.ancho
            and pelota.y + pelota.alto > self.y
            and pelota.y < self.y + self.alto
        ):
             pelota.dir_x = -pelota.dir_x
             pelota.x = self.x - pelota.ancho    


if __name__ == "__main__":
    main()