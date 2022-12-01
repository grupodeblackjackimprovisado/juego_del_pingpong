import random
import pygame
from pygame.locals import QUIT
Margen_V = 600
Margen_H = 800
Fondo_Blanco = (225, 225, 225)
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


def main():
    # Inicialización de Pygame
    pygame.init()

    # Inicialización de la superficie de dibujo (display surface)
    ventana = pygame.display.set_mode((VENTANA_HORI, VENTANA_VERT))
    pygame.display.set_caption("Pong 2")

    pelota = PelotaPong("bola_roja.png")

    # Bucle principal
    jugando = True
    while jugando:
        pelota.mover()

        ventana.fill()
        ventana.blit(pelota.imagen, (pelota.x, pelota.y))

        for event in pygame.event.get():
            if event.type == QUIT:
                jugando = False

        pygame.display.flip()
        pygame.time.Clock().tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
