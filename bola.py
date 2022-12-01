import random
import pygame
from pygame.locals import QUIT
Margen_V = 600
Margen_H = 800
FPS = 60
Fondo_Blanco = (255, 255, 255)
class PelotaPong:
    def __init__(self, fichero_imagen):
        # Imagen de la Pelota
        self.imagen = pygame.image.load(fichero_imagen).convert_alpha()

        # Dimensiones de la Pelota
        self.ancho, self.alto = self.imagen.get_size()

        # Posición de la Pelota
        self.x = Margen_H / 2 - self.ancho / 2
        self.y = Margen_V / 2 - self.alto / 2

        # Dirección de movimiento de la Pelota
        self.dir_x = random.choice([-5, 5])
        self.dir_y = random.choice([-5, 5])

    def mover(self):
        self.x += self.dir_x
        self.y += self.dir_y

    def rebotar(self):
        if self.x <= -self.ancho:
            self.reiniciar()
        if self.x >= Margen_H:
            self.reiniciar()
        if self.y <= 0:
            self.dir_y = -self.dir_y
        if self.y + self.alto >= Margen_V:
            self.dir_y = -self.dir_y
    def reiniciar(self):
        self.x = Margen_H / 2 - self.ancho / 2
        self.y = Margen_V / 2 - self.alto / 2
        self.dir_x = -self.dir_x
        self.dir_y = random.choice([-5, 5])
