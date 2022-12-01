import random
import pygame
from pygame.locals import QUIT
from bola import PelotaPong
from bola import Margen_H
from bola import Margen_V
from bola import FPS
from raqueta import raqueta
self.puntuacion = 0
self.puntuacion_ia = 0
def rebotar(self):
        if self.x <= -self.ancho:
            self.reiniciar()
            self.puntuacion_ia += 1
        if self.x >= VENTANA_HORI:
            self.reiniciar()
            self.puntuacion += 1
NEGRO = (0, 0, 0)  # Color del texto (RGB)
fuente = pygame.font.Font(None, 60)